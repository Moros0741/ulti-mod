import os

import discord
from discord.ext import commands

startup_extensions = ["botcommands", "warningsysext"]

TOKEN = open('token.txt', 'r').read()
intent = discord.Intents.default(all)
bot = commands.Bot(command_prefix='?', intent=intent)
bot.remove_command('help')

@bot.event
async def on_connect():
    print("Signing into discord")
    print("Loading Commands extension")

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Type: ?help for commands list."))
    
@bot.command()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} turned on.".format(extension_name))

@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.send("{} turned off.".format(extension_name))

@bot.command()
async def reload(ctx, extension_name: str):
    bot.reload_extension(extension_name)
    await ctx.send(f"Extension: {extension_name}, has been successfully reactivated!")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(TOKEN)
