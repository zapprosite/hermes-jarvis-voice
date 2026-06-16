"""Smoke tests para hermes-jarvis-voice."""
import pytest
import subprocess
import sys


def test_python_version():
    """Python 3.11+ required."""
    assert sys.version_info >= (3, 11), "Python 3.11+ required"


def test_hermes_agent_installed():
    """hermes-agent >= 0.16.0 deve estar instalado."""
    result = subprocess.run(
        ["pip", "show", "hermes-agent"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, "hermes-agent nao instalado"


def test_plugin_imports():
    """Plugin VoicePlugin deve ser importavel."""
    try:
        from jarvis_voice.plugin import VoicePlugin
        plugin = VoicePlugin()
        assert plugin.name == "jarvis-voice"
        assert plugin.version == "1.0.0"
        assert plugin.kind == "standalone"
    except ImportError:
        pytest.skip("jarvis_voice nao instalado")


def test_config_loads():
    """VoiceConfig deve carregar com defaults."""
    try:
        from jarvis_voice.config import VoiceConfig
        cfg = VoiceConfig()
        assert cfg.oww_threshold == 0.5
        assert cfg.stt_model == "large-v3-turbo"
        assert cfg.tts_voice == "jarvis-clone-trimmed"
    except ImportError:
        pytest.skip("jarvis_voice nao instalado")
