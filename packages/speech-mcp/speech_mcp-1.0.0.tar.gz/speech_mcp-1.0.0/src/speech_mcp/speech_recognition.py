"""
Speech recognition module for speech-mcp.

This module provides centralized speech recognition functionality including:
- Model loading and initialization
- Audio transcription
- Fallback mechanisms
- Consistent error handling

It consolidates speech recognition code that was previously duplicated
across server.py and speech_ui.py.
"""

import os
import time
import logging
import tempfile
from typing import Optional, Tuple, Dict, Any, List, Union

# Setup logging
logger = logging.getLogger(__name__)

class SpeechRecognizer:
    """
    Core speech recognition class that handles transcription of audio files.
    
    This class provides a unified interface for speech recognition with fallback mechanisms.
    It supports multiple speech recognition engines, with faster-whisper as the primary engine
    and SpeechRecognition as a fallback.
    """
    
    def __init__(self, model_name: str = "base", device: str = "cpu", compute_type: str = "int8"):
        """
        Initialize the speech recognizer.
        
        Args:
            model_name: The name of the faster-whisper model to use (e.g., "base", "small", "medium")
            device: The device to use for inference ("cpu" or "cuda")
            compute_type: The compute type to use for inference ("int8", "float16", "float32")
        """
        self.whisper_model = None
        self.sr_recognizer = None
        self.model_name = model_name
        self.device = device
        self.compute_type = compute_type
        self.is_initialized = False
        
        # Initialize the speech recognition models in the background
        self._initialize_speech_recognition()
    
    def _initialize_speech_recognition(self) -> bool:
        """
        Initialize speech recognition models.
        
        Returns:
            bool: True if initialization was successful, False otherwise
        """
        if self.is_initialized:
            logger.info("Speech recognition already initialized")
            return True
        
        # Try to initialize faster-whisper first
        try:
            logger.info(f"Loading faster-whisper speech recognition model '{self.model_name}' on {self.device}...")
            print(f"Loading faster-whisper speech recognition model '{self.model_name}' on {self.device}... This may take a moment.")
            
            import faster_whisper
            # Load the model with the specified parameters
            self.whisper_model = faster_whisper.WhisperModel(
                self.model_name, 
                device=self.device, 
                compute_type=self.compute_type
            )
            
            logger.info("faster-whisper model loaded successfully")
            print("faster-whisper speech recognition model loaded successfully!")
            
            self.is_initialized = True
            return True
            
        except ImportError as e:
            logger.error(f"Failed to load faster-whisper: {e}")
            print(f"ERROR: Failed to load faster-whisper module: {e}")
            print("Trying to fall back to SpeechRecognition library...")
            
            return self._initialize_speech_recognition_fallback()
        except Exception as e:
            logger.error(f"Error initializing faster-whisper: {e}")
            print(f"ERROR: Error initializing faster-whisper: {e}")
            print("Trying to fall back to SpeechRecognition library...")
            
            return self._initialize_speech_recognition_fallback()
    
    def _initialize_speech_recognition_fallback(self) -> bool:
        """
        Initialize fallback speech recognition using SpeechRecognition library.
        
        Returns:
            bool: True if initialization was successful, False otherwise
        """
        try:
            import speech_recognition as sr
            self.sr_recognizer = sr.Recognizer()
            
            logger.info("SpeechRecognition successfully loaded as fallback")
            print("SpeechRecognition library loaded successfully as fallback!")
            
            self.is_initialized = True
            return True
            
        except ImportError as e:
            logger.error(f"Failed to load SpeechRecognition: {e}")
            print(f"ERROR: Failed to load SpeechRecognition module: {e}")
            print("Please install it with: pip install SpeechRecognition")
            
            self.is_initialized = False
            return False
        except Exception as e:
            logger.error(f"Error initializing SpeechRecognition: {e}")
            print(f"ERROR: Error initializing SpeechRecognition: {e}")
            
            self.is_initialized = False
            return False
    
    def transcribe(self, audio_file_path: str, language: str = "en") -> Tuple[str, Dict[str, Any]]:
        """
        Transcribe an audio file using the available speech recognition engine.
        
        Args:
            audio_file_path: Path to the audio file to transcribe
            language: Language code for transcription (default: "en" for English)
            
        Returns:
            Tuple containing:
                - The transcribed text
                - A dictionary with metadata about the transcription
        """
        # Check if the file exists
        if not os.path.exists(audio_file_path):
            error_msg = f"Audio file not found: {audio_file_path}"
            logger.error(error_msg)
            return "", {"error": error_msg, "engine": "none"}
        
        # Ensure speech recognition is initialized
        if not self.is_initialized and not self._initialize_speech_recognition():
            error_msg = "Failed to initialize speech recognition"
            logger.error(error_msg)
            return "", {"error": error_msg, "engine": "none"}
        
        # Try faster-whisper first
        if self.whisper_model is not None:
            try:
                logger.info(f"Transcribing audio with faster-whisper: {audio_file_path}")
                print("Transcribing audio with faster-whisper...")
                
                transcription_start = time.time()
                segments, info = self.whisper_model.transcribe(audio_file_path, beam_size=5)
                
                # Collect all segments to form the complete transcription
                transcription = ""
                for segment in segments:
                    transcription += segment.text + " "
                
                transcription = transcription.strip()
                transcription_time = time.time() - transcription_start
                
                logger.info(f"Transcription completed in {transcription_time:.2f}s: {transcription}")
                logger.debug(f"Transcription info: {info}")
                print(f"Transcription complete: \"{transcription}\"")
                
                # Return the transcription and metadata
                return transcription, {
                    "engine": "faster-whisper",
                    "model": self.model_name,
                    "time_taken": transcription_time,
                    "language": info.language,
                    "language_probability": info.language_probability,
                    "duration": info.duration
                }
                
            except Exception as e:
                logger.error(f"Error transcribing with faster-whisper: {e}")
                print(f"ERROR: Failed to transcribe with faster-whisper: {e}")
                print("Falling back to SpeechRecognition...")
        
        # Fall back to SpeechRecognition if available
        if self.sr_recognizer is not None:
            try:
                import speech_recognition as sr
                
                logger.info(f"Transcribing audio with SpeechRecognition (fallback): {audio_file_path}")
                print("Transcribing audio with SpeechRecognition (fallback)...")
                
                transcription_start = time.time()
                
                with sr.AudioFile(audio_file_path) as source:
                    audio_data = self.sr_recognizer.record(source)
                    transcription = self.sr_recognizer.recognize_google(audio_data, language=language)
                
                transcription_time = time.time() - transcription_start
                
                logger.info(f"Fallback transcription completed in {transcription_time:.2f}s: {transcription}")
                print(f"Fallback transcription complete: \"{transcription}\"")
                
                # Return the transcription and metadata
                return transcription, {
                    "engine": "speech_recognition",
                    "api": "google",
                    "time_taken": transcription_time
                }
                
            except Exception as e:
                logger.error(f"Error transcribing with SpeechRecognition: {e}")
                print(f"ERROR: Failed to transcribe with SpeechRecognition: {e}")
        
        # If all methods fail, return an error
        error_msg = "All speech recognition methods failed"
        logger.error(error_msg)
        print(f"ERROR: {error_msg}")
        
        return "", {"error": error_msg, "engine": "none"}
    
    def cleanup_audio_file(self, audio_file_path: str) -> bool:
        """
        Clean up a temporary audio file.
        
        Args:
            audio_file_path: Path to the audio file to clean up
            
        Returns:
            bool: True if the file was cleaned up successfully, False otherwise
        """
        try:
            if os.path.exists(audio_file_path):
                logger.debug(f"Removing temporary audio file: {audio_file_path}")
                os.unlink(audio_file_path)
                return True
            return False
        except Exception as e:
            logger.error(f"Error removing temporary audio file: {e}")
            return False
    
    def get_available_models(self) -> List[Dict[str, Any]]:
        """
        Get a list of available speech recognition models.
        
        Returns:
            List of dictionaries containing model information
        """
        models = []
        
        # Add faster-whisper models if available
        if self.whisper_model is not None:
            models.extend([
                {"name": "tiny", "engine": "faster-whisper", "description": "Fastest, least accurate"},
                {"name": "base", "engine": "faster-whisper", "description": "Fast, good accuracy"},
                {"name": "small", "engine": "faster-whisper", "description": "Balanced speed and accuracy"},
                {"name": "medium", "engine": "faster-whisper", "description": "Good accuracy, slower"},
                {"name": "large-v2", "engine": "faster-whisper", "description": "Best accuracy, slowest"}
            ])
        
        # Add SpeechRecognition models if available
        if self.sr_recognizer is not None:
            models.append({
                "name": "google", 
                "engine": "speech_recognition", 
                "description": "Google Speech-to-Text API (requires internet)"
            })
        
        return models
    
    def get_current_model(self) -> Dict[str, Any]:
        """
        Get information about the currently active model.
        
        Returns:
            Dictionary containing information about the current model
        """
        if self.whisper_model is not None:
            return {
                "name": self.model_name,
                "engine": "faster-whisper",
                "device": self.device,
                "compute_type": self.compute_type
            }
        elif self.sr_recognizer is not None:
            return {
                "name": "google",
                "engine": "speech_recognition"
            }
        else:
            return {
                "name": "none",
                "engine": "none",
                "error": "No speech recognition model initialized"
            }
    
    def set_model(self, model_name: str, device: Optional[str] = None, compute_type: Optional[str] = None) -> bool:
        """
        Set the speech recognition model to use.
        
        Args:
            model_name: The name of the model to use
            device: The device to use for inference (optional)
            compute_type: The compute type to use for inference (optional)
            
        Returns:
            bool: True if the model was set successfully, False otherwise
        """
        # Update parameters if provided
        if device is not None:
            self.device = device
        
        if compute_type is not None:
            self.compute_type = compute_type
        
        # If the model name is the same and already initialized, no need to reinitialize
        if model_name == self.model_name and self.is_initialized and self.whisper_model is not None:
            logger.info(f"Model '{model_name}' is already active")
            return True
        
        # Update the model name
        self.model_name = model_name
        
        # Reset initialization state
        self.is_initialized = False
        self.whisper_model = None
        
        # Reinitialize with the new model
        return self._initialize_speech_recognition()


# Create a singleton instance for easy import
default_recognizer = SpeechRecognizer()

def transcribe_audio(audio_file_path: str, language: str = "en") -> str:
    """
    Transcribe an audio file using the default speech recognizer.
    
    This is a convenience function that uses the default recognizer instance.
    
    Args:
        audio_file_path: Path to the audio file to transcribe
        language: Language code for transcription (default: "en" for English)
        
    Returns:
        The transcribed text
    """
    transcription, _ = default_recognizer.transcribe(audio_file_path, language)
    return transcription

def initialize_speech_recognition(
    model_name: str = "base", 
    device: str = "cpu", 
    compute_type: str = "int8"
) -> bool:
    """
    Initialize the default speech recognizer with the specified parameters.
    
    Args:
        model_name: The name of the faster-whisper model to use
        device: The device to use for inference
        compute_type: The compute type to use for inference
        
    Returns:
        bool: True if initialization was successful, False otherwise
    """
    global default_recognizer
    default_recognizer = SpeechRecognizer(model_name, device, compute_type)
    return default_recognizer.is_initialized

def get_available_models() -> List[Dict[str, Any]]:
    """
    Get a list of available speech recognition models.
    
    Returns:
        List of dictionaries containing model information
    """
    return default_recognizer.get_available_models()

def get_current_model() -> Dict[str, Any]:
    """
    Get information about the currently active model.
    
    Returns:
        Dictionary containing information about the current model
    """
    return default_recognizer.get_current_model()