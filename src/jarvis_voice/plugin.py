"""VoicePlugin: Jarvis voice stack como plugin hermes-agent."""
from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger("jarvis_voice")


class VoicePlugin:
    """Plugin standalone que adiciona voice stack ao hermes-agent."""
    name = "jarvis-voice"
    kind = "standalone"
    version = "1.0.0"
    config_class = "jarvis_voice.config:VoiceConfig"

    def register(self, ctx) -> None:
        """Hook de registro. Chamado pelo hermes-agent no startup."""
        # Tools
        ctx.register_tool("voice_status", self._tool_voice_status)
        ctx.register_tool("voice_calibrate", self._tool_calibrate)
        ctx.register_tool("voice_toggle", self._tool_toggle)

        # Skills
        skill_path = self._skill_path()
        if skill_path.exists():
            ctx.register_skill("jarvis-voice", skill_path)

        # Hooks
        ctx.register_hook("pre_session", self._on_pre_session)
        ctx.register_hook("post_session", self._on_post_session)

        log.info("jarvis-voice v%s registrado", self.version)

    def _skill_path(self) -> Path:
        return Path(__file__).parent.parent.parent / "skills" / "jarvis-voice"

    def _tool_voice_status(self, **_):
        return {"status": "ready", "version": self.version}

    def _tool_calibrate(self, **_):
        return {"status": "calibration_started", "duration_s": 5}

    def _tool_toggle(self, action: str, **_):
        return {"status": f"toggled_{action}"}

    def _on_pre_session(self, **_):
        log.info("voice: pre-session")

    def _on_post_session(self, **_):
        log.info("voice: post-session")
