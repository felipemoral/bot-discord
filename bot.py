import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")

async def load_cogs():
    await bot.load_extension("cogs.rpg")

@bot.event
async def setup_hook():
    await load_cogs()

bot.run(os.getenv("TOKEN"))
