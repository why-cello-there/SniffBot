import discord
import os
from replit import db

from dotenv import load_dotenv
from discord.ext import commands, tasks

from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=".", description="Sniff Bot is a General Purpose bot I guess")

@bot.event
async def on_ready():
    activity = discord.Game(name="IServ")
    await bot.change_presence(status=discord.Status.idle,activity=activity)
    print("Bot is ready!")

@bot.command(name="null", help="")
async def null(ctx):
  await ctx.send(chr(0))

@bot.command(name="barry", help="Putain!!!!"):
async def barry(ctx):
  await ctx.send(<barry:812315535676932127>)

keep_alive()

bot.run(TOKEN)