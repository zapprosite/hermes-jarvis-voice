# hermes-jarvis-voice

**Voice stack para hermes-agent v0.16+** — wake word + STT + LLM + TTS + voice telemetry.

## Dependencias cross-repo

Este modulo **nao funciona sozinho**. Requer:

- **[hermes-jarvis-voice-clone](https://github.com/zapprosite/hermes-jarvis-voice-clone)** — Modelos de voz do Will (wake ONNX + TTS voice)
- **[hermes-omnivoice-tts](https://github.com/zapprosite/hermes-omnivoice-tts)** — Engine TTS (HTTP client)
- **[hermes-voice-telemetry](https://github.com/zapprosite/hermes-voice-telemetry)** — Service de telemetria (FastAPI, port 4140)
- **[hermes-voice-stream](https://github.com/zapprosite/hermes-voice-stream)** — Audio capture + VAD + PipeWire
- **[hermes-llm-routing](https://github.com/zapprosite/hermes-llm-routing)** — T1/T2/HEDGE routing
- **[hermes-memory-stack](https://github.com/zapprosite/hermes-memory-stack)** — Memory providers (Honcho + Qdrant + pgvector)

## Quick start (3 comandos)

```bash
pip install hermes-jarvis-voice
jarvis-voice-bootstrap
jarvis-voice-smoke
```

## Status

- voice-telemetry service (port 4140, 11/11 checks)
- OWW CUDA + jarvis_ptbr_user (PT-BR)
- faster-whisper CUDA (large-v3-turbo, float16)
- OmniVoice TTS (jarvis-clone-trimmed, sub-sentence streaming)
- LLM routing T1/T2/HEDGE
- Circuit breaker + Prometheus metrics

## Install

```bash
pip install hermes-jarvis-voice[voice]
jarvis-voice-bootstrap  # systemd + .env + wake model
jarvis-voice-smoke     # 11/11 checks
```

## E2E flow

```
Wake (OWW) -> STT (Whisper) -> LLM (T1/T2/HEDGE) -> TTS (OmniVoice) -> Playback -> Telemetry
```

## Compatibilidade

- Python 3.11+
- Ubuntu 22.04+ (ou similar)
- NVIDIA RTX 3060+ 12GB VRAM
- hermes-agent >= 0.16.0
