import discord
from discord import guild
from discord.ext import commands 
import random
import os

import youtube_dl

#bot command starts with '.'
client = commands.Bot(command_prefix='.')

#on ready
@client.event
async def on_ready():
    print('Bot is ready')

#member joins server
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

#member left server
@client.event 
async def on_member_remove(member):
    print(f'{member} has left a server.')

#bot sends its latency
@client.command()
async def ping(context):
    await context.send(f'{round(client.latency * 1000)}ms')

#bot rolls a die in NdN format
@client.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

#bot chooses options for users
@client.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

#bot sends a picture of racoon
@client.command()
async def racoon(ctx):
    await ctx.send('Racoon man is protecting you!', file=discord.File('Desktop/racoon/racoon.jpg'))


# @client.command()
# async def play(ctx, url: str):
#     song_there = os.path.isfile('song.mp3')
#     try:
#         if song_there:
#             os.remove('song.mp3')
#     except PermissionError:
#         await ctx.send("Wait for the current playing music to end or use the 'stop' command")
#         return

         
#     voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='추노')
#     await voiceChannel.connect()
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)


#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
#         'restrictfilenames': True,
#         'noplaylist': True,
#         'nocheckcertificate': True,
#         'ignoreerrors': False,
#         'logtostderr': False,
#         'quiet': True,
#         'no_warnings': True,
#         'default_search': 'auto',
#         'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
#     }

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#     for file in os.listdir("./"):
#         if file.endswith('.mp3'):
#             os.rename(file, 'song.mp3')
#     voice.play(discord.FFmpegPCMAudio('song.mp3'))


# @client.command()
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     if voice.is_connected():
#         await voice.disconnect()
#     else:
#         await ctx.send("Racoon man stopped the music for you!")

# @client.command()
# async def pause(ctx):
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send('STOP!')

# @client.command()
# async def resume(ctx):
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     if voice.is_paused():
#         voice.resumem()
#     else:
#         await ctx.send('PLAY!')

# @client.command()
# async def stop(ctx):
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     voice.stop()


client.run('TOKEN')