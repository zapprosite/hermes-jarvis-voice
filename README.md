# hermes-jarvis-voice

**Voice stack para hermes-agent v0.16+** — wake word + STT + LLM + TTS + voice telemetry.

## TL;DR — 3 comandos

\`\`\`bash
pip install hermes-jarvis-voice
jarvis-voice-bootstrap
jarvis-voice-smoke
\`\`\`

## Status

- ✅ voice-telemetry service (port 4140, 11/11 checks)
- ✅ OWW CUDA + jarvis_ptbr_user (PT-BR)
- ✅ faster-whisper CUDA (large-v3-turbo, float16)
- ✅ OmniVoice TTS (jarvis-clone-trimmed, sub-sentence streaming)
- ✅ LLM routing T1/T2/HEDGE
- ✅ Circuit breaker + Prometheus metrics

## Install

\`\`\`bash
pip install hermes-jarvis-voice[voice]
jarvis-voice-bootstrap  # systemd + .env + wake model
jarvis-voice-smoke     # 11/11 checks
\`\`\`

## E2E flow

\`\`\`
Wake (OWW) → STT (Whisper) → LLM (T1/T2/HEDGE) → TTS (OmniVoice) → Playback → Telemetry
\`\`\`

Ver [docs/E2E_TEST.md](docs/E2E_TEST.md) para suite completa de testes.

## Compatibilidade

- Python 3.11+
- Ubuntu 22.04+ (ou similar)
- NVIDIA RTX 3060+ 12GB VRAM
- hermes-agent >= 0.16.0
