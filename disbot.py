import discord
from discord.ext import commands
import os
import logging
import pyowm
import pymysql
from pymysql.cursors import DictCursor
import pymysql.cursors
import requests
from bs4 import BeautifulSoup
import re
import lxml
import datetime
import asyncio

bot = commands.Bot(command_prefix='>')
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

listBunMessage = ['сука', 'мат', 'уебак']
i=0
while i < len(listBunMessage):
	listBunMessage[i] = listBunMessage[i].lower()
	i+=1


@bot.command(pass_context= True)
async def time(ctx):
	today = datetime.datetime.today()
	await ctx.send(today.strftime("%H.%M.%S"))

# @bot.command(pass_context= True)
# async def pars(ctx):
# 	#Расписание
# 	url= "https://www.youtube.com/playlist?list=PLZfhqd1-Hl3CHweF-pR0c0zFveLB-HSWw"
# 	r=requests.get(url).text
# 	soup = BeautifulSoup(r, "lxml")

# 	# time = datetime.datetime.today().strftime("%d")
# 	# timenext = datetime.datetime.today().strftime("%d")

# 	pagerasp = soup.find('a').get('href')
# 	await ctx.send(str(pagerasp))

@bot.command()
async def ddda(ctx):
	todayNew = datetime.datetime.today()
	todayH = int(todayNew.strftime("%H"))
	todaym = int(todayNew.strftime("%M"))
	await ctx.send(str(todayH))
	await ctx.send(str(todaym))
	while(1==1):
		todayNew = datetime.datetime.today()
		todayH = int(todayNew.strftime("%H"))
		todaym = int(todayNew.strftime("%M"))
		if todayH == 4 :
			embed=discord.Embed(title="Доброе утрой!", description="Вот свежий выпуск игровых новостей:", color=0xfaff22)
			embed.set_footer(text="Стремитесь не к успеху, а к ценностям, которые он дает​.")
			await ctx.send(embed=embed)
			await ctx.send('https://www.youtube.com/watch?v=JR5staaSWdc&list=PLZfhqd1-Hl3CHweF-pR0c0zFveLB-HSWw')
			await asyncio.sleep(86400) #82800
		else:
			sleepHOne = 3600 - (todaym * 60)
			await asyncio.sleep(int(sleepHOne)) #3600

@bot.command(pass_context= True)
async def db(ctx):
	connection = pymysql.connect(
		host='localhost',
		user='id4459149_cls222221_bd',
		password='1a7L2orZMs0bR',
		db='id4459149_cl22s2221_bd',
		charset='utf8mb4',
		cursorclass=DictCursor
	)
	try:
		with connection.cursor() as cursor:
			sql1 = "INSERT INTO db_allBanMessage (message) VALUES (%s);"
			cursor.execute(sql1,('Merly'))
			connection.commit()
	finally:
		connection.close()


		
@bot.command(pass_context= True)
async def rede(ctx): 
	text_file=open("listBunMessage.txt", "r", encoding="utf-8")
	# text_file.writelines(lines)
	allBanMessage = text_file.readlines()
	text_file.close()
	await ctx.send(str(allBanMessage))


@bot.event
async def on_message(message):
	# print(message.content)
	messageUser = message.content[:]
	messageUser = messageUser.lower()
	messageUser = messageUser.split()
	# print(messageUser)
	# if set(messageUser).intersection(set(listBunMessage)):
	for ig in listBunMessage:
		if ig in messageUser:
			channel = message.channel
			userBan = message.author
			infoUserBan = discord.Embed(title= "Данное сообщение не прошло модерацию", colour= 0xf9d506, description=''+str(userBan)+', если хочешь использовать мат, заходи в голосовой чат.')
			infoUserBan.set_footer(text="Администрация осуждает данное высказывание. `© Maxim`")
			await discord.Message.delete(message, delay=None)
			await channel.send(embed=infoUserBan)
	await bot.process_commands(message)



@bot.command(pass_context= True)
async def hello(ctx):
	await ctx.send("Привет, {}".format(ctx.message.author.mention))

@bot.command(pass_context= True)
async def addBanMessage(ctx, *, word):
	allword = word.split( )
	allword = len(allword)
	if allword == 1:
		await ctx.send("Я тебя понял, сча все будет!")
		text_file=open("listBunMessage.txt", "r", encoding="utf-8")
		allBanMessage = text_file.readlines()
		text_file.close()
		text_file=open("listBunMessage.txt", "w", encoding="utf-8")
		allBanMessage+=str(word)+"\n"
		await ctx.send(str(allBanMessage))
		text_file.writelines(allBanMessage)
		text_file.close()
		author = ctx.message.author
		infoUser = discord.Embed(title= "Слово `"+str(word)+"` добавлено в список запрещенных слов.", colour= 0xf9d506, description=""+str(author)+" спасибо за то что внес вклад в мое развитие!")
		await ctx.send(embed=infoUser)
	else:
		await ctx.send("Чтобы добавить слово в список запрещенных нужно указать только одно слово. \nДанное правило `Максим` разработал чтобы исключить вырывание слов из контекста.")



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
