import os

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime

guild = 756401202434015232

class Embeds(commands.Cog):
    def  __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_guild=True)
    async def SrvRules(self, ctx):
        rulesem = discord.Embed(
            title="Welcome to UltiMod's Support Server",
            description="Please read below and verify to gain access to the support channels.",
            color=discord.Colour.gold()
        )
        rulesem.add_field(
            name="Server Rules",
            value="""The Server rules are as follows:
            > 1. No Spamming - This server is for support and any UltiMod related discussions. If you spam in any way you will be banned.
            > 
            > 2. No Advertising - This is not your personal advertisement space. Ads of any kind send or displayed in any way will result in a ban.
            > 
            > 3. Don't Ping support - Support staff are voluntary and not obligated to help. If you have a question, post it in one of the support channels, do NOT DM/PM or ping staff.
            > 
            > 4. **NO hate speech or politics** - You will be banned and/or reported to Discord.
            > 
            > 5. **NO NSFW Content** - This is not your Guys/Ladies club. Keep it to private servers.
            >  
            > 6. **NO Bad Language** - Rule of thumb is, if you wouldn't say it to your grandmother, don't say it here. Keep it civil, keep it classy.""",
            inline=False
        )
        rulesem.add_field(
            name="Check out these channels",
            value="""Please check these channels before posting any support questions. You may find your anwser in there.
            > 
            > 1. [F.A.Q. Channel](https://discord.com/channels/756401202434015232/775024006268846143) - Frequently asked questions.
            > 
            > 2. [Support Channel 1](https://discord.com/channels/756401202434015232/775023668278460426) - Check support channels for any recent questions relating to yours.
            >    [Support Channel 2](https://discord.com/channels/756401202434015232/775023699135823942)
            > 
            > 3. [Rules](https://discord.com/channels/756401202434015232/775023914748477481) - Check the rules page for more indepth explanation of rules.""",
            inline=False
        )
        rulesem.set_thumbnail(
            url = ctx.guild.icon_url
        )
        rulesem.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        rulesem.timestamp = datetime.datetime.utcnow()
        if ctx.guild.id == guild:
            await ctx.send(embed=rulesem)

def setup(bot):
    bot.add_cog(Embeds(bot))
    print("UltiMod Server extension has loaded!")
