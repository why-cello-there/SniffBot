import discord
from discord.ext import commands

class Meta(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ack", help="Tells you what code this bot stole code from")
  async def ack(self, ctx):
    await ctx.send("**Acknowledgements**\nThis bot uses `discord.py` and `discord.ext` and was made on repl.it. It 'stole' code from the following repositories:\nhttps://github.com/cocanb-altort/cocanb-bot\nhttps://github.com/smetch-discord/smetch-bot")

  @commands.command(name="github", help="This command will send the link of the GitHub repository of this bot")
  async def github(self, ctx):
    await ctx.send("https://github.com/ichbinderwooj/SniffBot")