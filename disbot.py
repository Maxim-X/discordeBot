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
async def ping(ctx):
    global summ
    summ+=1
    global user
    user = ctx.message.author
    await ctx.send('pong'+str(user))

@bot.command(pass_context= True)
async def myinfo(ctx, user: discord.User):
    await bot.say("Name: {}".format(user.name))

    

    
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))

