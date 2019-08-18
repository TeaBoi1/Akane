import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Esports'))
    print('Ready') 


@client.event
async def on_message(message):
    if message.content == 'hi:
        await client.send_message(message.channel,'Hello')
    if message.content == '!Live':
        await client.send_message(message.channel,'https://www.youtube.com/channel/UCFJsbAeFDM-zPsb1AlqIq8w')
    if message.content == 'attackerplz':
        variable = [
            'Maverick',
            'Dokkaebi',
            'Zofia',
            'Lion',
            'Hibana',
            'Jackal',
            'Finka',
            'Thatcher',
            'Blackbeard',
            'Ying',
            'Buck',
            'Ash',
            'IQ',
            'Fuze',
            'Capitao',
            'Blitz',
            'Glaz',
            'Sledge',
            'Montagne',
            'Thermite',
            'Twitch',
            'Nokk',]
        await client.send_message(message.channel,(random.choice(variable)))
    if message.content == 'defenderplz':
        variable = [
            'Clash',
            'Ela',
            'Vigil',
            'Caviera',
            'Tachanka',
            'Frost',
            'Lesion',
            'Echo',
            'Maestro',
            'Jager',
            'Valkyrie',
            'Kapkan',
            'Smoke',
            'Mute',
            'Mira',
            'Alibi',
            'Bandit',
            'Rook',
            'Doc',
            'Castle',
            'Pulse',]
        await client.send_message(message.channel,(random.choice(variable)))
    if message.content == 'landingspotplz':
        variable = [
            'JunkJunction',
            'BLOCK',
            'HauntedHills',
            'PleasantPark',
            'LazyLagoon',
            'Volcano',
            'SunnySteps',
            'LonelyLodge',
            'LootLake',
            'Dusty',
            'Tilted',
            'SoccerField',
            'Snobby',
            'VikingMountain',
            'ShiftyShafts',
            'FatalFields',
            'LuckyLanding',
            'FrostyFlight',
            'MegaMall',
            'Factory',
            'RaceTrack',
            'ParadisePalms',
            'Mexico',
            'ParadiseJunkJunction',]
        await client.send_message(message.channel,(random.choice(variable)))


client.run(os.getenv('TOKEN'))
