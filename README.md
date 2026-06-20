# Jarvis Personal AI Assistant

A private, Windows-based voice assistant built with Python. Jarvis combines local command handling with AI-powered responses to launch apps, perform web searches, and interact using speech.

## Features

- Voice-driven assistant loop with fallback to text input
- Speech output using `pyttsx3`
- Voice recognition using `SpeechRecognition`
- Local command handling for opening/closing applications
- AI conversation for questions and general prompts
- Configurable assistant persona and model settings

## Project Structure

- `main.py` - entry point that runs the assistant loop
- `assistant.py` - handles user input and decides whether to run local commands or call AI
- `commands.py` - local command implementations like app launching, closing, search, and date/time
- `voice.py` - text-to-speech and speech-to-text utilities
- `ai_client.py` - AI model integration with Groq chat completions
- `config.py` - assistant settings, prompts, and token limits
- `apps.json` - stored application shortcuts for quick launch
- `requirements.txt` - required Python dependencies

## Requirements

- Windows OS
- Python 3.10+ recommended
- Microphone access for voice input
- Internet access for AI and speech recognition

## Installation

1. Clone or copy the repository into a local folder.
2. Create a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

> Note: `ai_client.py` expects `GROQ_API_KEY` from environment variables.

## Usage

Run the assistant from the project root:

```powershell
python main.py
```

Then speak or type commands such as:

- `open chrome`
- `launch spotify`
- `close discord`
- `search for weather`
- `what is the time`

To exit, say or type:

- `exit`
- `quit`
- `bye`

## Configuration

Customize the assistant in `config.py`:

- `ASSIST_NAME` - assistant name shown at runtime
- `USER_NAME` - your user name
- `MODEL_NAME` / API settings
- `SYSTEM_PROMPT` - AI persona and behavior instructions

## App Shortcuts

`commands.py` uses `apps.json` to store app paths. You can add or update entries manually, for example:

```json
{
  "chrome": "C:\\Users\\Ananya\\Desktop\\google docs.lnk",
  "discord": "C:\\Users\\Ananya\\Desktop\\Discord.lnk"
}
```

If an app is not found, Jarvis will prompt for a path and save it to `apps.json`.

## Notes

- This assistant is designed for experimentation and private use.
- The voice recognition fallback returns to text input if no speech is detected.
- The AI prompt is set up for a sarcastic, witty personality with friendly tone.

## GitHub Repository Setup

To push this project to a private GitHub repository, follow these steps from the project root:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<your-username>/<your-private-repo>.git
git branch -M main
git push -u origin main
```

If you already have a repo, replace the `git remote add origin ...` line with your existing remote URL.

Make sure `.gitignore` includes private and generated files before pushing.

## License

This repository is private. Use and modify the code as needed for your personal assistant setup.
