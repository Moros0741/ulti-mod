import os

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sqlite3
import datetime

class welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT joinlogs FROM guild_config WHERE guild_id = ?", (member.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        welcome_embed = discord.Embed(
            title="User has joined!",
            color=discord.Color.greyple()
        )
        welcome_embed.set_author(
            name=member,
            icon_url=member.avatar_url
        )
        welcome_embed.timestamp = datetime.datetime.utcnow()
        welcome_embed.set_thumbnail(
            url=member.avatar_url
        )
        if results is None:
            pass
        elif results is not None:
            await channel.send(embed=welcome_embed)
            cursor.close()
            db.close()

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT joinlogs FROM guild_config WHERE guild_id = ?", (member.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        leave_embed = discord.Embed(
            title="User has left.",
            color=discord.Colour.blurple()
        )
        leave_embed.set_author(
            name=member,
            icon_url=member.avatar_url
        )
        leave_embed.timestamp = datetime.datetime.utcnow()
        leave_embed.set_thumbnail(
            url=member.avatar_url
        )
        if results is None:
            pass
        elif results is not None:
            await channel.send(embed=leave_embed)
            cursor.close()
            db.close()

def setup(bot):
    bot.add_cog(welcomer(bot))
    print("Welcome extension has loaded!")