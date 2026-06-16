#!/usr/bin/env bash
# jarvis-voice-bootstrap — setup idempotente

set -e

HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
SERVICE_NAME="voice-telemetry.service"

echo "=== jarvis-voice-bootstrap v1.0.0 ==="

# 1. Setup systemd
mkdir -p "$HERMES_HOME"
mkdir -p "$HOME/.config/systemd/user/"
cp systemd/user/voice-telemetry.service "$HOME/.config/systemd/user/" 2>/dev/null || true
systemctl --user daemon-reload

# 2. Habilitar service
if [ -f "$HOME/.config/systemd/user/voice-telemetry.service" ]; then
  systemctl --user enable "$SERVICE_NAME" 2>/dev/null || true
  systemctl --user restart "$SERVICE_NAME" 2>/dev/null || true
fi

# 3. Wake model
if [ ! -f "${JARVIS_OWW_MODEL_PATH:-/usr/local/share/hermes-jarvis-voice/models/jarvis_ptbr_user.onnx}" ]; then
  echo "  ! Wake model não encontrado, download necessário"
  echo "    curl -L <url> -o \${JARVIS_OWW_MODEL_PATH}"
fi

# 4. Validar
echo "=== Setup completo. Rodar smoke test: ==="
echo "  ~/.hermes/scripts/jarvis-voice-smoke"
