import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>')

summ = 1

@bot.command()
async def ping(ctx):
    await ctx.send('pong'+summ)
    summ+=1

    
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
