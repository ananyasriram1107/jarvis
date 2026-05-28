# JARVIS Backlog

## Known Issues

- get_target() picks up random words between keyword and app name
  e.g. "open fatass chrome" → looks for "fatass chrome"
  Fix: take last word after keyword, or use NLP library later
- Smart fallback: if command target not found in store,
  pass to AI instead of asking for path
  e.g. "open my favourite app" should let AI interpret intent

## Future Features

- Real Claude API integration
- Persistent app store (save new apps between sessions)
- Voice output (pyttsx3)
- Persistent app store (save new apps between sessions)
- Fuzzy app name matching
- Context tracking for pronouns
- Voice input (speech_recognition)

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

## Cool new features:

Weather command — "what's the weather today?" fetches real weather using a free API. Very practical.
Web search — "search for..." opens Google with that query. One line of code actually.
System info — "what's my battery?" or "how much RAM am I using?" using Python's psutil library.
Reminders — "remind me in 10 minutes to call mom." Uses Python's threading library to trigger after a delay.
Clipboard control — "copy that" or "what's in my clipboard?" Very useful daily.
Screenshot — "take a screenshot" saves it with a timestamp. One library called pyautogui.
Jokes/fun mode — already partially there with your personality but you could add a dedicated joke command.

## Visual polish:

Colored terminal output — JARVIS responses in one color, your input in another. Library called colorama. Makes the terminal look much more premium.
Typing animation — instead of printing instantly, print character by character like a real terminal. Very cinematic.
GUI — full window with chat bubbles, JARVIS logo, animations.
