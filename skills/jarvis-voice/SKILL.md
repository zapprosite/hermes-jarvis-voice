---
name: jarvis-voice
description: |
  Voice stack (wake + STT + LLM + TTS) em português brasileiro.
  Persona "Jarvis" estilo Tony Stark ("Senhor", 1-3 frases curtas, sem bajular).
  Voice clonada (jarvis-clone-trimmed), GPU-only, fail-closed CPU.
---

# Jarvis Voice

Voice stack em PT-BR com:
- **Wake**: OWW CUDA + jarvis_ptbr_user (custom trained)
- **STT**: faster-whisper large-v3-turbo (float16)
- **LLM**: T1 (Qwen 4B local) + T2 (cloud) + HEDGE parallel
- **TTS**: OmniVoice + jarvis-clone-trimmed (sub-sentence 8-15 palavras)
- **Telemetria**: voice-telemetry service (port 4140, 11 checks)

## Comandos

- `jarvis-voice-bootstrap` — setup idempotente
- `jarvis-voice-smoke` — validar (11/11 checks)
- `jarvis-voice-status` — status do runtime

## Variáveis de ambiente (em ~/.hermes/.env)

Ver [docs/CONFIG.md](docs/CONFIG.md).

## Referencias

- `references/voice-stack-overview.md`
- `references/wake-model-customization.md`
- `references/llm-tier-routing.md`
- `references/tts-streaming-sub-sentences.md`
- `references/voice-telemetry-sre.md`
- `references/troubleshooting.md`
