import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests
import json  
import random 

load_dotenv()
client = discord.Client()
bot = commands.Bot(command_prefix="$", case_insensitive=True)

monkey_words = ['mandrill', 'golden snub-nosed monkey', 'panamanian white-faced capuchin',
                'rhesus macaque', 'proboscis monkey', 'emperor tamarin', 'lion-tailed macaque',
                'japanese macaque', 'colombian white-faced capuchin', 'crab-eating macaque', 
                'vervet monkey', 'common marmoset', 'guinea baboon', 'golden lion tamarin',
                'bonnet macaque', 'golden monkey', 'bald uakari', 'common squirrel monkey', 
                'hamadryas baboon', 'white-faced saki', 'northern plains gray langur', 
                'popa langur', 'dusky leaf monkey', 'formosan rock macaque', 'green monkey',
                'black howler', 'colombian red howler', 'mantled guereza', 'chacma baboon',
                'southern pig-tailed macaque', 'black-handed spider monkey', 'black snub-nosed monkey',
                'red-faced spider monkey', 'drill', 'de brazzas monkey', 'yellow baboon', 'celebes crested macaque',
                'gelada', 'east javan langur', 'barbary macaque', 'myanmar snub-nosed monkey', 'black-crested sumatran langur',
                'cotton-top tamarin', 'central american squirrel monkey', 'red-shanked douc', 'kinda baboon', 
                'maroon leaf monkey', 'tufted capuchin', 'olive baboon', 'grivet', 'gees golden langur']

def get_monkey():
    return random.choice(monkey_words)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(int(os.getenv('CHANNEL')))
    await channel.send('welcome to monkey bot! heres a list of commands: \n $hello \n $monkey \n $song')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH OUGH 🦍 OUGH 🦍 OUGH!')

    if message.content.startswith('$monkey'):
        await message.channel.send(get_monkey())
    
    if message.content.startswith('$song'):
        await message.channel.send('here is your monkey song: https://open.spotify.com/track/2aV6fJYHSZeQ4sTGusPLE4?si=6d29c89c28474176')


client.run(os.getenv('TOKEN'))
bot.run(os.getenv('TOKEN'))

