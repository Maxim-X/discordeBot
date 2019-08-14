import discord
from discord.ext import commands
import os
import logging

bot = commands.Bot(command_prefix='>')

summ = 1

@bot.command()
async def ping(ctx1):
    global summ
    summ+=1
    await ctx.send('pong'+str(summ))

    
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
    
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
