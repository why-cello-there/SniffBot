import discord
import os
from replit import db

from dotenv import load_dotenv
from discord.ext import commands, tasks

from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=".", description="Sniff Bot is a General Purpose bot I guess")

@bot.command(name="null", help="")
async def null(ctx):
  await ctx.send("** **")

keep_alive()

bot.run(TOKEN)