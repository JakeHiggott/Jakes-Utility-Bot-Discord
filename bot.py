import discord
from discord.ext import commands
import random 

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



client.run('YOUR CER HERE') #I accidentally committed  this one time but it has since been reset :)

