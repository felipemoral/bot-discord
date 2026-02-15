import discord
from discord.ext import commands
import os

# 1️⃣ Criar intents
intents = discord.Intents.default()
intents.message_content = True

# 2️⃣ Criar o bot
bot = commands.Bot(command_prefix="!", intents=intents)

# 3️⃣ Eventos
@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

# 4️⃣ Comandos
@bot.command()
async def itens(ctx):
    await ctx.send("FUNCIONANDO ✅")

# 5️⃣ Rodar o bot
bot.run(os.getenv("MTQ2OTA5MDA5OTE5Mzk3NDk2NQ.GJ9Qoa.vF9qHXIkq0UDXKNi5PZsBWTK01AHGcNyn53Lhc
"))
