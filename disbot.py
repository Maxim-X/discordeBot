import discord
from discord.ext import commands
import os

Bot = commands.Bot(command_prefix='!')

@Bot.event
async def on_ready():
	print('Бот онлайн!')

@Bot.command(pass_context = True)
async def hello(ctx):
	await Bot.say("Hello!!!")

token = os.environ.get('BOT_TIKEN')
Bot.run(str(token))
