import discord
from discord.ext import commands

class Server(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="rules", help="Tells you the server rules")
  async def rules(self, ctx):
    await ctx.send("__**Rules**__\n**1. Communication with other members**\n     a. Please be civil to your servermates and do not offend or disturb them. If you are swearing, please use ||spoiler markdown||\n     b. NSFW is strictly forbidden\n     c. Advertisements are only permitted in #advertisements\n**2. Use of channels**\n     a. Spam is only permitted in #spam\n     b. General bot use is only permitted in #bot\n         i. The use of @Cocánb bot#3570 and @TeXit#0796 is permitted everywhere\n          ii. The use of @Chess#6768 is permitted in #chess \n     c. Please restrain yourself from going off-topic\n**3. Punishments**\n     a. Punishments will be given as the following:\n          1. warn\n          2. mute for 1 hour\n          3. kick\n          4. ban for 1 day\n          5. permanent ban\n          if you are staff, you will be 1. warned and 2. demoted first.\n     b. You may appeal your punishment\n**4. Other**\n     a. The rules are subject to change\n     b. The abuse of your staff position is not permitted")

  @commands.command(name="server", help="Gets the WCT invite link")
  async def server(self, ctx):
    await ctx.send("https://discord.gg/Tayz2DWE2D")