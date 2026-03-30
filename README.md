# Openclaw_bot

A minimal Discord bot scaffold that forwards user prompts to an OpenClaw-backed workflow.

## What this project does

- logs into Discord using `discord.py`
- listens for simple bot commands
- replies to `!ping`
- accepts `!ask <message>` prompts
- prepares a place to connect OpenClaw API calls

At the moment, the OpenClaw call is still a stub in `main.py`, so this repository is best understood as a starter integration project.

## Files

- `main.py` — bot entry point
- `.env.example` — example environment variables
- `requirements.txt` — Python dependencies

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file from `.env.example` and fill in real values:

```env
DISCORD_TOKEN=your-discord-bot-token
OPENCLAW_API_KEY=your-openclaw-api-key
```

## Run

```bash
python main.py
```

## Commands

- `!ping` → replies with `pong`
- `!ask <message>` → sends the message to the OpenClaw handler stub

## Security note

Real secrets must stay only in `.env` and are ignored by Git. Only `.env.example` should be committed.
