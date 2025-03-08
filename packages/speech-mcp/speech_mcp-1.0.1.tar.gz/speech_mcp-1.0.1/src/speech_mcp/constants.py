"""
Centralized constants for speech-mcp.

This module provides constants used throughout the speech-mcp extension.
It eliminates duplication by centralizing all shared constants in one place.
"""

import os
import sys
import pyaudio
from pathlib import Path

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, "speech_state.json")
TRANSCRIPTION_FILE = os.path.join(BASE_DIR, "transcription.txt")
RESPONSE_FILE = os.path.join(BASE_DIR, "response.txt")
COMMAND_FILE = os.path.join(BASE_DIR, "ui_command.txt")

# Log files
SERVER_LOG_FILE = os.path.join(BASE_DIR, "speech-mcp-server.log")
UI_LOG_FILE = os.path.join(BASE_DIR, "speech-mcp-ui.log")
MAIN_LOG_FILE = os.path.join(BASE_DIR, "speech-mcp.log")

# Audio parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Audio notification files
AUDIO_DIR = os.path.join(BASE_DIR, "resources", "audio")
START_LISTENING_SOUND = os.path.join(AUDIO_DIR, "start_listening.wav")
STOP_LISTENING_SOUND = os.path.join(AUDIO_DIR, "stop_listening.wav")

# Default speech state
DEFAULT_SPEECH_STATE = {
    "listening": False,
    "speaking": False,
    "last_transcript": "",
    "last_response": "",
    "ui_active": False,
    "ui_process_id": None
}

# Configuration paths
CONFIG_DIR = os.path.join(str(Path.home()), '.config', 'speech-mcp')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')

# Environment variable names
ENV_TTS_VOICE = "SPEECH_MCP_TTS_VOICE"

# Default configuration values
DEFAULT_CONFIG = {
    'tts': {
        'engine': 'kokoro',
        'voice': 'af_heart',
        'speed': 1.0,
        'lang_code': 'a'
    },
    'stt': {
        'engine': 'faster-whisper',
        'model': 'base',
        'device': 'cpu',
        'compute_type': 'int8'
    },
    'ui': {
        'theme': 'dark'
    }
}

# UI Commands
CMD_LISTEN = "LISTEN"
CMD_SPEAK = "SPEAK"
CMD_IDLE = "IDLE"
CMD_UI_READY = "UI_READY"
CMD_UI_CLOSED = "UI_CLOSED"

# Speech recognition parameters
SILENCE_THRESHOLD = 0.008  # Reduced threshold to be more sensitive to quiet speech
MAX_SILENCE_DURATION = 2.0  # 2 seconds of silence to stop recording
SILENCE_CHECK_INTERVAL = 0.1  # Check every 100ms
SPEECH_TIMEOUT = 600  # 10 minutes timeout for speech recognition