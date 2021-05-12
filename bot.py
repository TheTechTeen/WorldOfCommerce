from discord.ext import commands

from world import World

bot = commands.Bot(command_prefix="!")

@bot.command(name="ping")
async def pingpong(ctx):
    await ctx.send("PONG!")


@bot.command(name="prefix")
async def prefix(ctx, new_prefix):
    bot.command_prefix = new_prefix
    print("Set prefix to " + new_prefix)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print("Connected to " + guild.name)