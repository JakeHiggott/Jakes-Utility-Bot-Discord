import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('INSERT YOUR BOT CER HERE') #MAKE SURE YOU DO NOT COMMIT YOUR CER

