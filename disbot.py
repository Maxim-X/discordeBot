import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('NTcxMzUzNDI3NzI1MjU0NjU3.XVMNvQ.K1jIE0dq7mhc5zQfHWi8_qdaHqk')
