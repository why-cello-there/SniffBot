import discord
from discord.ext import commands

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="null", help="")
  async def null(ctx):
    await ctx.send(chr(0))

  @commands.command(name="barry", help="Putain!!!!")
  async def barry(ctx):
    await ctx.send("<:barry:810819195050131466>")