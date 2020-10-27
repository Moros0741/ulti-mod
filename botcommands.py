# commands.py
import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Help menu
    @commands.command()
    async def help(self, ctx):
        curpage = 1
        totpage = 5
        

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
            📁 - Logging and Automod Setup Menu.""",
            inline=False
        )
        hlpembed.add_field(
            name= "Interactive setup:",
            value= " Type `?config`.",
            inline=False
        )

        utilembed = discord.Embed(
            title= "Utility Commands.",
            description= "current utility commands and their usages.",
            color=15844367
        )
        utilembed.add_field(
            name= "?say <message>",
            value= "*Echo's the message as if from the bot.*",
            inline=False
        )
        utilembed.add_field(
            name= "?hello",
            value= "*Similar to 'ping' command on other bots. Bot responds with a unique message.*",
            inline=False
        )
        utilembed.add_field(
            name= "?botinfo",
            value= "*Displays Nerd infor for the bot. Current build, Code Language, shards and whether premium is active.*",
            inline=False
        )
        utilembed.add_field(
            name= "?channelid",
            value="*Fetches the ID for the server channel mentioned.*",
            inline=False
        )
        utilembed.add_field(
            name="?userid",
            value="*Fetches the user ID of the member mentioned.*",
            inline=False
        )
        utilembed.add_field(
            name="?avatar @user",
            value="*Fetches the avatar of the mentioned user and relays in an embed.*",
            inline=False
        )
        utilembed.add_field(
            name="?channelstats or ?cs",
            value="*Fetches cool information about the channel. Such as, permissions, slowmode time, creation date, etc.*",
            inline=False
        )
        utilembed.add_field(
            name="?roleadd @user <rolename>",
            value="*Adds the specified role to the mentioned user.*",
            inline=False
        )
        utilembed.add_field(
            name="?roleremove @user <rolename>",
            value="*Removes the specified role from the mentioned user.*",
            inline=False
        )
        modembed = discord.Embed(
            title= "Moderation Commands",
            description= "Moderation commands an their uses.",
            color=15158332
        )
        modembed.add_field(
            name= "?warn @user <reason>",
            value="*Warns the user mentioned and provides a reason.*",
            inline=False
        )
        modembed.add_field(
            name="?warnings or ?warnings @user",
            value="*Displays warnings in the server, or warnings from a mentioned user.*",
            inline=False
        )
        modembed.add_field(
            name="?delwarn @user <case #>",
            value="*Deleted the specified warning from the mentioned user. NOTE: Must have case number from modlogs or warnings.*",
            inline=False
        )
        modembed.add_field(
            name="?clearwarns @user or ?clw @user",
            value="*Deletes all warnings from the mentioned user.*",
            inline=False
        )
        modembed.add_field(
            name="?mute @user <reason>",
            value="*Mutes the mentioned user and provides a reason.*",
            inline=False
        )
        modembed.add_field(
            name="?unmute @user [Opt: <reason>]",
            value= "*Unmutes the mentioned user, and provides the optional reason.*",
            inline=False
        )
        modembed.add_field(
            name="?kick @user <reason>",
            value="*Kicks the mentioned user and provides a reason*",
            inline=False
        )
        modembed.add_field(
            name="?invkick @user_ID",
            value="*Invites the kicked user.*",
            inline=False
        )
        modembed.add_field(
            name="?ban @user <reason>",
            value="*Bans the mentioned user and provides a reason.*",
            inline=False
            )

        modembed.add_field(
            name="?unban <user_ID>",
            value="*Unbans the user mentioned.*",
            inline=False
        )
        givembed = discord.Embed(
            title= "Giveaway Commands",
            description="Giveaway commands and their uses.",
            color=10181046
        )
        givembed.add_field(
            name="?eventcreate <'event_name'> <'event prize'>",
            value="*Creates an event using the name and prize stated. Creates embed and add reaction for contestants to enter.*",
            inline=False
        )
        givembed.add_field(
            name="?eventdel <event_ID>",
            value="*Deletes the event specified via the Event ID. (can be found in footer of event embed)*",
            inline=False
        )
        givembed.add_field(
            name= "?eventforce",
            value= "*Forces the bot to end the event and choose a winner.*",
            inline=False
        )
        loggembed = discord.Embed(
            title= "Logging & Automod commands and setup.",
            description="Setup and control commands for logging and automod.",
            color=3066993
        )
        loggembed.add_field(
            name="?automodon",
            value="*Enables or disables automod features.*",
            inline=False
        )
        loggembed.add_field(
            name="?censorlist",
            value="*Displays an Embedded list of the banned words list.*",
            inline=False
        )
        loggembed.add_field(
            name="?censor <word>",
            value= "*Add a word or words to the censor list.*",
            inline=False
        )
        loggembed.add_field(
            name="?modlog <#channel-name>",
            value="*Adds the mentioned channel to the Modlogs. Bot will post moderation reports in this channel.*",
            inline=False
        )
        message = await ctx.send(f"Page: {curpage}/{totpage}", embed=hlpembed)
        await message.add_reaction('🛠️')
        await message.add_reaction('🛡️')
        await message.add_reaction('🎁')
        await message.add_reaction('📁')
        await message.add_reaction('❌')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['❌', '📁', '🎁', '🛡️', '🛠️']
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
                
                elif str(reaction.emoji) == '❌':
                    await message.delete()

            except asyncio.TimeoutError:
                await message.delete()

    ### CLASS: Utility commands ###
    #-----------------------------#

    # Ping command   
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

    # Purge Command
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
        await ctx.send(embed=purgembed)

    # Echo Command
    @commands.command(aliases=['echo', 'print'], description="say <message>")
    async def say(self, ctx, channel, *, message=""): 
        await ctx.message.delete()
        channel = self.bot.get_channel("id")
        if not channel:
            await ctx.send("What do you want me to say?")
        else:
            await self.bot.send(destination=channel, content=message) 

    # Bot Info command
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
            value= ":green_circle: Enabled",
            inline=False
        )
        botinembed.set_thumbnail(
            url='https://i.imgur.com/L6ipEgf.png'
        )
        await message.send(embed=botinembed)

    # Channel ID Command
    @commands.command()
    async def channelid(self, ctx, channel: discord.TextChannel):
        await ctx.send(f"Here's your mentioned channel's ID: {channel.id}")

    # User Info command
    @commands.command()
    async def whois(self, ctx, member: discord.Member):
        userid = member.id
        name = member
        created_at = member.created_at.strftime("%b %d, %Y")
        joined_on = member.joined_at.strftime("%b %d, %Y")
        propic = member.avatar_url

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
            value= userid,
            inline=False
        )
        whoisembed.add_field(
            name= "Account Creation:",
            value=f"Created on: {created_at}.",
            inline=False
        )
        whoisembed.add_field(
            name= "Joined:",
            value= f"Joined on: {joined_on}."
        )
        whoisembed.set_thumbnail(
            url=member.avatar_url
            )

        whoisembed.set_footer(
            text="User Background Check."
        )
        await ctx.send(embed=whoisembed)

    # Server Info command
    @commands.command()
    async def serverinfo(self, ctx):
        server = ctx.message.guild
        servericon = ctx.guild.icon_url
        created = server.created_at
        serverid = server.id
        owner_no = server.owner_id
        ownername = ctx.message.guild.owner
        vchannels = len(server.voice_channels)
        tchannels = len(server.text_channels)
        totmems = len(ctx.message.guild.members) # includes bots
        tothums = len([m for m in ctx.message.guild.members if not m.self.bot]) # excludes bots
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

        await ctx.send(embed=serverembed)

    # Fetch Avatar command
    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        avembed = discord.Embed(
            color=2123412
        )
        avembed.set_image(url=userAvatarUrl)

        await ctx.send(embed=avembed)

    # Channel Stats command
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
            url='https://i.imgur.com/L6ipEgf.png'
        )
        await ctx.send(embed=csembed)

    # Add role command
    @commands.command()
    @has_permissions(manage_guild=True)
    async def roleadd(self, ctx, member: discord.Member, rolename):
        roles = discord.utils.get(ctx.guild.roles, name=rolename)
        await member.add_roles(roles)
        await ctx.send(f":white_check_mark: Success! {member.mention} has been given the `{rolename}` role.")

    # Remove role command
    @commands.command()
    @has_permissions(manage_guild=True)
    async def roleremove(self, ctx, member: discord.Member, rolename):
        roles = discord.utils.get(ctx.guild.roles, name=rolename)
        await member.remove_roles(roles)
        await ctx.send(f":white_check_mark: Success! Role: `{rolename}` has been removed from {member.mention}.")

    # Custom Embed creator command



    ### CLASS:  Moderator Commands ###
    #--------------------------------#

    ## SUB CLASS:  Warning Commands ##

    # Warn Command


    # Warnings Commands (view warnings)


    # Clear All Warnings Command


    # Delete Single Warning Command


    ## SUB CLASS: Other Mod Commands ##

    # DM user Command
    @commands.command()
    @has_permissions(administrator=True)
    async def userdm(self, ctx, user: discord.Member, *, message):

        await user.send(f"From {ctx.author}: {message}")
        await ctx.message.add_reaction('✅')

    # Mute Command
    @commands.command()
    @has_permissions(manage_guild=True)
    async def mute(self, ctx, member: discord.Member, *, reason="No reason provided."):
        reason=reason
        role = discord.utils.get(ctx.guild.roles, name='Muted')
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
        await ctx.send(embed=succmute)

    # Unmute command
    @commands.command()
    @has_permissions(manage_guild=True)
    async def unmute(ctx, member: discord.Member):
        role = role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} has been unmuted by {ctx.author.mention}")

    # Kick Command
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(ctx, user: discord.Member, *, reason="No reason provided."):
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
            await user.send(f'You have been kicked! \n __**Server:**__ {server} \n __**Reason:**__ {reason} \n __**Moderator:**__ {ctx.author.name}')   
            await user.kick(reason=reason)
            await ctx.message.delete()
            await ctx.channel.send(embed=kickem)

    # Invite Kick Command
    @commands.command()
    @has_permissions(manage_guild=True)
    async def invkick(ctx, user: discord.Member, *, reason="No reason given."):
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
        await ctx.send(embed=kickdem)

    # Ban Command
    @commands.command()
    @has_permissions(manage_guild=True)
    async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
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
            await user.send(f'You have been banned! \n __**Server:**__ {server} \n __**Reason:**__ {reason} \n __**Moderator:**__ {ctx.author.name}')
            await user.ban(reason=reason)
            await ctx.message.delete()
            await ctx.channel.send(embed=banem)

    # Unban Command
    @commands.command()
    @has_permissions(administrator=True)
    async def unban(ctx, id: int):
        user = await bot.fetch_user(id)
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
        await ctx.guild.unban(user)
        await ctx.send(embed=unbanem)

    ### Giveaway Commands Section###
    #------------------------------#

    # Event creation command
    @commands.command()
    async def eventcreate(ctx, arg1, arg2):
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
        newfield = eventembed.add_field(
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

        def check (reaction, user):
            return str(reaction.emoji) == '🥳' and user != bot.user
        
        while True:
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=2000000, check=check)
                msg = await ctx.fetch_message(message.id)
                
                global reactors
                reactors = []
                for reaction in msg.reactions:
                    if reaction.emoji == '🥳':
                        async for user in reaction.users():
                            if user != bot.user:
                                reactors.append(f'{user}')
                                eventembed.set_field_at(2, name="Entered:", value="```{}```".format('\n'.join(reactors)))
                                await message.edit(embed=eventembed)

            except asyncio.TimeoutError:
                await message.remove_reaction('🥳')
        

    @commands.command()
    @has_permissions(manage_messages=True)
    async def eventdel(ctx, messid):
        message = await ctx.fetch_message(id=messid)
        await message.delete()
        await ctx.send("Success! Event has been deleted.")
        
    @commands.command()
    @has_permissions()
    async def eventforce(ctx, messid):
        user = random.choice(reactors)
        message = await ctx.fetch_message(id=messid)
        await ctx.send(f"The winner is: {user}. Congratulations!!")
        eventembed.add_field(name="Winner:", value=f"Congratulations to {user}!", inline=False)
        await message.edit(embed=eventembed)
        await message.clear_reaction('🥳')

def setup(bot):
    bot.add_cog(commands(bot))
    print("Commands Extension loaded successfully")