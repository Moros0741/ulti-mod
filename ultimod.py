
import os

import discord
from discord.ext import commands, tasks
import sqlite3
from itertools import cycle

intents = discord.Intents.all()
startup_extensions = ["commandext", "welcome"]
default_prefix = '?'

def set_prefix(bot, message):
    guild = message.guild
    db = sqlite3.connect('ultidb.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT prefix FROM guild_config WHERE guild_id = ?", (guild.id,))
    result = cursor.fetchone()
    if result is not None:
        return str(result[0][0])
    elif result is None:
        sql = ("INSERT INTO guild_config(guild_id, prefix) VALUES(?,?)")
        val = (guild.id, default_prefix)
        cursor.execute(sql, val)
        db.commit()

TOKEN = open('token.txt', 'r').read()
bot = commands.Bot(command_prefix=set_prefix, intents=intents, chunk_guilds_at_startup = False)
status = cycle(["Server Protection System", "?help for commands", "?support | Join support", "?bug | Report a Bug"])

global Moros, Rach, Vexy
Moros = 700057705951395921
Rach = 765324522676682803
Vexy = 709576853337407529

@bot.event
async def on_connect():
    print("Signing into discord")
    print("Loading Commands extension")

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    await change_stats.start(bot)
    
@tasks.loop(seconds=25)
async def change_stats(bot):
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.command() #Loads an extension
async def load(ctx, extension_name : str):
    try:
        if ctx.author.id == Vexy or ctx.author.id == Rach or ctx.author.id == Moros:
            bot.load_extension(extension_name)
            await ctx.send("{} {} has been turned on.".format(ctx.author.mention, extension_name))
        else:
            await ctx.send(f'ERROR! {ctx.author.mention} You do no have permissions to use this command!')
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return

@bot.command() #Unload an extension
async def unload(ctx, extension_name : str):
    if ctx.author.id == Vexy or ctx.author.id == Rach or ctx.author.id == Moros:
        bot.unload_extension(extension_name)
        await ctx.send("{} {} has been turned off.".format(ctx.author.mention, extension_name))
    else:
        await ctx.send(f'ERROR! {ctx.author.mention} You do no have permissions to use this command!')


@bot.command() #Reloads an extension
async def reload(ctx, extension_name: str):
    if ctx.author.id == Vexy or ctx.author.id == Rach or ctx.author.id == Moros:
        bot.reload_extension(extension_name)
        await ctx.send("{} {} has been restarted.".format(ctx.author.mention, extension_name))
    else:
        await ctx.send(f'ERROR! {ctx.author.mention} You do no have permissions to use this command!')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(TOKEN)
