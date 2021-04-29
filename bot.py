import discord
from discord.ext import commands
import random 
import requests
import pprint


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
    

#commands bot will do something
@client.command()

#this command will tell us the ping of the bot called with ".ping"
async def ping(ctx):
    await ctx.send(f'ping in ms: {round(client.latency * 1000)}ms ')

#this command lets you roll and 8 ball and ask a question called with ".8ball YOUR QUESTION"
@client.command(aliases=['8ball','8Ball'])
async def _8Ball(ctx,*,question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#this command can be used to clear an amount of messages that is passed in
@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

#this will clear all of the messages in a channel
@client.command()
async def clearAll(ctx):
    await ctx.channel.purge()

#this command takes a zip code input and returns a list of breweries inside that zipcode

@client.command()

async def beer(ctx,*,zipcode):
    r = requests.get(f'https://api.openbrewerydb.org/breweries?by_postal={zipcode}')
    i = 0
    if(len(r.json()) == 0):
        await ctx.send("ERROR: No breweries found make sure postal code is right")
    while (i < len(r.json())):
        await ctx.send(f"Brewery: {r.json()[i]['name']}")
        await ctx.send(f"Street Adress: {r.json()[i]['street']}")
        await ctx.send(f"Website: {r.json()[i]['website_url']}")
        i = i+1
 

client.run('ODM3MTYyNjc3NDE0OTIwMjEy.YIoigA.nNMQBIco_yyKI5_P4awg93OULdM') #I accidentally committed  this one time but it has since been reset :)
