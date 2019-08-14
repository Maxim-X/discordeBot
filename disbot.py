import discord
from discord.ext import commands
import os
import logging

bot = commands.Bot(command_prefix='>')
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

summ = 1

@bot.command(pass_context= True)
async def hello(ctx):
    await ctx.send("Hello1 {}".format(ctx.message.author.mention))

@bot.command(pass_context= True)
async def myinfo(ctx, user: discord.User):
    await ctx.send("Name: {}".format(user.name))

    

    
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
