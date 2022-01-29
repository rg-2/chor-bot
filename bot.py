import discord
import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()

client = discord.Client()

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = f"{json_data[0]['q']}\r\n -{json_data[0]['a']}"
    return quote

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author.mention}!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(f'Hi {message.author.mention}, here is your inspiration:\r\n{quote}')

client.run(os.getenv('TOKEN'))
