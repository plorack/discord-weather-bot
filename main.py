#!/home/test/virtualenv/nextcord/bin/python3
###############################################
#  ____              ____    /\/|  /\/|  /\/| #
# | __ ) _____ _____|  _ \  |/\/  |/\/  |/\/  #
# |  _ \|_____|_____| | | |                   #
# | |_) |_____|_____| |_| |                   #
# |____/            |____/                    #
#                                             #
###############################################
# BASIC SKELETON FOR A DISCORD BOT @ main.py  #
###############################################

# 1. IMPORTING LIBRARIES ##################################################
# nextcord -> methods to interact with Discord API
# config -> hosting api keys
import nextcord 
from nextcord.ext import commands # Used for bot interactions
from nextcord import Interaction, SlashOption # Used for UI slashcommands
from config import * # hosting our various keys
import asyncio

# 2. LOADING BOT KEYS #####################################################
api_key = api_key_weather
discord_key = api_key_discord

# 3. PREFIX COMMANDS ######################################################
# Preffix commands are used directly in the chat bar to ask
# the bot to perform certain actions in this case -> ! <- will
# be pick up by the bot which will run the code associated with a
# defined prefix.
client = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

# 4. BOT CONNECTION STATUS ################################################
# ON SUCCESSFULL CONNECTION - THESE ARE COMMANDS PERFORMED BY THE BOT
@client.event
async def on_ready():
    #Prints to linux console
    print("Success: Bot is connected to Discord")
    #Displays status on discord channel
    activity = nextcord.Activity(type= 1, name="a dangerous game")
    await client.change_presence(status=nextcord.Status.online, activity=activity)

#5. SAMPLE PREFIX COMMANDS ################################################
## 5.1 Connection latency in milli seconds
@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)  # Convert to milliseconds
    await ctx.send(f"Bot latency: {latency} ms")

# Running main event loop
async def main():
    client.load_extension('cogs.90_weather')
    await client.start(discord_key)

asyncio.run(main())