import discord
from discord.ext import commands
import os
import logging
import pyowm


bot = commands.Bot(command_prefix='>')
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

listBunMessage = ['сука', 'мат']
@bot.event
async def on_message(message):
	# print(message.content)
	# messageUser = message.content[:]
	# messageUser = messageUser.lower()
	# messageUser = messageUser.split()
	# print(messageUser)
	# if set(messageUser).intersection(set(listBunMessage)):
	for ig in listBunMessage:
		if ig in message.content:
			channel = message.channel
			userBan = message.author
			infoUserBan = discord.Embed(title= "Данное сообщение не прошло модерацию", colour= 0xf9d506, description='Оу Оу '+str(userBan)+', полегче.')
			infoUserBan.set_footer(text="Администрация осуждает данное высказывание.")
			await discord.Message.delete(message, delay=None)
			await channel.send(embed=infoUserBan)
	await bot.process_commands(message)



@bot.command(pass_context= True)
async def hello(ctx):
	await ctx.send("Привет, {}".format(ctx.message.author.mention))

@bot.command(pass_context= True)
async def myinfo(ctx, user: discord.User):
	InfoUserEmb = discord.Embed(title= "Title", colour= 0xFF00FF, description="werwer")
	InfoUserEmb.add_field(name = "Name", value= "Value")
	InfoUserEmb.set_thumbnail(url= user.avatar_url)
	InfoUserEmb.set_author(name= "Author", url= user.avatar_url)
	await ctx.send(embed = InfoUserEmb)

@bot.command(pass_context= True)
async def pogoda(ctx, city):
	owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')  # You MUST provide a valid API key
	observation = owm.weather_at_place(str(city))
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	await ctx.send("Погода в городе "+str(city)+": "+str(temp)+"℃")

@bot.command()
async def clean(ctx, TextChannel = discord.TextChannel):
	# messages = channel.history(limit=123).flatten()
	allMessageChanelList = []
	for message in channel.history(limit=200, oldest_first= True):
		allMessageChanelList.append(message)
	await ctx.send(allMessageChanelList)

    

    
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
