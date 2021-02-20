import discord
import os
from replit import db

from dotenv import load_dotenv
from discord.ext import commands, tasks

from keep_alive import keep_alive

from Fun import Fun

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=".", description="Sniff Bot is a General Purpose bot I guess\n\nAcknowledgements:\nThis bot has copied code from the following bots:\nCocánb bot\nSmetch bot")

@bot.event
async def on_ready():
    activity = discord.Game(name="IServ")
    await bot.change_presence(status=discord.Status.idle,activity=activity)
    print("Bot is ready!")

keep_alive()

bot.add_cog(Fun(bot))

bot.run(TOKEN)