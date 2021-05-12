from discord.ext import commands
import discord

from world import World

bot = commands.Bot(command_prefix="!")

@bot.command(name="ping")
async def pingpong(ctx):
    await ctx.send("PONG!")


@bot.command(name="prefix")
async def prefix(ctx, new_prefix):
    bot.command_prefix = new_prefix
    print("Set prefix to " + bot.command_prefix)
    await bot.change_presence(activity=discord.Game(name="Prefix is "+bot.command_prefix))

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print("Connected to " + guild.name)
    await bot.change_presence(activity=discord.Game(name="Prefix is "+bot.command_prefix))