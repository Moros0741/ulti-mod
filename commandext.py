# commands.py
import os

import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
import random
from random import choice
import platform
import datetime
import sqlite3

class UltiMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Help menu
    @commands.command()
    async def help(self, ctx):
        curpage = 1
        totpage = 6
        
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT prefix FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchone()
        prefix = str(results[0][0])

        hlpembed = discord.Embed(
            title= "UltiMod Help & Information.",
            description= "List of all command uses, and setup information. ",
            color=2123412
        )
        hlpembed.add_field(
            name= "How to use:",
            value= """React with the corresponding emoji to jump straight to the page you would like.
            
            ❌ - Close Help Menu
            __**Pages:**__
            🛠️ - Utility Commands Menu.
            🛡️ - Moderation Commands Menu.
            🎁 - Giveaway Commands Menu.
            📁 - Logs Configuration Commands.
            📨 - Future features and information.""",
            inline=False
        )
        utilembed = discord.Embed(
            title= "Utility Commands.",
            description= "current utility commands and their usages.",
            color=15844367
        )
        utilembed.add_field(
            name= f"{prefix}echo <#channel> <message>",
            value= "*Echo's the message as if from the bot.*. **Note:** *Channel is required. if you wish to post in the same channel just mention that channel.*",
            inline=False
        )
        utilembed.add_field(
            name= f"{prefix}hello",
            value= "*Similar to 'ping' command on other bots. Bot responds with a unique message.*",
            inline=False
        )
        utilembed.add_field(
            name= f"{prefix}botinfo",
            value= "*Displays Nerd infor for the bot. Current build, Code Language, shards and whether premium is active.*",
            inline=False
        )
        utilembed.add_field(
            name= f"{prefix}channelid",
            value="*Fetches the ID for the server channel mentioned.*",
            inline=False
        )
        utilembed.add_field(
            name=f"{prefix}whois",
            value="*Fetches information about the specified user. Currently supports only @mentions.*",
            inline=False
        )
        utilembed.add_field(
            name=f"{prefix}avatar @user",
            value="*Fetches the avatar of the mentioned user and relays in an embed.*",
            inline=False
        )
        utilembed.add_field(
            name=f"{prefix}channelstats or ?cs",
            value="*Fetches cool information about the channel. Such as, permissions, slowmode time, creation date, etc.*",
            inline=False
        )
        utilembed.add_field(
            name=f"{prefix}roleadd @user <rolename>",
            value="*Adds the specified role to the mentioned user.*",
            inline=False
        )
        utilembed.add_field(
            name=f"{prefix}roleremove @user <rolename>",
            value="*Removes the specified role from the mentioned user.*",
            inline=False
        )
        utilembed.add_field(
            name=f"{prefix}support",
            value="*Gives you a link to join UltiMod's support server*",
            inline=False
        )
        utilembed.add_field(
            name=f"{prefix}inviteme",
            value="*Displays the authorization link to invite UltiMod to your server.*",
            inline=False
        )
        utilembed.add_field(
            name=f"{prefix}bug <message>",
            value="*Sends a bug report to the support server where developers can either contact you to help you work around a bug or get right into fixing it for you.*"
        )
        modembed = discord.Embed(
            title= "Moderation Commands",
            description= "Moderation commands an their uses.",
            color=15158332
        )
        modembed.add_field(
            name="Warning system coming soon",
            value="*The warning system will be released shortly, It takes an extensive amount of coding to do what we would like it to do. When released you can expect to see a users warnings, actions taken against them, number of times they have been warned by a specific moderator, all server warnings, as well as see which moderators are sending out the most warnings. *",
            inline=False
        )
        modembed.add_field(
            name=f"{prefix}mute @user <reason>",
            value="*Mutes the mentioned user and provides a reason.*",
            inline=False
        )
        modembed.add_field(
            name=f"{prefix}unmute @user [Opt: <reason>]",
            value= "*Unmutes the mentioned user, and provides the optional reason.*",
            inline=False
        )
        modembed.add_field(
            name=f"{prefix}kick @user <reason>",
            value="*Kicks the mentioned user and provides a reason*",
            inline=False
        )
        modembed.add_field(
            name=f"{prefix}invkick @user_ID",
            value="*Invites the kicked user.*",
            inline=False
        )
        modembed.add_field(
            name=f"{prefix}ban @user <reason>",
            value="*Bans the mentioned user and provides a reason.*",
            inline=False
            )

        modembed.add_field(
            name=f"{prefix}unban <user_ID>",
            value="*Unbans the user mentioned.*",
            inline=False
        )
        givembed = discord.Embed(
            title= "Giveaway Commands",
            description="Giveaway commands and their uses.",
            color=10181046
        )
        givembed.add_field(
            name=f"{prefix}eventcreate <'event_name'> <'event prize'>",
            value="*Creates an event using the name and prize stated. Creates embed and add reaction for contestants to enter.*",
            inline=False
        )
        givembed.add_field(
            name=f"{prefix}eventdel <event_ID>",
            value="*Deletes the event specified via the Event ID. (can be found in footer of event embed)*",
            inline=False
        )
        givembed.add_field(
            name=f"{prefix}eventforce",
            value= "*Forces the bot to end the event and choose a winner.*",
            inline=False
        )
        loggembed = discord.Embed(
            title= "Logging Configuration Commands",
            description="Setup commands for setting the log channels. \n\n**REQUIRES:** Manage Server permissions to execute.",
            color=3066993
        )
        loggembed.add_field(
            name=f"{prefix}config msglogs <#channel>",
            value="*Sets the mentioned channel as the message logs channel.*",
            inline=False
        )
        loggembed.add_field(
            name=f"{prefix}config modlogs <#channel>",
            value="*Sets the mentioned channel as the moderation logs channel.*",
            inline=False
        )
        loggembed.add_field(
            name=f"{prefix}config welcomelogs <#channel>",
            value= "*Sets the channel that welcome messages will be posted in.*",
            inline=False
        )
        loggembed.add_field(
            name=f"{prefix}config serverlogs <#channel>",
            value="*Sets the channel that any audit logs will be sent to. i.e: role permissions updates, etc.*",
            inline=False
        )
        loggembed.add_field(
            name=f"{prefix}config tickets <category_name>",
            value="*Sets the category the support ticket channels will be created under.*",
            inline=False
        )
        featembed = discord.Embed(
            title="Future Features and information",
            description="We are constantly working on adding new features to UltiMod and fixing bugs that everyone has reported to us. Here is some fun and useful information about UltiMod for you.",
            color=discord.Colour.gold()
        )
        featembed.add_field(
            name="NEW Features Coming Soon!!",
            value="-Auto-Mod system \n-Warnings System \n-Leveling System \n-Economy System (with customizable guild stores) \n-Modmail or ticket system \n-Reaction Roles system \n-Various games/trivia extensions server managers can turn on and off for their server!.",
            inline=False
        )
        featembed.add_field(
            name="Known Bugs and current working fixes.",
            value="1. We are currently aware of issues where if a player uses the help command in two different guilds, the bot will change pages to both help messages in each guild no matter which is reacted to. We are currently working on a check system to prevent this from happening. \n\n 2. Verify System - We expect issues with the verified system not working after a bot outage. To mitigate this issue users will have to redo the command if the bot goes down. (unlikely) \n\n 3. whois command - Although we plan to update this command in the future, it currently does not allow look up for users not in your guid or mutual guild with the bot. \n\n 4. settings command - We are aware of the settings command bugging out when guild managers have not completely set up their guild's roles and log channels with UltiMod. This feature will be fixed in the very near future.",
            inline=False
        )
        message = await ctx.send(f"Page: {curpage}/{totpage}", embed=hlpembed)
        await message.add_reaction('🛠️')
        await message.add_reaction('🛡️')
        await message.add_reaction('🎁')
        await message.add_reaction('📁')
        await message.add_reaction('📨')
        await message.add_reaction('❌')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['❌', '📁', '🎁', '🛡️', '🛠️','📨']
        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                
                if str(reaction.emoji) == '🛠️':
                    curpage = 2
                    await message.edit(content=f"Page: {curpage}/{totpage}", embed=utilembed)
                    await message.remove_reaction(reaction, user)
                
                elif str(reaction.emoji) == '🛡️':
                    curpage = 3
                    await message.edit(content=f"Page: {curpage}/{totpage}", embed=modembed)
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == '🎁':
                    curpage = 4
                    await message.edit(content=f"Page: {curpage}/{totpage}", embed=givembed)
                    await message.remove_reaction(reaction, user)
                
                elif str(reaction.emoji) == '📁':
                    curpage = 5
                    await message.edit(content=f"Page: {curpage}/{totpage}", embed=loggembed)
                    await message.remove_reaction(reaction, user)
                
                elif str(reaction.emoji) == '📨':
                    curpage = 6
                    await message.edit(content=f"Page: {curpage}/{totpage}", embed=featembed)
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == '❌':
                    await message.delete()

            except asyncio.TimeoutError:
                await message.clear_reaction('❌')
                await message.clear_reaction('📨')
                await message.clear_reaction('📁')
                await message.clear_reaction('🎁')
                await message.clear_reaction('🛡️')
                await message.clear_reaction('🛠️')
                

    ### CLASS: Utility commands ###
    #-----------------------------#

    # Ping command #Finished
    @commands.command()
    async def hello(self, ctx):
        helloembed = discord.Embed(
            description= f"Yes {ctx.author.mention}, Can I help you with something?",
            color=15844367
        )
        helloembed.set_image(
            url='https://media1.tenor.com/images/06ea225c668e10581763f20501a41825/tenor.gif',
        )
        await ctx.send(embed=helloembed)

    # Purge Command #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def purge(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        purgembed = discord.Embed(
            title="Channel has been purged!",
            description=f"**Channel:** {ctx.channel.mention} \n**Messages purged:** {len(deleted)} \n**Purged by:** {ctx.author.mention}",
            color=2123412
        )
        purgembed.set_thumbnail(
            url=ctx.author.avatar_url
        )
        purgembed.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        purgembed.timestamp = datetime.datetime.utcnow()

        await ctx.send(f"Channel has been purged by {ctx.author.mention}")
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT msglogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        await channel.send(embed=purgembed)
        cursor.close()
        db.close()

    # Echo Command #Finished
    @commands.command()
    async def echo(self, ctx, channel:discord.TextChannel, *, message=""): 
        await ctx.message.add_reaction('✅')
        channel = self.bot.get_channel(channel.id)
        if not channel:
            await ctx.send("What do you want me to say?")
        else:
            await channel.send(message)

    # Bot Info command #Finished
    @commands.command()
    async def botinfo(self, message):
        developer = "Moros#0741 (700057705951395921)"
        pyversion = platform.python_version()
        dpyversion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
        botshards = self.bot.shard_count
        botinembed = discord.Embed(
            title= "Bot Info",
            description="Stats for the nerds. :wink:",
            color=3447003
        )
        botinembed.add_field(
            name="Developer:",
            value=developer
        )
        botinembed.add_field(
            name= "Bot Version:",
            value= "1.0.0",
            inline=False
        )
        botinembed.add_field(
            name= "Discord API:",
            value= f"discord.py v{dpyversion}",
            inline=False
        )
        botinembed.add_field(
            name= "Code Language:",
            value= f"Python v{pyversion}",
            inline=False
        )
        botinembed.add_field(
            name="Members Served:",
            value=memberCount,
            inline=False
        )
        botinembed.add_field(
            name="Servers Protected:",
            value=serverCount,
            inline=False
        )
        botinembed.add_field(
            name="Total Shards:",
            value=botshards,
            inline=False
        )
        botinembed.add_field(
            name= "Premium Features:",
            value= "🟢 Enabled",
            inline=False
        )
        botinembed.set_thumbnail(
            url=self.bot.user.avatar_url
        )
        botinembed.timestamp = datetime.datetime.utcnow()
        botinembed.set_footer(
            text="UltiMod Server Protection System",
            icon_url=self.bot.user.avatar_url
        )
        await message.send(embed=botinembed)

    # Channel ID Command #Finished
    @commands.command()
    async def channelid(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"Here's the ID for that channel: {channel.id}")

    @commands.command()  
    @has_permissions(manage_guild=True)
    async def getusers(self, ctx, *, role):
        roles = discord.utils.get(ctx.guild.roles, name=role)
        empty = False
        usersembed = discord.Embed(
            color=discord.Colour.orange()
        )
        usersembed.add_field(
            name="Users with that role:",
            value="Compiling a list....",
            inline=False
        )
        usersembed.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        usersembed.timestamp = datetime.datetime.utcnow()
        message = await ctx.send(embed=usersembed)
        members = []
        if roles is None:
            usersembed.set_field_at(0, name="Users with role:", value="```None```")
            await message.edit(embed=usersembed)
            empty = True
            return
        for member in ctx.guild.members:
            if roles in member.roles:
                members.append(f'{member}')
                for member in members:
                    usersembed.set_field_at(0, name="Users with that role:", value="```{}```".format('\n'.join(members)))
                    await message.edit(embed=usersembed)
        if empty:
            await ctx.send("Nobody has the role {}".format(roles.mention))

    # User Info command #Finished
    @commands.command()
    async def whois(self, ctx, member: discord.Member):
        userid = member.id
        name = member
        created_at = member.created_at.strftime("%b %d, %Y")
        joined_on = member.joined_at.strftime("%b %d, %Y")
        roles = [role.mention for role in member.roles if role.mentionable]
        whoisembed = discord.Embed(
            title= f"Who is {member.name}?",
            color=15844367
        )
        whoisembed.add_field(
            name= "Username & Discriminator:",
            value=name,
            inline=False
        )
        whoisembed.add_field(
            name= "User ID:",
            value=userid,
            inline=False
        )
        whoisembed.add_field(
            name="Roles:",
            value="This does not include unmentionable roles: \n{}".format('\n'.join(roles)),
            inline=False
        )
        whoisembed.add_field(
            name= "Account Creation:",
            value=f"Created on: {created_at}.",
            inline=True
        )
        whoisembed.add_field(
            name= "Joined:",
            value= f"Joined on: {joined_on}.",
            inline=True
        )
        whoisembed.set_thumbnail(
            url=member.avatar_url
            )

        whoisembed.set_footer(
            text="User Background Check.",
            icon_url=self.bot.user.avatar_url
        )
        whoisembed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=whoisembed)

    # Server Info command #working
    @commands.command()
    async def serverinfo(self, ctx):
        server = ctx.message.guild
        servericon = ctx.guild.icon_url
        created = server.created_at
        serverid = server.id
        owner_no = server.owner_id
        vchannels = len(server.voice_channels)
        tchannels = len(server.text_channels)
        totmems = len(ctx.message.guild.members) # includes bots
        tothums = len([m for m in ctx.message.guild.members if not m.bot]) # excludes bots
        serverembed = discord.Embed(
            title= f"Server info for {server}.",
            color=2123412
        )
        serverembed.add_field(
            name= "Server ID:",
            value=serverid,
            inline=False
        )
        serverembed.add_field(
            name= "Server Owner ID:",
            value=owner_no,
            inline=False
        )
        serverembed.add_field(
            name="Text Channels:",
            value=tchannels,
            inline=True
        )
        serverembed.add_field(
            name="Voice Channels:",
            value=vchannels,
            inline=True
        )
        serverembed.add_field(
            name= '\u200b',
            value= '\u200b',
            inline=True
        )

        serverembed.add_field(
            name="Members:",
            value=tothums,
            inline=True
        )
        serverembed.add_field(
            name= "Total Members:",
            value=totmems,
            inline=True
        )
        serverembed.add_field(
            name='\u200b',
            value='\u200b',
            inline=True
        )
        serverembed.add_field(
            name="Server created on:",
            value=created,
            inline=False
        )
        serverembed.set_thumbnail(
            url=servericon
        )
        serverembed.set_footer(
            text="UltiMod Server Protection System",
            icon_url=self.bot.user.avatar_url
        )
        serverembed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=serverembed)

    # Fetch Avatar command #working
    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        avembed = discord.Embed(
            color=2123412
        )
        avembed.set_image(url=userAvatarUrl)
        avembed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=avembed)

    # Channel Stats command #working
    @commands.command(aliases=['cs', 'cstats'])
    async def channelstats(self, ctx):
        channel = ctx.channel
        csembed = discord.Embed(
            title=f"Channel stats for {channel.name}",
            description=f"Category: {channel.category.name}",
            color=2123412
        )
        csembed.add_field(
            name="Channel Guild:",
            value=ctx.guild.name,
            inline=False
        )
        csembed.add_field(
            name="Channel ID:",
            value=channel.id,
            inline=False
        )
        csembed.add_field(
            name="Channel Topic:",
            value=f"{channel.topic if channel.topic else 'No Topic'}",
            inline=False
        )
        csembed.add_field(
            name="Channel Position:",
            value=channel.position,
            inline=False
        )
        csembed.add_field(
            name="Channel Slowmode:",
            value=channel.slowmode_delay,
            inline=False
        )
        csembed.add_field(
            name="Channel is NSFW:",
            value=channel.is_nsfw(),
            inline=False
        )
        csembed.add_field(
            name="Channel is News:",
            value=channel.is_news(),
            inline=False
        )
        csembed.add_field(
            name="Channel created on:",
            value=channel.created_at,
            inline=False
        )
        csembed.add_field(
            name="Channel permissions synced:",
            value=channel.permissions_synced,
            inline=False
        )
        csembed.add_field(
            name="Channel Hash:",
            value=hash(channel),
            inline=False
        )
        csembed.set_thumbnail(
            url=ctx.guild.icon_url
        )
        csembed.set_footer(
            text="UltiMod Server Protection System",
            icon_url=self.bot.user.avatar_url
        )
        csembed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=csembed)

    # Add role command #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def roleadd(self, ctx, member: discord.Member, rolename):
        roles = discord.utils.get(ctx.guild.roles, name=rolename)
        await member.add_roles(roles)
        await ctx.send(f":white_check_mark: Success! {member.mention} has been given the `{rolename}` role.")
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT serverlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        roleadd_embed = discord.Embed(
            title="A role has been given!",
            color=discord.Colour.green()
        )
        roleadd_embed.add_field(
            name="Role given to:",
            value=member.mention,
            inline=False
        )
        roleadd_embed.add_field(
            name="Role Given:",
            value=rolename,
            inline=False
        )
        roleadd_embed.add_field(
            name="Role given by:",
            value=ctx.author.mention,
            inline=False
        )
        roleadd_embed.set_thumbnail(
            url=member.avatar_url
        )
        roleadd_embed.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        roleadd_embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=roleadd_embed)
        cursor.close()
        db.close()

    # Remove role command #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def roleremove(self, ctx, member: discord.Member, rolename):
        roles = discord.utils.get(ctx.guild.roles, name=rolename)
        await member.remove_roles(roles)
        await ctx.send(f":white_check_mark: Success! Role: `{rolename}` has been removed from {member.mention}.")
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT serverlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        roleremove_embed = discord.Embed(
            title="A role has been taken!",
            color=discord.Colour.red()
        )
        roleremove_embed.add_field(
            name="Role taken from:",
            value=member.mention,
            inline=False
        )
        roleremove_embed.add_field(
            name="Role Taken:",
            value=rolename,
            inline=False
        )
        roleremove_embed.add_field(
            name="Role taken by:",
            value=ctx.author.mention
        )
        roleremove_embed.set_thumbnail(
            url=member.avatar_url
        )
        roleremove_embed.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        roleremove_embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=roleremove_embed)
        cursor.close()
        db.close()

    # Bug report command #Finished
    @commands.command()
    async def bug(self, ctx, *, message):
        message=message
        channel = self.bot.get_channel(id=772573156498079824)
        bug_embed = discord.Embed(
            title="A Bug Report has been Submitted",
            color=discord.Colour.orange()
        )
        bug_embed.add_field(
            name="Reporting User:",
            value=f"{ctx.author} | ID: {ctx.author.id}",
            inline=False
        )
        bug_embed.add_field(
            name="Reported Bug:",
            value=message,
            inline=False
        )
        bug_embed.set_thumbnail(
            url =ctx.author.avatar_url
        )
        bug_embed.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        bug_embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(f":ok_hand: {ctx.author.mention} your bug report has been submitted!")
        await channel.send(embed=bug_embed)

    # Bot invite command
    @commands.command()
    async def inviteme(self, ctx):
        invite_embed = discord.Embed(
            title="Want to invite UltiMod?",
            description="[Invite UltiMod](https://discord.com/api/oauth2/authorize?client_id=749299900965191781&permissions=8&scope=bot)",
            color=discord.Colour.gold()
        )
        invite_embed.set_footer(
            text="UltiMod Server Protection",
            icon_url=self.bot.user.avatar_url
        )
        invite_embed.set_thumbnail(
            url=self.bot.user.avatar_url
        )
        invite_embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=invite_embed)

    # Support server invite command
    @commands.command()
    @has_permissions(manage_guild=True)
    async def support(self, ctx):
        support_embed = discord.Embed(
            title="Need help?",
            description="Join our support server: \n[UltiMod Support](https://discord.gg/XpDDHZuZhJ)",
            color=discord.Colour.orange()
        )
        support_embed.set_thumbnail(
            url=self.bot.user.avatar_url
        )
        support_embed.set_footer(
            text = "UltiMod Server Protection",
            icon_url=self.bot.user.avatar_url
        )
        support_embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=support_embed)

    ### CLASS:  Moderator Commands ###
    #--------------------------------#

    #Warning command
    @commands.command()
    @has_permissions(manage_guild=True)
    async def warn(self, ctx, user: discord.User, *, reason):
        warnembed = discord.Embed(
            title="Warning Issued!",
            color=discord.Colour.gold()
        )
        warnembed.add_field(
            name="User Warned:",
            value=user.mention,
            inline=False
        )
        warnembed.add_field(
            name="Reason:",
            value=reason,
            inline=False
        )
        warnembed.add_field(
            name="Moderator:",
            value=ctx.author.mention,
            inline=False
        )
        warnembed.set_thumbnail(
            url=user.avatar_url
        )
        warnembed.set_footer(
            text = ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        warnembed.timestamp = datetime.datetime.utcnow()
        await ctx.send(f":thumbsup: `{user}` has been warned for `{reason}`.")
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT modlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        await channel.send(embed=warnembed)
        cursor.close()
        db.close()

    # DM user Command #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def userdm(self, ctx, user: discord.Member, *, message):

        await user.send(f"From {ctx.author}: {message}")
        await ctx.message.add_reaction('✅')

    # Mute Command #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def mute(self, ctx, member: discord.Member, *, reason="No reason provided."):
        reason=reason
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT muteroles FROM muterole WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        rolename = str(results[0][0])
        role = discord.utils.get(ctx.guild.roles, name=rolename)
        cursor.close()
        db.close()
        await member.add_roles(role)
        succmute = discord.Embed(
            title="User Muted!",
            color=15105570
        )
        succmute.add_field(
            name= "User:",
            value=f"{member.mention}",
            inline=False
        )
        succmute.add_field(
            name="Reason:",
            value=reason,
            inline=False
        )
        succmute.add_field(
            name="Responsible moderator:",
            value=ctx.author.mention,
            inline=False
        )
        succmute.set_thumbnail(
            url=member.avatar_url
        )
        succmute.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        succmute.timestamp = datetime.datetime.utcnow()

        await ctx.send(f":thumbsup: `{member}` has been muted indefinitely. Reason: `{reason}`")
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT modlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        await channel.send(embed = succmute)
        cursor.close()
        db.close()

    # Unmute command #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def unmute(self, ctx, member: discord.Member):
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT muteroles FROM muterole WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        rolename = str(results[0][0])
        role = discord.utils.get(ctx.guild.roles, name=rolename)
        cursor.close()
        db.close()
        await member.remove_roles(role)
        await ctx.send(f":thumbsup:`{member}` has been unmuted!")
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT modlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        succunmute = discord.Embed(
            title="User has been unmuted!",
            color = discord.Colour.green()
        )
        succunmute.add_field(
            name="Unmuted User:",
            value=member.mention,
            inline=False
        )
        succunmute.add_field(
            name="Unmuted by:",
            value=ctx.author.mention,
            inline=False
        )
        succunmute.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        succunmute.set_thumbnail(
            url=member.avatar_url
        )
        succunmute.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=succunmute)
        cursor.close()
        db.close()
    
    # Kick Command #Finished
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason="No reason provided."):
            server = ctx.guild
            kickem = discord.Embed(
                title=":boot: User has been kicked! :boot:",
                color=15105570
            )
            kickem.add_field(
                name="Kicked User:",
                value=f"{user.mention} \n **User ID:** {user.id}",
                inline=False
            )
            kickem.add_field(
                name="Reason:",
                value=reason,
                inline=False
            )
            kickem.add_field(
                name="Responsible Moderator:",
                value=ctx.author.mention,
                inline=False
            )
            kickem.set_thumbnail(
                url=user.avatar_url
            )
            kickem.set_footer(
                text=server,
                icon_url=server.icon_url
            )
            kickem.timestamp = datetime.datetime.utcnow()

            await user.send(f'You have been kicked! \n __**Server:**__ {server} \n __**Reason:**__ {reason} \n __**Moderator:**__ {ctx.author.name}')   
            await user.kick(reason=reason)
            await ctx.message.delete()
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT modlogs FROM guild_config WHERE guild_id = ?", (server.id,))
            results = cursor.fetchall()
            channel = self.bot.get_channel(int(str(results[0][0])))
            await channel.send(embed=kickem)
            cursor.close()
            db.close()

    # Invite Kick Command #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def invkick(self, ctx, user: discord.Member, *, reason="No reason given."):
        channel = ctx.channel
        server = ctx.guild
        code = await channel.create_invite()
        await user.send(f"You have been kicked from {server} for {reason} by{ctx.author.name}. \n Here is an invite back: {code}")
        await user.kick(reason=reason)
        kickdem = discord.Embed(
            title=":boot: User has been kicked! :boot:",
            color=15105570
        )
        kickdem.add_field(
            name="Kicked User:",
            value=f"{user.mention} \n **User ID:** {user.id}",
            inline=False
        )
        kickdem.add_field(
            name="Reason:",
            value=reason,
            inline=False
        )
        kickdem.add_field(
            name="Responsible Moderator:",
            value=ctx.author.mention,
            inline=False
        )
        kickdem.set_thumbnail(
            url=user.avatar_url
        )
        kickdem.set_footer(
            text= server,
            icon_url=server.icon_url
        )
        kickdem.timestamp = datetime.datetime.utcnow()

        await ctx.send(f":thumbsup: `{user}` has been kicked and invited back. Reason: `{reason}`")
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT modlogs FROM guild_config WHERE guild_id = ?", (server.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        await channel.send(embed=kickdem)
        cursor.close()
        db.close()

    # Ban Command #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def ban(self, ctx, user: discord.Member, *, reason="No reason provided"):
            server = ctx.guild
            banem = discord.Embed(
                title=":hammer: User has been banned! :hammer:",
                color=15105570
            )
            banem.add_field(
                name="Banned User:",
                value=f"{user.mention} \n **User ID:** {user.id}",
                inline=False
            )
            banem.add_field(
                name="Reason:",
                value=reason,
                inline=False
            )
            banem.add_field(
                name="Responsible Moderator:",
                value=ctx.author.mention,
                inline=False
            )
            banem.set_thumbnail(
                url=user.avatar_url
            )
            banem.set_footer(
                text=server,
                icon_url=server.icon_url
            )
            banem.timestamp = datetime.datetime.utcnow()

            await user.send(f'You have been banned! \n __**Server:**__ {server} \n __**Reason:**__ {reason} \n __**Moderator:**__ {ctx.author.name}')
            await user.ban(reason=reason)
            await ctx.message.delete()
            await ctx.send(f":thumbsup: `{user}` has been banned indefinitely. Reason: `{reason}`")
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT modlogs FROM guild_config WHERE guild_id = ?", (server.id,))
            results = cursor.fetchall()
            channel = self.bot.get_channel(int(str(results[0][0])))
            await channel.send(embed=banem)
            cursor.close()
            db.close()

    # Unban Command #working #NEEDS MOD LOGGING
    @commands.command()
    @has_permissions(administrator=True)
    async def unban(self, ctx, id: int):
        user = await self.bot.fetch_user(id)
        unbanem = discord.Embed(
            title= ":white_check_mark: User has been unbanned!",
            color=2067276
        )
        unbanem.add_field(
            name= "Unbanned User:",
            value=f"{user}",
            inline=False
        )
        unbanem.add_field(
            name="Responsible Admin:",
            value=f"{ctx.author.mention}",
            inline=False
        )
        unbanem.set_thumbnail(
            url=user.avatar_url
        )
        unbanem.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        unbanem.timestamp = datetime.datetime.utcnow()
        await ctx.guild.unban(user)
        await ctx.send(f":thumbsup: `{user}` has been unbanned!")
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT modlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        channel = self.bot.get_channel(int(str(results[0][0])))
        await channel.send(embed=unbanem)
        cursor.close()
        db.close()

    ### Giveaway Commands Section###
    #------------------------------#

    @commands.command()
    async def trigger(self, ctx):
        await ctx.send("?help")

    # Event creation Command #Finished
    @commands.command()
    async def eventcreate(self, ctx, arg1, arg2):
        global eventembed
        eventembed = discord.Embed(
            title= ":partying_face: GIVEAWAY!!! :partying_face:",
            color=7419530
        )
        eventembed.add_field(
            name= "Event",
            value=arg1,
            inline=False
        )
        eventembed.add_field(
            name= "Prize:",
            value=arg2,
            inline=False
        )
        eventembed.add_field(
            name= "Entered:",
            value="\u200b",
            inline=False
        )
        eventembed.set_thumbnail(
            url='https://i.imgur.com/v1f3ay1.png'
        )
        message = await ctx.send(embed=eventembed)
        await message.add_reaction('🥳')
        msg = await ctx.fetch_message(message.id)
        eventembed.set_footer(
            text=f"React with '🥳' below to enter | Event ID: {msg.id}"
                )
        await message.edit(embed=eventembed)

        def check ( reaction, user):
            return str(reaction.emoji) == '🥳' and user != self.bot.user
        
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=604800, check=check)
                msg = await ctx.fetch_message(message.id)
                
                global reactors
                reactors = []
                for reaction in msg.reactions:
                    if reaction.emoji == '🥳':
                        async for user in reaction.users():
                            if user != self.bot.user:
                                reactors.append(f'{user}')
                                eventembed.set_field_at(2, name="Entered:", value="```{}```".format('\n'.join(reactors)))
                                await message.edit(embed=eventembed)

            except asyncio.TimeoutError:
                await message.remove_reaction('🥳')
        
    # Event Deletion Command #Finished
    @commands.command()
    @has_permissions(manage_messages=True)
    async def eventdel(self, ctx, messid):
        message = await ctx.fetch_message(id=messid)
        await message.delete()
        await ctx.send("Success! Event has been deleted.")

    # Event Finish Command (Chooses winner) #Finished   
    @commands.command()
    @has_permissions(manage_guild=True)
    async def eventforce(self, ctx, messid):
        user = random.choice(reactors)
        message = await ctx.fetch_message(id=messid)
        await ctx.send(f"The winner is: {user}. Congratulations!!")
        eventembed.add_field(name="Winner:", value=f"Congratulations to {user}!", inline=False)
        await message.edit(embed=eventembed)
        await message.clear_reaction('🥳')

    #Guild Configuration class creation #Finished
    @commands.group(invoke_without_command=True)
    @has_permissions(manage_guild=True)
    async def config(self, ctx):
        await ctx.send("Please add a sub command so I know what to do!")

    # Config set guild prefix command #Finished
    @config.command()
    @has_permissions(manage_guild=True)
    async def setprefix(self, ctx, prefix):
        prefix=prefix
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT prefix FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchone()
        cursor.close()
        db.close()
        if results is None:
            await ctx.send("I can't find a prefix stored for this server, Hold on a second and I'll add this one.")
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            sql = ("INSERT INTO guild_config(guild_id, prefix) VALUES(?,?)")
            val = (ctx.guild.id, prefix)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! Server prefix set to: `{}`".format(prefix))

        elif results is not None:
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE guild_config SET prefix = ? WHERE guild_id = ?", (prefix, ctx.guild.id,))
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! Server prefix set to: `{}`".format(prefix))

    # Config Message logs channel command #Finished
    @config.command()
    @has_permissions(manage_guild=True)
    async def msglogs(self, ctx, channel:discord.TextChannel):
        channel = channel
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT guild_id, msglogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchone()
        cursor.close()
        db.close()
        if results is None:
            await ctx.send("I can't find a channel stored for this server, Hold on a second and I'll add this one.")
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            sql = ("INSERT INTO guild_config(guild_id, msglogs) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! The message logs channel has been set to: {}".format(channel.mention))

        elif results is not None:
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE guild_config SET msglogs = ? WHERE guild_id = ?", (channel.id, ctx.guild.id,))
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! The message logs channel has been set to: {}".format(channel.mention))

    # Config server logs channel command #Finished
    @config.command()
    @has_permissions(manage_guild=True)
    async def serverlogs(self, ctx, channel:discord.TextChannel):
        channel = channel
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT guild_id, serverlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchone()
        cursor.close()
        db.close()
        if results is None:
            await ctx.send("I can't find a channel stored for this server, Hold on a second and I'll add this one.")
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            sql = ("INSERT INTO guild_config(guild_id, serverlogs) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! The server logs channel has been set to: {}".format(channel.mention))

        elif results is not None:
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE guild_config SET serverlogs = ? WHERE guild_id = ?", (channel.id, ctx.guild.id,))
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! The server logs channel has been set to: {}".format(channel.mention))
    
    # Config welcome logs channel command #Finished
    @config.command()
    @has_permissions(manage_guild=True)
    async def welcomelogs(self, ctx, channel:discord.TextChannel):
        channel = channel
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT guild_id, joinlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchone()
        cursor.close()
        db.close()
        if results is None:
            await ctx.send("I can't find a channel stored for this server, Hold on a second and I'll add this one.")
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            sql = ("INSERT INTO guild_config(guild_id, joinloga) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! The Join/Leave logs channel has been set to: {}".format(channel.mention))

        elif results is not None:
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE guild_config SET joinlogs = ? WHERE guild_id = ?", (channel.id, ctx.guild.id,))
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! The Join/Leave logs channel has been set to: {}".format(channel.mention))

    # Config moderation logs channel command #Finished
    @config.command()
    @has_permissions(manage_guild=True)
    async def modlogs(self, ctx, channel:discord.TextChannel):
        channel = channel
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT guild_id, modlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchone()
        cursor.close()
        db.close()
        if results is None:
            await ctx.send("I can't find a channel stored for this server, Hold on a second and I'll add this one.")
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            sql = ("INSERT INTO guild_config(guild_id, modlogs) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! The moderator logs channel has been set to: {}".format(channel.mention))

        elif results is not None:
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE guild_config SET modlogs = ? WHERE guild_id = ?", (channel.id, ctx.guild.id,))
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(":white_check_mark: Success! The moderator logs channel has been set to: {}".format(channel.mention))

    @config.command()
    @has_permissions(manage_guild=True)
    async def muterole(self, ctx, *, rolename):
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT guild_id, muteroles FROM muterole WHERE guild_id = ?", (ctx.guild.id,))
        results = cursor.fetchall()
        cursor.close()
        db.close()
        if results is None:
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("INSERT INTO muterole(guild_id, muteroles) VALUES(?,?)", (ctx.guild.id, rolename,))
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(f":ok_hand: Muterole has been set to: `{rolename}`")
        elif results is not None:
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE muterole SET muteroles = ? WHERE guild_id = ?", (rolename, ctx.guild.id,))
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(f":ok_hand: Muterole has been set to: `{rolename}`")

    # View configured server settings #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def settings(self, ctx):
        db = sqlite3.connect('ultidb.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT modrole, adminrole, msglogs, serverlogs, joinlogs, modlogs, supportcat FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
        results1 = cursor.fetchone()
        if results1 is None:
            await ctx.send("Sorry, you haven't completely set up your server's logging. Please type `?config help` for setup help.")
        
        elif results1 is not None:
            db = sqlite3.connect('ultidb.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT prefix, modrole, adminrole, msglogs, serverlogs, joinlogs, modlogs, supportcat FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
            results = cursor.fetchone()
            prefix = str(results[0])
            adminrole = int(str(results[2]))
            modrole = int(str(results[1]))
            msglogs = int(str(results[3]))
            serverlogs = int(str(results[4]))
            joinlogs = int(str(results[5]))
            modlogs = int(str(results[6]))
            settingsembed = discord.Embed(
                title=f"Settings for {ctx.guild}",
                color=11027200
            )
            settingsembed.set_footer(
                text="Log Settings Panel"
            )
            settingsembed.set_thumbnail(
                url=ctx.guild.icon_url
            )
            settingsembed.timestamp = datetime.datetime.utcnow()
            settingsembed.add_field(
                name="Current Prefix:",
                value=f"{prefix}",
                inline=True
            )
            settingsembed.add_field(
                name="Moderator Role:",
                value=f"<@&{modrole}>",
                inline=False
            )
            settingsembed.add_field(
                name="Admin Role:",
                value=f"<@&{adminrole}>",
                inline=False
            )
            settingsembed.add_field(
                name="Moderator Logs:",
                value=f"<#{modlogs}>",
                inline=True
            )
            settingsembed.add_field(
                name='\u200b',
                value='\u200b',
                inline=True
            )
            settingsembed.add_field(
                name="Server Logs:",
                value=f"<#{serverlogs}>",
                inline=True
            )
            settingsembed.add_field(
                name="Message Logs:",
                value=f"<#{msglogs}>",
                inline=True
            )
            settingsembed.add_field(
                name='\u200b',
                value='\u200b',
                inline=True
            )
            settingsembed.add_field(
                name="Welcome Logs:",
                value=f"<#{joinlogs}>",
                inline=True
            )
            await ctx.send(embed=settingsembed)
    
    # Verify command for rules, etc. #Finished
    @commands.command()
    @has_permissions(manage_guild=True)
    async def verify(self, ctx, role, arg1, arg2):
        roles = discord.utils.get(ctx.guild.roles, name=role)
        verifyembed = discord.Embed(
            title=arg1,
            description=arg2,
            color = discord.Colour.green()
        )
        verifyembed.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        verifyembed.timestamp = datetime.datetime.utcnow()
        msg = await ctx.send(embed=verifyembed)
        await msg.add_reaction('✅')

        def check (reaction, user):
            return str(reaction.emoji) == '✅' and user != self.bot.user
        
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=check)
                if str(reaction.emoji) == '✅':
                    await user.add_roles(roles)
                    await msg.remove_reaction(reaction, user)
                    db = sqlite3.connect('ultidb.sqlite')
                    cursor = db.cursor()
                    cursor.execute("SELECT serverlogs FROM guild_config WHERE guild_id = ?", (ctx.guild.id,))
                    results = cursor.fetchall()
                    channel = self.bot.get_channel(int(str(results[0][0])))
                    verified_embed = discord.Embed(
                        title="User has agreed!",
                        color=discord.Colour.green()
                    )
                    verified_embed.add_field(
                        name="User:",
                        value=user.mention,
                        inline=False
                    )
                    verified_embed.set_thumbnail(
                        url=user.avatar_url
                    )
                    verified_embed.set_footer(
                        text = "UltiMod Verify System",
                        icon_url = self.bot.user.avatar_url
                    )
                    verified_embed.timestamp = datetime.datetime.utcnow()
                    await channel.send(embed=verified_embed)
                    cursor.close()
                    db.close()

            except asyncio.TimeoutError:
                raise
           
def setup(bot):
    bot.add_cog(UltiMod(bot))
    print("Commands Extension loaded successfully")