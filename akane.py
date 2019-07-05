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
    await client.change_presence(game=Game(name='Apex Legends'))
    print('Ready') 


@client.event
async def on_message(message):
    if message.content == 'hi raphtalia':
        await client.send_message(message.channel,'Hello ^^')    
    if message.content == 'lurks':
        await client.send_message(message.channel,'https://cdn.discordapp.com/emojis/489171674764410941.png?v=1')
    if message.content == 'hugs Raphtalia':
        await client.send_message(message.channel,'https://cdn.discordapp.com/emojis/489171686210404363.png?v=1')
    if message.content == 'hmph':
        await client.send_message(message.channel,'https://cdn.discordapp.com/emojis/489171684465836032.png?v=1')
    if message.content == 'yesnt':
        await client.send_message(message.channel,'https://cdn.discordapp.com/emojis/489171675141898240.png?v=1')
    if message.content == 'nani?':
        await client.send_message(message.channel,'https://cdn.discordapp.com/emojis/489171675141898240.png?v=1')
    if message.content == 'bye':
        await client.send_message(message.channel,'https://cdn.discordapp.com/emojis/489171686814515223.png?v=1')
    if message.content == 'hoho':
        await client.send_message(message.channel,'https://cdn.discordapp.com/emojis/489171697694539776.png?v=1')
    if message.content == 'Ohayo':
        await client.send_message(message.channel,'OHAYOO')
    if message.content == 'u win':
        await client.send_message(message.channel,'YAASSS')
    if message.content == 'LOL':
        await client.send_message(message.channel,'XD')
    if message.content == 'I WON':
        await client.send_message(message.channel,'NUUUU!')
    if message.content == 'Akane what are u doing?':
        await client.send_message(message.channel,'Im trying to make a paperplane but i cant make it symmetrical @R3TR0 B0Y#0106 Can u help me?')
    if message.content == 'good morning':
        await client.send_message(message.channel,'GOOD MORNING')
    if message.content == 'im back':
        await client.send_message(message.channel,'Welcome back ')
    if message.content == '!Live':
        await client.send_message(message.channel,'https://www.youtube.com/channel/UCsT1iWCqFjXe5438KRTZNgw')
        em.set_image(url='https://media.discordapp.net/attachments/454724320782974986/489393181163782145/b1f25ab558ac4c7ffa15d0fada68a0b7bed6f926_hq.gif?width=486&height=273')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Raphtalia introduce yourself':
        await client.send_message(message.channel,'I am Naofumis proud sword')
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
            'Twitch',]
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
            'DustyDiner',
            'DustyDivot',
            'NeoTilted',
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
            'Crane',
            'Mexico',
            'ParadiseJunkJunction',]
        await client.send_message(message.channel,(random.choice(variable)))
    if message.content == 'ROCK':
        variable = [
            'PAPER',
            'SCISSORS',]
        await client.send_message(message.channel,(random.choice(variable)))
    if message.content == 'PAPER!':
        variable = [
            'ROCK!',
            'SCISSORS!',]
        await client.send_message(message.channel,(random.choice(variable)))
    if message.content == 'SCISSORS I CHOOSE U':
        variable = [
            'ROCK I CHOOSE U',
            'PAPER I CHOOSE U',]
        await client.send_message(message.channel,(random.choice(variable)))
    if message.content == 'Akane who is your favorite?':
        variable = [
            'Nova',
            'Teaboi',
            'Retro',
            'Shad',]
        await client.send_message(message.channel,(random.choice(variable)))


client.run(os.getenv('TOKEN'))
