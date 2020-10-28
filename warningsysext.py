# Warning system extension
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sqlite3 

class warningsext(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @warningsext.command()
    @has_permissions(manage_guild=True)
    async def warn(self, ctx, user: discord.Member, reason="No reason provided"):
        if reason != None and user != self.bot:
            warnembed = discord.Embed(
                title="A User has been warned!",
                color=15844367
            )
            warnembed.add_field(
                name="Offender:",
                value=user.mention,
                inline=False
            )
            warnembed.add_field(
                name="Reason:",
                value=reason,
                inline=False
            )
            warnembed.add_field(
                name="Responsible Moderator:",
                value=ctx.author.mention,
                inline=False
            )
            warnembed.set_thumbnail(
                url= user.avatar_url
            )
            await ctx.send(embed=warnembed) #will be changed to channel.send when modlog is set. 
            await ctx.send(f":ok_hand: {user} has been warned.")
        
        elif user != discord.Member:
            await ctx.send("__**ERROR:**__ Can't find that user. Please double check and try again. Usage: `?warn @user <reason>`")
        
        elif user == self.bot:
            await ctx.send("Hey! Don't bite the hand that feeds you.")
        
    @warningsext.command()
    @has_permissions(manage_guild=True)
    async def warnings(self, ctx, user: discord.Member):
        warningsembed = discord.Embed(
            title=f"Warnings for {user}",
            description="Current: \n ```()```",
            color=15844367
        )
        warningsembed.set_thumbnail(
            url = user.avatar_url
        )
        await ctx.send(embed=warningsembed)

    def setup(bot):
        bot.add_cog(warningsext(bot))
        print("Warnings Extension has been loaded.")
