import os

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OPENCLAW_API_KEY = os.getenv("OPENCLAW_API_KEY")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set. Add it to your .env file.")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


async def run_openclaw_agent(user_text: str) -> str:
    if not OPENCLAW_API_KEY:
        return "OPENCLAW_API_KEY를 .env에 넣어주세요."

    # TODO: 여기에 OpenClaw API 호출 코드를 붙이면 됩니다.
    # 지금은 기본 구조 확인용으로 임시 응답만 반환합니다.
    return f"[OpenClaw 연결 전] 받은 질문: {user_text}"


@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author.bot:
        return

    content = message.content.strip()

    if content.startswith("!ping"):
        await message.channel.send("pong")
        return

    if not content.startswith("!ask "):
        return

    user_text = content[5:].strip()

    if not user_text:
        await message.reply("질문 내용을 입력해 주세요. 예: !ask 오늘 할 일 정리해줘")
        return

    async with message.channel.typing():
        reply = await run_openclaw_agent(user_text)
        await message.reply(reply[:1900])

client.run(TOKEN)
