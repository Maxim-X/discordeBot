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


# @bot.command()
# async def ddda(ctx):
# 	while(1==1):
# 		todayNew = datetime.datetime.today()
# 		todayH = int(todayNew.strftime("%H"))
# 		todaym = int(todayNew.strftime("%M"))
# 		if todayH + 5 < 24:
# 			todayH = todayH + 5
# 		else:
# 			todayH = todayH + 5 - 24

# 		if todayH == 10 :
# 			embed=discord.Embed(title="Доброе утрой!", description="Вот свежий выпуск игровых новостей:", color=0xfaff22)
# 			embed.set_thumbnail(url='https://s8.hostingkartinok.com/uploads/images/2019/08/3fe82fae8fb064fecf28ca34a3f1ec38.png')
# 			embed.set_footer(text="Стремитесь не к успеху, а к ценностям, которые он дает​.")
# 			await ctx.send(embed=embed)
# 			await ctx.send('https://www.youtube.com/watch?v=JR5staaSWdc&list=PLZfhqd1-Hl3CHweF-pR0c0zFveLB-HSWw')
# 			await asyncio.sleep(86400) #82800
# 		else:
# 			sleepHOne = 3600 - (todaym * 60)
# 			await asyncio.sleep(int(sleepHOne)) #3600

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


		
#ALL EVENTS ----------------------------------------

	

async def goodMorning():
	while not bot.is_closed():
		await bot.wait_until_ready()
		channel = bot.get_channel(610541252160651269)
		todayNew = datetime.datetime.today()
		todayH = int(todayNew.strftime("%H"))
		todaym = int(todayNew.strftime("%M"))
		if todayH + 5 < 24:
			todayH = todayH + 5
		else:
			todayH = todayH + 5 - 24

		if todayH == 9:
			embed=discord.Embed(title="Доброе утрой!", description="Вот свежий выпуск игровых новостей:\nСтремитесь не к успеху, а к ценностям, которые он дает​.", color=0xfaff22)
			embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/21/mountain.png')
			embed.set_footer(text="Сервер")
			await channel.send(embed=embed)
			await channel.send('https://www.youtube.com/watch?v=JR5staaSWdc&list=PLZfhqd1-Hl3CHweF-pR0c0zFveLB-HSWw')
			await asyncio.sleep(86400) #82800
		else:
			sleepHOne = 3600 - (todaym * 60)
			await asyncio.sleep(int(sleepHOne)) #3600

async def freeGameEpic():
	print('--------')
	while not bot.is_closed():
		await bot.wait_until_ready()
		print('0')
		channel = bot.get_channel(610541252160651269)
		print('0')
		todayNew = datetime.datetime.today()
		print('0')
		todayWeekDay = str(todayNew.strftime("%A"))
		print('0')
		todayH = int(todayNew.strftime("%H"))
		print('1')
		print('1')
		print(str(todayH))
		if todayH + 5 < 24:
			todayH = todayH + 5
		else:
			todayH = todayH + 5 - 24
		print(str(todayH))
		if todayWeekDay == 'Wednesday':
			print('2')
			if todayH >= 19:
				print('3')
				url= "https://www.epicgames.com/store/ru/collection/free-game-collection"
				r=requests.get(url).text
				soup = BeautifulSoup(r, "lxml")
				pageFree = soup.find('div',{'class':'StoreRow-wrapper_32933b82'})
				# print(str(pageFree))

				soupPage = BeautifulSoup(str(pageFree), "lxml")
				AllNameGameNew=''
				AllPageFree = soupPage.findAll('h3')
				AllNameGame = []
				AllGameImg = []
				AllGameCena = []
				GameAllCena=[]
				for NameGame in AllPageFree:
					AllNameGame.append("``"+str(NameGame.contents).replace("['","").replace("']","")+"``")
					AllGameImg.append(soupPage.find('img',{'alt':''+str(NameGame.contents).replace("['","").replace("']","")+''}))
				AllGameCena = soupPage.findAll('s') 
				# for NameGameC in AllGameCena:
				# 	print(str(NameGameC.contents))
				# 	GameAllCena.append(""+str(NameGameC.contents).replace("['","").replace("']","").replace("\\xa0","").replace("'","").replace(",00","").replace("₽","").replace("$","").replace(",",".")+"")
				# if float(GameAllCena[0]) >= float(GameAllCena[1]):
				# 	ImgGameId = 0
				# 	GameImgAll = soupPage.findAll('img', {'src':re.compile('^http')}) 
				# 	ImgGame = GameImgAll[ImgGameId].get('src')
				# else:
				# 	ImgGameId = 1
				# 	GameImgAll = soupPage.findAll('img', {'src':re.compile('^http')})
				# 	ImgGame = GameImgAll[ImgGameId].get('src')
				# payCenaGame = float(GameAllCena[0]) + float(GameAllCena[1])
				if len(AllNameGame) >= 2:
					AllNameGameNew = ' и '.join(AllNameGame)
				embed=discord.Embed(title="Привет всем участникам канала!", description="Сейчас в магазине EpicGames бесплатно раздается: "+str(AllNameGameNew)+"\n\nДанные игры бесплатны до "+str('12 сент')+"", color=0x0078f2)
				embed.set_thumbnail(url="https://image.prntscr.com/image/fpuKs8vaRiiA_Xc6eE742Q.png")
				embed.set_footer(text="Сервер")
				await channel.send(embed=embed)
				# await channel.send(str(ImgGame))
				await channel.send('https://www.epicgames.com/store/ru/collection/free-game-collection')
				await channel.send('1')
				await channel.send('Сплю: 604800 секунд')
				await asyncio.sleep(604800)
				# await ctx.send(AllGameImgNew)
			else:
				print('4')
				todayM = int(todayNew.strftime("%M"))
				sleepHOne = 3600 - (todayM * 60)
				await channel.send('Сплю: '+str(sleepHOne)+' секунд')
				await asyncio.sleep(int(sleepHOne))
		else:
			todayM = int(todayNew.strftime("%M"))
			sleepHOne = 3600 - (todayM * 60)
			sleepHOne += (86400 - (todayH * 60 * 60))
			await channel.send('Сплю: '+sleepHOne+' секунд')
			await asyncio.sleep(int(sleepHOne))


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


@bot.event
async def on_member_update(before, after):
	for guild in bot.guilds:
		print(str(guild))
		for channel in guild.channels:
			if str(channel) == 'основной':

				# Пользователь начал играть
				if after.activity != None:
					if before.activity != None:
						oldGameStatus = before.activity.name
					else:
						oldGameStatus = ''
					newGameStatus = after.activity.name
					if oldGameStatus != newGameStatus:
						embed=discord.Embed(title="Пользователь "+str(after.display_name)+" запустил игру\n`"+str(newGameStatus)+"`", description="У вас есть шанс взять в свою команду скилового игрока.\n``(Данное сообщени удалится через 15 минут)``", color=0xed5565)
						embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/19/gamepad.png')
						embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
						await channel.send(embed=embed, delete_after=60*15)
				# / Пользователь начал играть

				# / Пользователь получил новую роль
				roleADD=list(set(after.roles) - set(before.roles))
				roleDELL=list(set(before.roles) - set(after.roles))
				if len(roleADD) >= 1:
					embed=discord.Embed(title="Пользователь "+str(after.display_name)+" получил новую роль `"+str(roleADD[0])+"`", description="Носи данный знак с честью или сразу считай его клеймом.\n``(Данное сообщени удалится через 5 минут)``", color=0x26b99a)
					embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/19/id-card.png')
					embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
					await channel.send(embed=embed, delete_after=60*5)
				elif len(roleDELL) >= 1:
					embed=discord.Embed(title="Пользователь "+str(after.display_name)+" лишился своей роли `"+str(roleDELL[0])+"`", description="Тут и добавить то нечего.\n``(Данное сообщени удалится через 5 минут)``", color=0x26b99a)
					embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/19/id-card.png')
					embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
					await channel.send(embed=embed, delete_after=60*5)
				# / Пользователь получил новую роль



#ALL EVENTS ----------------------------------------


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

 

@bot.command(pass_context=True)
async def cleanChat(ctx, allNumMessage):
	levelProtect = 0
	for xRole in ctx.author.roles:
		if str(xRole) == 'Яндекс.Уборщик' and levelProtect != 2:
			levelProtect = 1
		if str(xRole) == 'Максим':
			levelProtect = 2

	if levelProtect == 2:
		await ctx.channel.purge(limit=int(allNumMessage))
	elif levelProtect == 1:
		if int(allNumMessage) <= 10:
			await ctx.channel.purge(limit=int(allNumMessage))
		else:
			await ctx.send('Пользователь со статусом `Яндекс.Уборщик` может удалить до 10 сообщений за раз.\nЕсли вы хотите очистить чат полностью обратитесь к `Maxim`')
	else:
		await ctx.send("Пользователь без статуса `Яндекс.Уборщик` не может массово удалять сообщения.")

    
token = os.environ.get('BOT_TOKEN')
bot.bg_task = bot.loop.create_task(goodMorning())
bot.bg_task = bot.loop.create_task(freeGameEpic())
bot.run(str(token))

