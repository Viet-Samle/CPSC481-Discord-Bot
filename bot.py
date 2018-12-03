import discord
import requests
import shutil

TOKEN = 'NTE4MTgyNjczODE5MzY5NDcz.DuNC_Q.0eLSTaUZNCQQf3lCU9zKVSFjHPM'

client = discord.Client()

@client.event
async def on_message(message):
    # The bot won't respond to itself
    if message.author == client.user:
        return
    
    if message.content.startswith('!hi'):
        await client.send_message(message.channel, 'Hello')
    
    if message.content.startswith('!id'):
        # Fetching URL
        attachment = message.attachments[0]
        url = attachment['url']
        # Downloading image from url
        # Should be in the same folder as the script
        image = requests.get(url, stream = True)
        with open('dog.jpeg', 'wb') as out:
            shutil.copyfileobj(image.raw, out)
        print('Downloaded Image')
    
@client.event
async def on_ready():
    print('Logged in')

client.run(TOKEN)