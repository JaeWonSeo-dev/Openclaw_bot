# Openclaw_bot

A minimal Discord bot scaffold that forwards user prompts to an OpenClaw-backed workflow.

## What this project does

- logs into Discord using `discord.py`
- listens for simple bot commands
- replies to `!ping`
- accepts `!ask <message>` prompts
- prepares a place to connect OpenClaw API calls
- creates `memory/YYYY-MM-DD.md` in the configured OpenClaw workspace when the bot starts for the first time that day

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
WORKSPACE_ROOT=C:\Users\wonsu\.openclaw\workspace
OPENCLAW_TIMEZONE=Asia/Seoul
```

## Run

```bash
python main.py
```

## Commands

- `!ping` → replies with `pong`
- `!ask <message>` → sends the message to the OpenClaw handler stub

## Daily memory file behavior

On startup, the bot creates the following file if it does not already exist for the current day:

```text
<WORKSPACE_ROOT>/memory/YYYY-MM-DD.md
```

By default:

- `WORKSPACE_ROOT` = `C:\Users\wonsu\.openclaw\workspace`
- `OPENCLAW_TIMEZONE` = `Asia/Seoul`

If the file already exists, it is left unchanged.

## Security note

Real secrets must stay only in `.env` and are ignored by Git. Only `.env.example` should be committed.
