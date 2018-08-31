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
        await grab_post(message, 'dankmemes')
    elif message.content.startswith('!pupaf'):
        await grab_post(message, 'rarepuppers')
    elif message.content.startswith('!meowaf'):
        await grab_post(message, 'catpictures')
    elif message.content.startswith('!loudaf'):
        await grab_post(message, 'listentothis')
    elif message.content.startswith('!helpaf'):
        'Commands: !spicyaf (memes), !pupaf (puppers), !meowaf (kitties), !loudaf (musika)'
        await client.send_message(message.channel, msg)

async def grab_post(message, subreddit_string):
    url = f'https://www.reddit.com/r/{subreddit_string}/random.json'
    response = requests.get(url, headers = {'User-agent': 'Anubot - Spicy Memes'})
    resp_url = response.json()[0]['data']['children'][0]['data']['url']
    await client.send_message(message.channel, resp_url)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Unleash the meme')

client.run(config.TOKEN)
