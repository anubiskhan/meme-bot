import discord
import config
import requests

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!spicyaf'):
        response = requests.get('https://www.reddit.com/r/dankmemes/random.json', headers = {'User-agent': 'Anubot - Spicy Memes'})
        resp_url = response.json()[0]['data']['children'][0]['data']['url']
        await client.send_message(message.channel, resp_url)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Unleash the meme')

client.run(config.TOKEN)
