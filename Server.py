import discord
from discord.ext import commands

class Server(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="rules", help="Tells you the server rules")
  async def rules(self, ctx):
    await ctx.send("**Read the rules here:** https://discord.com/channels/723430338470084648/812267276136611842/812289948999745586")

  @commands.command(name="server", help="Gets the WCT invite link")
  async def server(self, ctx):
    await ctx.send("https://discord.gg/Tayz2DWE2D")