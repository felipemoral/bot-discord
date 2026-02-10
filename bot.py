import discord
import os
from groq import Groq

TOKEN = os.getenv("DISCORD_TOKEN")
GROQ_KEY = os.getenv("GROQ_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
groq = Groq(api_key=GROQ_KEY)

@client.event
async def on_ready():
    print("Bot online")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!ia"):
        texto = message.content.replace("!ia", "").strip()

        if texto == "":
            await message.channel.send("Digite algo depois de !ia")
            return

        resposta = groq.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": texto}]
        )

        await message.channel.send(resposta.choices[0].message.content)

client.run(TOKEN)
