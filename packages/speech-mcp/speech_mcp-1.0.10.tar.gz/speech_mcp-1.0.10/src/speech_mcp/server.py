import sys
import os
import json
import time
import threading
import tempfile
import subprocess
import psutil
import importlib.util
from typing import Dict, Optional, Callable

from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

# Import the centralized logger
from speech_mcp.utils.logger import get_logger

# Get a logger for this module
logger = get_logger(__name__, component="server")

# Import centralized constants
from speech_mcp.constants import (
    STATE_FILE, DEFAULT_SPEECH_STATE, SERVER_LOG_FILE,
    TRANSCRIPTION_FILE, RESPONSE_FILE, COMMAND_FILE,
    CMD_LISTEN, CMD_SPEAK, CMD_IDLE, CMD_UI_READY, CMD_UI_CLOSED,
    SPEECH_TIMEOUT, ENV_TTS_VOICE
)

# Import shared audio processor and speech recognition
from speech_mcp.audio_processor import AudioProcessor
from speech_mcp.speech_recognition import initialize_speech_recognition as init_speech_recognition
from speech_mcp.speech_recognition import transcribe_audio as transcribe_audio_file

mcp = FastMCP("speech")

# Define TTS engine variable
tts_engine = None

# Define initialize_kokoro_tts function before it's used
def initialize_kokoro_tts():
    """Initialize Kokoro TTS specifically"""
    global tts_engine
    
    try:
        # Import the Kokoro TTS adapter
        from speech_mcp.tts_adapters import KokoroTTS
        
        # Try to get voice preference from config or environment
        voice = None
        try:
            from speech_mcp.config import get_setting, get_env_setting
            
            # First check environment variable
            env_voice = get_env_setting(ENV_TTS_VOICE)
            if env_voice:
                voice = env_voice
            else:
                # Then check config file
                config_voice = get_setting("tts", "voice", None)
                if config_voice:
                    voice = config_voice
        except ImportError:
            pass
        
        # Initialize Kokoro with default or saved voice settings
        if voice:
            tts_engine = KokoroTTS(voice=voice, lang_code="a", speed=1.0)
        else:
            tts_engine = KokoroTTS(voice="af_heart", lang_code="a", speed=1.0)
        
        if tts_engine.is_initialized and tts_engine.kokoro_available:
            logger.info("Kokoro TTS initialized successfully")
            return True
        else:
            # If Kokoro initialization failed, set tts_engine to None so we'll try fallback later
            tts_engine = None
            logger.warning("Kokoro TTS initialization failed, will use fallback")
            return False
            
    except ImportError as e:
        logger.error(f"Kokoro TTS import error: {e}")
        return False
    except Exception as e:
        logger.error(f"Kokoro TTS initialization error: {e}")
        return False

# Initialize Kokoro TTS on server start (asynchronously)
logger.info("Starting asynchronous Kokoro TTS initialization...")
# Use a thread-safe variable to track initialization status
import threading
kokoro_init_lock = threading.Lock()
kokoro_init_status = {"initialized": False, "in_progress": True}

def async_kokoro_init():
    """Initialize Kokoro TTS in a background thread"""
    global kokoro_init_status
    try:
        # Attempt to initialize Kokoro
        result = initialize_kokoro_tts()
        
        # Update status with thread safety
        with kokoro_init_lock:
            kokoro_init_status["initialized"] = result
            kokoro_init_status["in_progress"] = False
        
        if result:
            logger.info("Async Kokoro TTS initialization completed successfully")
        else:
            logger.warning("Async Kokoro TTS initialization failed, will use fallback when needed")
    except Exception as e:
        # Update status with thread safety
        with kokoro_init_lock:
            kokoro_init_status["initialized"] = False
            kokoro_init_status["in_progress"] = False
        logger.error(f"Error during async Kokoro TTS initialization: {e}")

# Start the initialization in a background thread
kokoro_init_thread = threading.Thread(target=async_kokoro_init)
kokoro_init_thread.daemon = True
kokoro_init_thread.start()

# Load speech state from file or use default
def load_speech_state():
    try:
        if os.path.exists(STATE_FILE):
            logger.debug(f"Loading speech state from {STATE_FILE}")
            with open(STATE_FILE, 'r') as f:
                state = json.load(f)
                logger.debug(f"Speech state loaded: {state}")
                return state
        else:
            logger.debug(f"State file {STATE_FILE} not found, using default state")
            return DEFAULT_SPEECH_STATE.copy()
    except Exception as e:
        logger.error(f"Error loading speech state: {e}")
        return DEFAULT_SPEECH_STATE.copy()

# Save speech state to file
def save_speech_state(state, create_response_file=False):
    try:
        logger.debug(f"Saving speech state to {STATE_FILE}")
        with open(STATE_FILE, 'w') as f:
            json.dump(state, f)
        
        # Only create response file if specifically requested
        if create_response_file:
            # Create or update response file for UI communication
            # This helps ensure the UI is properly notified of state changes
            if state.get("speaking", False):
                # If speaking, write the response to the file for the UI to pick up
                logger.debug(f"Creating response file with text: {state.get('last_response', '')[:30]}...")
                with open(RESPONSE_FILE, 'w') as f:
                    f.write(state.get("last_response", ""))
        
        # Create a special command file to signal state changes to the UI
        command = ""
        if state.get("listening", False):
            command = CMD_LISTEN
        elif state.get("speaking", False):
            command = CMD_SPEAK
        else:
            command = CMD_IDLE
        
        logger.debug(f"Writing command {command} to {COMMAND_FILE}")
        with open(COMMAND_FILE, 'w') as f:
            f.write(command)
    except Exception as e:
        logger.error(f"Error saving speech state: {e}")
        pass

# Initialize speech state
speech_state = load_speech_state()

def initialize_speech_recognition():
    """Initialize speech recognition"""
    try:
        # Use the centralized speech recognition module
        result = init_speech_recognition(model_name="base", device="cpu", compute_type="int8")
        return result
    except Exception:
        return False

def initialize_tts():
    """Initialize text-to-speech"""
    global tts_engine, kokoro_init_status
    
    if tts_engine is not None:
        return True
    
    # Check if Kokoro initialization is still in progress
    kokoro_in_progress = False
    with kokoro_init_lock:
        kokoro_in_progress = kokoro_init_status["in_progress"]
        kokoro_initialized = kokoro_init_status["initialized"]
    
    # If Kokoro initialization completed successfully in the background,
    # but tts_engine is not set yet, we need to initialize it now
    if not kokoro_in_progress and kokoro_initialized and tts_engine is None:
        logger.info("Kokoro was initialized asynchronously, but tts_engine is not set. Reinitializing...")
        if initialize_kokoro_tts():
            return True
    
    try:
        # Try to import the TTS adapters
        try:
            # First try to use the new adapter system
            from speech_mcp.tts_adapters import KokoroTTS, Pyttsx3TTS
            
            # Try to get voice preference from config or environment
            voice = None
            try:
                from speech_mcp.config import get_setting, get_env_setting
                
                # First check environment variable
                env_voice = get_env_setting(ENV_TTS_VOICE)
                if env_voice:
                    voice = env_voice
                else:
                    # Then check config file
                    config_voice = get_setting("tts", "voice", None)
                    if config_voice:
                        voice = config_voice
            except ImportError:
                pass
            
            # First try Kokoro (our primary TTS engine)
            try:
                # Only try Kokoro if it's not still initializing
                if not kokoro_in_progress:
                    # Initialize with default or saved voice settings
                    if voice:
                        tts_engine = KokoroTTS(voice=voice, lang_code="a", speed=1.0)
                    else:
                        tts_engine = KokoroTTS(voice="af_heart", lang_code="a", speed=1.0)
                    
                    if tts_engine.is_initialized:
                        return True
            except ImportError:
                pass
            except Exception:
                pass
            
            # Fall back to pyttsx3 adapter
            try:
                # Initialize with default or saved voice settings
                if voice and voice.startswith("pyttsx3:"):
                    tts_engine = Pyttsx3TTS(voice=voice, lang_code="en", speed=1.0)
                else:
                    tts_engine = Pyttsx3TTS(lang_code="en", speed=1.0)
                
                if tts_engine.is_initialized:
                    return True
            except ImportError:
                pass
            except Exception:
                pass
        
        except ImportError:
            pass
        
        # Direct fallback to pyttsx3 if adapters are not available
        try:
            import pyttsx3
            tts_engine = pyttsx3.init()
            return True
        except ImportError:
            return False
        except Exception:
            return False
            
    except Exception:
        return False

def ensure_ui_is_running():
    """Ensure the PyQt UI process is running"""
    global speech_state
    
    # Check if UI is already active
    if speech_state.get("ui_active", False) and speech_state.get("ui_process_id"):
        # Check if the process is actually running
        try:
            process_id = speech_state["ui_process_id"]
            if psutil.pid_exists(process_id):
                process = psutil.Process(process_id)
                if process.status() != psutil.STATUS_ZOMBIE:
                    return True
        except Exception:
            pass
    
    # Check for any existing UI processes by looking for Python processes running speech_mcp.ui
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = proc.info.get('cmdline', [])
                if cmdline and len(cmdline) >= 3:
                    # Look specifically for PyQt UI processes
                    if 'python' in cmdline[0].lower() and '-m' in cmdline[1] and 'speech_mcp.ui' in cmdline[2]:
                        # Found an existing PyQt UI process
                        
                        # Update our state to track this process
                        speech_state["ui_active"] = True
                        speech_state["ui_process_id"] = proc.info['pid']
                        save_speech_state(speech_state, False)
                        
                        return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
    except Exception:
        pass
    
    # No UI process found, we'll need to start one using the launch_ui tool
    return False

def record_audio():
    """Record audio from the microphone and return the audio data"""
    try:
        # Create an instance of the shared AudioProcessor
        audio_processor = AudioProcessor()
        
        # Use the AudioProcessor to record audio
        audio_file_path = audio_processor.record_audio()
        
        if not audio_file_path:
            raise Exception("Failed to record audio")
        
        return audio_file_path
    
    except Exception as e:
        raise Exception(f"Error recording audio: {str(e)}")

def transcribe_audio(audio_file_path):
    """Transcribe audio file using the speech recognition module"""
    try:
        if not initialize_speech_recognition():
            raise Exception("Failed to initialize speech recognition")
        
        # Use the centralized speech recognition module
        transcription = transcribe_audio_file(audio_file_path)
        
        if not transcription:
            raise Exception("Transcription failed or returned empty result")
        
        # Clean up the temporary file
        try:
            os.unlink(audio_file_path)
        except Exception:
            pass
        
        return transcription
    
    except Exception as e:
        raise Exception(f"Error transcribing audio: {str(e)}")

def speak_text(text):
    """Speak text using TTS engine"""
    global tts_engine, kokoro_init_status
    
    if not text:
        raise McpError(
            ErrorData(
                INVALID_PARAMS,
                "No text provided to speak."
            )
        )
    
    # Set speaking state
    speech_state["speaking"] = True
    speech_state["last_response"] = text
    
    # Save state but don't create response file - we'll handle TTS directly
    save_speech_state(speech_state, False)
    
    try:
        # Check if Kokoro initialization is in progress
        kokoro_in_progress = False
        with kokoro_init_lock:
            kokoro_in_progress = kokoro_init_status["in_progress"]
            kokoro_initialized = kokoro_init_status["initialized"]
        
        # If Kokoro is still initializing and we don't have a TTS engine yet,
        # we'll use a fallback immediately rather than waiting
        if kokoro_in_progress and tts_engine is None:
            logger.info("Kokoro initialization still in progress, using fallback TTS for now")
            # Try to initialize a fallback TTS engine
            try:
                from speech_mcp.tts_adapters import Pyttsx3TTS
                tts_engine = Pyttsx3TTS(lang_code="en", speed=1.0)
            except Exception:
                # If fallback initialization fails, we'll simulate speech
                pass
        
        # Use the already initialized TTS engine or initialize if needed
        if tts_engine is None:
            # First check if Kokoro initialization completed successfully
            if not kokoro_in_progress and kokoro_initialized:
                # Kokoro was initialized successfully in the background
                logger.info("Using Kokoro TTS that was initialized asynchronously")
                # No need to initialize again, the global tts_engine should be set
            else:
                # If Kokoro initialization failed or is still in progress, try the general TTS initialization
                if not initialize_tts():
                    # If all TTS initialization fails, simulate speech with a delay
                    speaking_duration = len(text) * 0.05  # 50ms per character
                    time.sleep(speaking_duration)
                    
                    # Update state
                    speech_state["speaking"] = False
                    save_speech_state(speech_state, False)
                    return f"Simulated speaking: {text}"
        
        # Use TTS engine to speak text directly without going through the UI
        tts_start = time.time()
        
        # Use the appropriate method based on the TTS engine type
        if hasattr(tts_engine, 'speak'):
            # Use the speak method (our adapter system or Kokoro adapter)
            result = tts_engine.speak(text)
        elif hasattr(tts_engine, 'say'):
            # Use pyttsx3 directly
            tts_engine.say(text)
            tts_engine.runAndWait()
        else:
            # Simulate speech as fallback
            speaking_duration = len(text) * 0.05  # 50ms per character
            time.sleep(speaking_duration)
        
        # Update state
        speech_state["speaking"] = False
        save_speech_state(speech_state, False)
        
        return f"Spoke: {text}"
    
    except Exception as e:
        # Update state on error
        speech_state["speaking"] = False
        save_speech_state(speech_state, False)
        
        # Simulate speech with a delay as fallback
        speaking_duration = len(text) * 0.05  # 50ms per character
        time.sleep(speaking_duration)
        
        return f"Error speaking text: {str(e)}"

def listen_for_speech() -> str:
    """Listen for speech and return transcription"""
    global speech_state
    
    # Set listening state
    speech_state["listening"] = True
    save_speech_state(speech_state, False)
    
    try:
        # Record audio
        audio_file_path = record_audio()
        
        # Transcribe audio
        transcription = transcribe_audio(audio_file_path)
        
        # Update state
        speech_state["listening"] = False
        speech_state["last_transcript"] = transcription
        save_speech_state(speech_state, False)
        
        return transcription
    
    except Exception as e:
        # Update state on error
        speech_state["listening"] = False
        save_speech_state(speech_state, False)
        
        raise McpError(
            ErrorData(
                INTERNAL_ERROR,
                f"Error during speech recognition: {str(e)}"
            )
        )

def cleanup_ui_process():
    """Clean up the PyQt UI process when the server shuts down"""
    global speech_state
    
    if speech_state.get("ui_active", False) and speech_state.get("ui_process_id"):
        try:
            process_id = speech_state["ui_process_id"]
            if psutil.pid_exists(process_id):
                process = psutil.Process(process_id)
                process.terminate()
                try:
                    process.wait(timeout=3)
                except psutil.TimeoutExpired:
                    process.kill()
            
            # Update state
            speech_state["ui_active"] = False
            speech_state["ui_process_id"] = None
            save_speech_state(speech_state, False)
            
            # Write a UI_CLOSED command to the command file
            try:
                with open(COMMAND_FILE, 'w') as f:
                    f.write(CMD_UI_CLOSED)
            except Exception:
                pass
        except Exception:
            pass

# Register cleanup function to be called on exit
import atexit
atexit.register(cleanup_ui_process)

@mcp.tool()
def launch_ui() -> str:
    """
    Launch the speech UI.
    
    This will start the speech UI window that shows the microphone status and speech visualization.
    The UI is required for visual feedback during speech recognition.
    
    Returns:
        A message indicating whether the UI was successfully launched.
    """
    global speech_state
    
    # Check if UI is already running
    if ensure_ui_is_running():
        return "Speech UI is already running."
    
    # Check if a voice preference is saved
    has_voice_preference = False
    try:
        # Import config module if available
        if importlib.util.find_spec("speech_mcp.config") is not None:
            from speech_mcp.config import get_setting, get_env_setting
            
            # Check environment variable
            env_voice = get_env_setting(ENV_TTS_VOICE)
            if env_voice:
                has_voice_preference = True
            else:
                # Check config file
                config_voice = get_setting("tts", "voice", None)
                if config_voice:
                    has_voice_preference = True
    except Exception:
        pass
    
    # Start a new UI process
    try:
        # Check for any existing UI processes first to prevent duplicates
        existing_ui = False
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = proc.info.get('cmdline', [])
                if cmdline and len(cmdline) >= 3:
                    # Look specifically for PyQt UI processes
                    if 'python' in cmdline[0].lower() and '-m' in cmdline[1] and 'speech_mcp.ui' in cmdline[2]:
                        # Found an existing PyQt UI process
                        existing_ui = True
                        
                        # Update our state to track this process
                        speech_state["ui_active"] = True
                        speech_state["ui_process_id"] = proc.info['pid']
                        save_speech_state(speech_state, False)
                        
                        return f"Speech PyQt UI is already running with PID {proc.info['pid']}."
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        
        # Start a new UI process if none exists
        if not existing_ui:
            # Clear any existing command file
            try:
                if os.path.exists(COMMAND_FILE):
                    os.remove(COMMAND_FILE)
            except Exception:
                pass
            
            # Start the UI process
            ui_process = subprocess.Popen(
                [sys.executable, "-m", "speech_mcp.ui"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Update the speech state
            speech_state["ui_active"] = True
            speech_state["ui_process_id"] = ui_process.pid
            save_speech_state(speech_state, False)
            
            # Wait for UI to fully initialize by checking for the UI_READY command
            max_wait_time = 10  # Maximum wait time in seconds
            wait_interval = 0.2  # Check every 200ms
            waited_time = 0
            ui_ready = False
            
            while waited_time < max_wait_time:
                # Check if the process is still running
                if not psutil.pid_exists(ui_process.pid):
                    return "ERROR: PyQt UI process terminated unexpectedly."
                
                # Check if the command file exists and contains UI_READY
                if os.path.exists(COMMAND_FILE):
                    try:
                        with open(COMMAND_FILE, 'r') as f:
                            command = f.read().strip()
                            if command == CMD_UI_READY:
                                ui_ready = True
                                break
                    except Exception:
                        pass
                
                # Wait before checking again
                time.sleep(wait_interval)
                waited_time += wait_interval
            
            if ui_ready:
                # Check if we have a voice preference
                if has_voice_preference:
                    return f"PyQt Speech UI launched successfully with PID {ui_process.pid} and is ready."
                else:
                    return f"PyQt Speech UI launched successfully with PID {ui_process.pid}. Please select a voice to continue."
            else:
                return f"PyQt Speech UI launched with PID {ui_process.pid}, but readiness state is unknown."
    except Exception as e:
        return f"ERROR: Failed to launch PyQt Speech UI: {str(e)}"

@mcp.tool()
def start_conversation() -> str:
    """
    Start a voice conversation by beginning to listen.
    
    This will initialize the speech recognition system and immediately start listening for user input.
    
    Returns:
        The transcription of the user's speech.
    """
    global speech_state
    
    # Force reset the speech state to avoid any stuck states
    speech_state = DEFAULT_SPEECH_STATE.copy()
    save_speech_state(speech_state, False)
    
    # Initialize speech recognition if not already done
    if not initialize_speech_recognition():
        return "ERROR: Failed to initialize speech recognition."
    
    # Check if UI is running but don't launch it automatically
    ensure_ui_is_running()
    
    # Start listening
    try:
        # Set listening state before starting to ensure UI shows the correct state
        speech_state["listening"] = True
        save_speech_state(speech_state, False)
        
        # Create a special command file to signal LISTEN state to the UI
        # This ensures the audio blips are played
        try:
            with open(COMMAND_FILE, 'w') as f:
                f.write(CMD_LISTEN)
        except Exception:
            pass
        
        # Use a queue to get the result from the thread
        import queue
        result_queue = queue.Queue()
        
        def listen_and_queue():
            try:
                result = listen_for_speech()
                result_queue.put(result)
            except Exception as e:
                result_queue.put(f"ERROR: {str(e)}")
        
        # Start the thread
        listen_thread = threading.Thread(target=listen_and_queue)
        listen_thread.daemon = True
        listen_thread.start()
        
        # Wait for the result with a timeout
        try:
            transcription = result_queue.get(timeout=SPEECH_TIMEOUT)
            
            # Signal that we're done listening
            speech_state["listening"] = False
            save_speech_state(speech_state, False)
            
            # Create a special command file to signal IDLE state to the UI
            # This ensures the audio blips are played
            try:
                with open(COMMAND_FILE, 'w') as f:
                    f.write(CMD_IDLE)
            except Exception:
                pass
            
            return transcription
        except queue.Empty:
            # Update state to stop listening
            speech_state["listening"] = False
            save_speech_state(speech_state, False)
            
            # Signal that we're done listening
            try:
                with open(COMMAND_FILE, 'w') as f:
                    f.write(CMD_IDLE)
            except Exception:
                pass
            
            # Create an emergency transcription
            emergency_message = f"ERROR: Timeout waiting for speech transcription after {SPEECH_TIMEOUT} seconds."
            return emergency_message
    
    except Exception as e:
        # Update state to stop listening
        speech_state["listening"] = False
        save_speech_state(speech_state, False)
        
        # Signal that we're done listening
        try:
            with open(COMMAND_FILE, 'w') as f:
                f.write(CMD_IDLE)
        except Exception:
            pass
        
        # Return an error message instead of raising an exception
        error_message = f"ERROR: Failed to start conversation: {str(e)}"
        return error_message

@mcp.tool()
def reply(text: str, wait_for_response: bool = True) -> str:
    """
    Speak the provided text and optionally listen for a response.
    
    This will speak the given text and then immediately start listening for user input
    if wait_for_response is True. If wait_for_response is False, it will just speak
    the text without listening for a response.
    
    Args:
        text: The text to speak to the user
        wait_for_response: Whether to wait for and return the user's response (default: True)
        
    Returns:
        If wait_for_response is True: The transcription of the user's response.
        If wait_for_response is False: A confirmation message that the text was spoken.
    """
    global speech_state
    
    # Reset listening and speaking states to ensure we're in a clean state
    speech_state["listening"] = False
    speech_state["speaking"] = False
    save_speech_state(speech_state, False)
    
    # Clear any existing response file to prevent double-speaking
    try:
        if os.path.exists(RESPONSE_FILE):
            os.remove(RESPONSE_FILE)
    except Exception:
        pass
    
    # Speak the text
    try:
        speak_text(text)
        
        # Add a small delay to ensure speaking is complete
        time.sleep(0.5)
    except Exception as e:
        return f"ERROR: Failed to speak text: {str(e)}"
    
    # If we don't need to wait for a response, return now
    if not wait_for_response:
        return f"Spoke: {text}"
    
    # Check if UI is running but don't launch it automatically
    ensure_ui_is_running()
    
    # Start listening for response
    try:
        # Use a queue to get the result from the thread
        import queue
        result_queue = queue.Queue()
        
        def listen_and_queue():
            try:
                result = listen_for_speech()
                result_queue.put(result)
            except Exception as e:
                result_queue.put(f"ERROR: {str(e)}")
        
        # Start the thread
        listen_thread = threading.Thread(target=listen_and_queue)
        listen_thread.daemon = True
        listen_thread.start()
        
        # Wait for the result with a timeout
        try:
            transcription = result_queue.get(timeout=SPEECH_TIMEOUT)
            return transcription
        except queue.Empty:
            # Update state to stop listening
            speech_state["listening"] = False
            save_speech_state(speech_state, False)
            
            # Create an emergency transcription
            emergency_message = f"ERROR: Timeout waiting for speech transcription after {SPEECH_TIMEOUT} seconds."
            return emergency_message
    
    except Exception as e:
        # Update state to stop listening
        speech_state["listening"] = False
        save_speech_state(speech_state, False)
        
        # Return an error message instead of raising an exception
        error_message = f"ERROR: Failed to listen for response: {str(e)}"
        return error_message

@mcp.tool()
def close_ui() -> str:
    """
    Close the speech UI window.
    
    This will gracefully shut down the speech UI window if it's currently running.
    Use this when you're done with voice interaction to clean up resources.
    
    Returns:
        A message indicating whether the UI was successfully closed.
    """
    global speech_state
    
    # Check if UI is running
    if speech_state.get("ui_active", False) and speech_state.get("ui_process_id"):
        try:
            process_id = speech_state["ui_process_id"]
            if psutil.pid_exists(process_id):
                # Check if it's actually our UI process (not just a reused PID)
                try:
                    process = psutil.Process(process_id)
                    cmdline = process.cmdline()
                    if not any('speech_mcp.ui' in cmd for cmd in cmdline):
                        # Update state since this isn't our process
                        speech_state["ui_active"] = False
                        speech_state["ui_process_id"] = None
                        save_speech_state(speech_state, False)
                        return "No active Speech UI found to close (PID was reused by another process)."
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
                
                # First try to gracefully close the UI by writing a UI_CLOSED command
                try:
                    with open(COMMAND_FILE, 'w') as f:
                        f.write(CMD_UI_CLOSED)
                    
                    # Give the UI a moment to close gracefully
                    time.sleep(1.0)
                except Exception:
                    pass
                
                # Now check if the process is still running
                if psutil.pid_exists(process_id):
                    # Process is still running, terminate it
                    process = psutil.Process(process_id)
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except psutil.TimeoutExpired:
                        process.kill()
            
            # Update state
            speech_state["ui_active"] = False
            speech_state["ui_process_id"] = None
            save_speech_state(speech_state, False)
            
            return "Speech UI was closed successfully."
        except Exception as e:
            return f"ERROR: Failed to close Speech UI: {str(e)}"
    else:
        return "No active Speech UI found to close."

@mcp.resource(uri="mcp://speech/usage_guide")
def usage_guide() -> str:
    """
    Return the usage guide for the Speech MCP.
    """
    return """
    # Speech MCP Usage Guide
    
    This MCP extension provides voice interaction capabilities with a simplified interface.
    
    ## How to Use
    
    1. Launch the speech UI for visual feedback (optional but recommended):
       ```
       launch_ui()
       ```
       This starts the visual interface that shows when the microphone is active.
       
    2. Start a conversation:
       ```
       user_input = start_conversation()
       ```
       This initializes the speech recognition system and immediately starts listening for user input.
       Note: The first time you run this, it will download the faster-whisper model which may take a moment.
    
    3. Reply to the user and get their response:
       ```
       user_response = reply("Your response text here")
       ```
       This speaks your response and then listens for the user's reply.
       
    4. Speak without waiting for a response:
       ```
       reply("This is just an announcement", wait_for_response=False)
       ```
       This speaks the text but doesn't listen for a response, useful for announcements or confirmations.
       
    5. Close the speech UI when done:
       ```
       close_ui()
       ```
       This gracefully closes the speech UI window when you're finished with voice interaction.
    
    ## Typical Workflow
    
    1. Start the conversation to get the initial user input
    2. Process the transcribed speech
    3. Use the reply function to respond and get the next user input
    4. Repeat steps 2-3 for a continuous conversation
    
    ## Example Conversation Flow
    
    ```python
    # Start the conversation
    user_input = start_conversation()
    
    # Process the input and generate a response
    # ...
    
    # Reply to the user and get their response
    follow_up = reply("Here's my response to your question.")
    
    # Process the follow-up and reply again
    reply("I understand your follow-up question. Here's my answer.")
    
    # Make an announcement without waiting for a response
    reply("I'll notify you when the process is complete.", wait_for_response=False)
    
    # Close the UI when done with voice interaction
    close_ui()
    ```
    
    ## Tips
    
    - For best results, use a quiet environment and speak clearly
    - Kokoro TTS is automatically initialized on server start for faster response times
    - Use the `launch_ui()` function to start the visual PyQt interface:
      - The PyQt UI shows when the microphone is active and listening
      - A blue pulsing circle indicates active listening
      - A green circle indicates the system is speaking
      - Voice selection is available in the UI dropdown
      - Only one UI instance can run at a time (prevents duplicates)
    - The system automatically detects silence to know when you've finished speaking
      - Silence detection waits for 5 seconds of quiet before stopping recording
      - This allows for natural pauses in speech without cutting off
    - The overall listening timeout is set to 10 minutes to allow for extended thinking time or long pauses
    """

@mcp.resource(uri="mcp://speech/kokoro_tts")
def kokoro_tts_guide() -> str:
    """
    Return information about the Kokoro TTS adapter.
    """
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "kokoro_tts_adapter.md"), 'r') as f:
            return f.read()
    except Exception:
        return """
        # Kokoro TTS Adapter
        
        Kokoro is a high-quality neural text-to-speech engine that can be used with speech-mcp.
        
        To install Kokoro, run:
        ```
        python scripts/install_kokoro.py
        ```
        
        For more information, see the documentation in the speech-mcp repository.
        """

@mcp.resource(uri="mcp://speech/auto_initialization")
def auto_initialization_guide() -> str:
    """
    Return information about automatic TTS initialization.
    """
    return """
    # Asynchronous TTS Initialization
    
    The speech-mcp extension automatically initializes the Kokoro TTS engine when the server starts,
    but now does so asynchronously in a background thread. This ensures that voice capabilities are 
    immediately available without blocking the server startup process.
    
    ## How it works
    
    1. When the server starts, it launches a background thread to initialize the Kokoro TTS engine
    2. The server continues to start up and respond to requests while Kokoro initializes
    3. If a speech request comes in before Kokoro is fully initialized:
       - The system will use a fallback TTS engine (pyttsx3) temporarily
       - Once Kokoro initialization completes, it will be used for subsequent requests
    4. The initialization status is tracked and logged for troubleshooting
    
    ## Voice Selection
    
    The asynchronous initialization will:
    
    1. Check for a voice preference in the environment variable `SPEECH_MCP_TTS_VOICE`
    2. If not found, check the config file at `~/.config/speech-mcp/config.json`
    3. If no preference is found, use the default voice "af_heart" (American female)
    
    ## Benefits
    
    - Server starts up quickly without waiting for TTS initialization
    - Speech functionality is available immediately using fallback TTS if needed
    - Kokoro is still used as the primary TTS engine once initialization completes
    - Smooth transition from fallback to Kokoro without user intervention
    
    ## Troubleshooting
    
    If you experience issues with TTS initialization, check the logs at:
    
    ```
    ~/.speech-mcp/logs/speech-mcp-server.log
    ```
    
    Common issues include:
    
    - Kokoro not installed (install with `pip install kokoro`)
    - Missing dependencies for Kokoro (torch, soundfile)
    - Invalid voice selection in config or environment
    """
