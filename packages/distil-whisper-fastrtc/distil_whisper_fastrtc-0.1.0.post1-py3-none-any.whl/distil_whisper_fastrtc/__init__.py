from .model import DistilWhisperSTT, get_stt_model, STTModel
from .utils import detect_device, load_audio

__version__ = "0.1.0"

__all__ = [
    "DistilWhisperSTT",
    "get_stt_model",
    "STTModel",
    "detect_device",
    "load_audio",
]
