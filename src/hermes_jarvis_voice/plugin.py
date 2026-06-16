"""JarvisVoicePlugin: hermes-jarvis-voice para hermes-agent."""
from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger("hermes-jarvis-voice")


class JarvisVoicePlugin:
    """Plugin standalone."""
    name = "hermes-jarvis-voice"
    kind = "standalone"
    version = "1.0.0"

    def register(self, ctx) -> None:
        """Hook de registro."""
        # Tools
        ctx.register_tool("hermes_jarvis_voice_status", self._tool_status)

        # Skills
        skill_path = self._skill_path()
        if skill_path.exists():
            ctx.register_skill("hermes-jarvis-voice", skill_path)

        log.info("hermes-jarvis-voice v%s registrado", self.version)

    def _skill_path(self) -> Path:
        return Path(__file__).parent.parent.parent / "skills" / "jarvis-voice"

    def _tool_status(self, **_):
        return {"status": "ready", "version": self.version}
