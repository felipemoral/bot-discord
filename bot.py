import os
import discord
from discord.ext import commands
import requests

@bot.event
async def on_message(message):
    print(message.content)
    await bot.process_commands(message)


TOKEN = os.getenv("DISCORD_TOKEN")
API_URL = "https://metaforge.app/api/arc-raiders/items"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


items_cache = []

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")
    try:
        r = requests.get(API_URL)
        global items_cache
        items_cache = r.json()
        print("Itens carregados!")
    except:
        print("Erro ao carregar itens.")

@bot.command()
async def itens(ctx):
    await ctx.send("Comando funcionando ✅")

    if not items_cache:
        return await ctx.send("Erro ao carregar itens.")
    
    mensagem = "📦 Lista de Itens:\n"
    for item in items_cache[:20]:
        mensagem += f"- {item.get('name')} ({item.get('rarity')})\n"
    
    await ctx.send(mensagem)

bot.run(TOKEN)
