import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot is Online")
    print("Name: {}".forma(client.user.name))
    print("ID: {}".format (client.user.id))

@client.command(pass_context=True)
async def ping (ctx):
    await client.say ("pong!")

@client.command(pass_context=True)
async def makers (ctx):
    await client.say ("spyke1304#4487 , thundercloud130#7549")

@client.command(pass_context=True)
async def dawnload (ctx):
    await client.say ("https://discordapp.com/api/oauth2/authorize?client_id=437169657103908870&permissions=8&scope=bot")

@client.command(pass_context=True)
async def support (ctx):
    await client.say ("https://discord.gg/rA87P5q")

@client.command(pass_context=True)
async def commands (ctx):
    await client.say ("!ping krijg een woordje terug")
    await client.say ("!maker krijg de maker van deze bot")
    await client.say ("!dawnload krijg de dawnload link van deze bot")
    await client.say ("!support krijg de discord voor support van deze bot")
    await client.say ("!informatie informatie over de bot")

@client.command(pass_context=True)
async def informatie (ctx):
    await client.say ("Gebruikers: 2")
    await client.say ("Versie: 1.0")
    await client.say ("Datum laaste update: 21-4-2018")
    await client.say ("Als er een update komt staat het in onze discord")
    await client.say ("Dit is de gratis versie")
    
@client.command(pass_context=True)
async def top5games (ctx):
    await client.say ("1.Fortnite")
    await client.say ("2.Minecraft")
    await client.say ("3.Rocket League")
    await client.say ("4.Fifa 18")
    await client.say ("5.Call of Duty: Black Ops 3")
    await client.say ("LET op: Word elke maand geüpdatete")
    

client.run("NDM3MTY5NjU3MTAzOTA4ODcw.DbyQ4A.E76kZ4QxbxAfDVXkt9Gc_yLLtE4")
