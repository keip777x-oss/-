import os
import asyncio
from dotenv import load_dotenv
import discord
from discord import app_commands

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise SystemExit("BOT_TOKEN がありません。GitHub Secrets に BOT_TOKEN を追加してください")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")
    print("Slash commands synced!")


@tree.command(
    name="spam",
    description="指定したメッセージを1〜100回送信します。"
)
async def spam(interaction: discord.Interaction, 回数: int, メッセージ: str):
    if 回数 < 1 or 回数 > 100:
        await interaction.response.send_message("回数は1〜100で指定してください！", ephemeral=True)
        return

    await interaction.response.send_message(f"{回数}回送信開始！")

    for i in range(回数):
        await interaction.channel.send(メッセージ)
        await asyncio.sleep(0.6)  # レート制限対策


client.run(TOKEN)