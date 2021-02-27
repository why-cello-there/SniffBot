import discord
import os
from replit import db

from dotenv import load_dotenv
from discord.ext import commands, tasks

from keep_alive import keep_alive

from Fun import Fun
from Meta import Meta
from Server import Server

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(
    command_prefix=".",
    description="Sniff Bot is the bot for the Why Cello There server.", intents=discord.Intents.all())


@bot.event
async def on_ready():
	print("Bot is ready!")

@bot.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, id = 795609115492876298)
  await channel.send(f"Welcome to Why Cello There, <@{member.id}>! Make sure to join all of the servers in <#812269573323227176>. You can also ~~join in on the pyramid scheme and~~ write `$join @username` of the person who invited you. Have fun!")

@bot.event 
async def on_member_remove(member): 
  channel = discord.utils.get(member.guild.channels, id = 795609115492876298)
  await channel.send(f"<@{member.id}> just left! They will certainly not be missed.")

keep_alive()

bot.add_cog(Fun(bot))
bot.add_cog(Meta(bot))
bot.add_cog(Server(bot))

bot.run(TOKEN)
