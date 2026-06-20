# JARVIS Backlog

desktop only application

## Known Issues 

- Smart fallback: if command target not found in store,
  pass to AI instead of asking for path
  e.g. "open my favourite app" should let AI interpret intent

- open apps and do the said task
- Weather command — "what's the weather today?" fetches real weather using a free API. Very practical.
- Web search — "search for..." opens Google with that query. One line of code actually.
- System info — "what's my battery?" or "how much RAM am I using?" using Python's psutil library.
- Reminders — "remind me in 10 minutes to call mom." Uses Python's threading library to trigger after a delay.
- Clipboard control — "copy that" or "what's in my clipboard?" Very useful daily.
- Screenshot — "take a screenshot" saves it with a timestamp. One library called pyautogui.

## STAGES

- Stage 1 — Core assistant + commands
- Stage 2 — Voice output
- Stage 3 — Voice input(DONE UP TILL HERE)

- Stage 4 — GUI window interface
- Stage 5 — "Hey JARVIS" wake word
- Stage 6 — Backlog fixes + polish

Stage 1 — Complete

- Modular architecture
- Natural language command parser
- App launcher and closer
- Real AI brain (Groq + Llama)
- JARVIS personality via system prompt
- Secure API key management
- Conversation history (short term memory)

Stage 2 — Complete

- Voice output (pyttsx3)
- JARVIS speaks every response


## FINAL ADDITIONS
## Voice System Improvements

### ElevenLabs Integration
Priority: Medium

Current:
- Using pyttsx3 for offline text-to-speech
- Fast and free but sounds robotic

Planned:
- Integrate ElevenLabs API for realistic JARVIS voice
- Keep existing speak() architecture
- Replace or extend voice.py implementation

Goals:
- Natural-sounding voice
- More immersive assistant experience
- Better personality expression

Architecture:
main.py
    ↓
voice.py
    ↓
ElevenLabs API

Future Improvement:
- Support multiple voice engines
    - pyttsx3 (offline fallback)
    - ElevenLabs (high quality online mode)

Example:
VOICE_ENGINE = "elevenlabs"

Benefits:
- Human-like speech
- Better user experience
- Makes JARVIS feel more realistic

Requirements:
- ElevenLabs account
- API key in .env
- Internet connection

Status:
Not Started