"""VoiceConfig: Pydantic settings para jarvis-voice."""
from __future__ import annotations

from pathlib import Path
from pydantic import BaseSettings, Field, HttpUrl


class VoiceConfig(BaseSettings):
    """Config do jarvis-voice, lido de ~/.hermes/.env."""

    oww_model_path: Path = Field(
        default=Path("/usr/local/share/hermes-jarvis-voice/models/jarvis_ptbr_user.onnx"),
    )
    oww_threshold: float = 0.5
    oww_provider: str = "CUDAExecutionProvider"

    stt_model: str = "large-v3-turbo"
    stt_device: str = "cuda"
    stt_compute_type: str = "float16"
    stt_language: str = "pt"

    tts_base_url: HttpUrl = "http://127.0.0.1:8202/v1/audio/speech"
    tts_voice: str = "jarvis-clone-trimmed"

    llm_t1_base_url: HttpUrl = "http://127.0.0.1:8001/v1"
    llm_t2_base_url: HttpUrl = "https://api.minimax.io/anthropic/v1"

    telemetry_enabled: bool = True
    telemetry_port: int = 4140
    telemetry_bind: str = "127.0.0.1"

    cb_enabled: bool = True
    cb_threshold_fails: int = 3
    cb_window_s: int = 60
