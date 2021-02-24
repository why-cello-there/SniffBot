import discord
import os
from replit import db

from dotenv import load_dotenv
from discord.ext import commands, tasks

from keep_alive import keep_alive

from Fun import Fun
from Meta import Meta
from Moderation import Moderation
from Server import Server

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(
    command_prefix=".",
    description="Sniff Bot is the bot for the Why Cello There server.")


@bot.event
async def on_ready():
	activity = discord.Game(name="IServ")
	await bot.change_presence(status=discord.Status.online, activity=activity)
	print("Bot is ready!")

@bot.event
async def on_member_join(member):
  pass


keep_alive()

bot.add_cog(Fun(bot))
bot.add_cog(Meta(bot))
bot.add_cog(Moderation(bot))
bot.add_cog(Server(bot))

bot.run(TOKEN)
