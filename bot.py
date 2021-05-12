from discord.ext import commands

from world import World

bot = commands.Bot(command_prefix="!")

@bot.command(name="ping")
async def pingpong(ctx):
    await ctx.send("PONG!")

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print("Connected to " + guild.name)