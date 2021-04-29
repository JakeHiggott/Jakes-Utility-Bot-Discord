import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

#Anytime the bot sees that someone has joined a server it is connected to it will announce that they have joined
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

#Anytime someone leaves or joins the server it will say it.
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

client.run('BOT TOKEN HERE') #MAKE SURE YOU DO NOT COMMIT YOUR CER

