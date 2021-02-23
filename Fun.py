import discord
from discord.ext import commands

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="null", help="")
  async def null(self, ctx):
    await ctx.send("** **")

  @commands.command(name="barry", help="Putain!!!!")
  async def barry(self, ctx):
    await ctx.send("<:barry:810819195050131466>")

  @commands.command(name="echo", help="returns argument")
  async def echo(self, ctx, *, args):
    await ctx.send(args)

  @commands.command(name="delecho", help="returns argument")
  async def delecho(self, ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args)