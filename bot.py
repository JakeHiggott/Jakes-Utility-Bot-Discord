import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

#check the documentation: But below is how you detect the different events that occur in servers

#Anytime the bot sees that someone has joined a server it is connected to it will announce that they have joined
@client.event
#any event you could ever need is in the documentation.
async def on_member_join(member):
    print(f'{member} has joined a server.')

#Anytime someone leaves or joins the server it will say it.
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


client.run('INSERT TOKEN HERE') #I accidentally committed  this one time but it has since been reset :)

