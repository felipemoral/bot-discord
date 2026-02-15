import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

@bot.command()
async def itens(ctx):
    await ctx.send("FUNCIONANDO ✅")

print("TOKEN:", os.getenv("TOKEN"))


bot.run(os.getenv("MTQ2OTA5MDA5OTE5Mzk3NDk2NQ.GJ9Qoa.vF9qHXIkq0UDXKNi5PZsBWTK01AHGcNyn53Lhc
"))
