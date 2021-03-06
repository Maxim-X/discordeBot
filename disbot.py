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
from selenium import webdriver
import random
from discord.utils import get

from datetime import timedelta
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
import epic_mod
import time
bot = commands.Bot(command_prefix='>')
 
mainLoopStatus = False  # Variable which starts or stops the main loop
dataConfig = None  # Loaded configuration
langM = None

def chromeOpen():
	#--- Парсинг сайтов
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	#--- Парсинг сайтов

def EpicGamesFreeGame():
	global mainLoopStatus
	global dataConfig  # Gets config values
	global langM

	# await ctx.send(str(langM["start_success"]))

	# Here is where the real function starts

	mainLoopStatus = True  # Changes It to True so the main loop can start
	allNameGame = ""

	# Epic Games methods
	epic_mod.obj.make_request()
	epic_mod.obj.process_request()
	# print(epic_mod.obj.gameData)
	allGameInfo = epic_mod.obj.gameData
	if len(allGameInfo) == 1:
		embed=discord.Embed(title="Бесплатные игры в Epic Games | Store", description=f"Привет всем участникам канала!\nСейчас в магазине Epic Games | Store бесплатно раздается: ``{allGameInfo[0][0]}``\n\nДанная игра будет бесплатна до {allGameInfo[0][2]}, успей добавить ее в свою библиотеку!\n[Ссылка на игру]({allGameInfo[0][1]})", color=0xff7d25)
	else:
		# Собираем список игр
		for GameInfo in allGameInfo:
			if allNameGame != "":
				allNameGame = allNameGame+"`` "+GameInfo[0]+" ``\n"
			else:
				allNameGame = "`` "+GameInfo[0]+" ``\n"
		# Собираем список игр
		embed=discord.Embed(title="Бесплатные игры в Epic Games | Store", description=f"Привет всем участникам канала!\nСейчас в магазине Epic Games | Store бесплатно раздаются: {allNameGame}\nДанные игры будут бесплатны до {allGameInfo[0][2]}, успей добавить их в свою библиотеку!\n[Ссылка на игры](https://www.epicgames.com/store/ru/free-games)", color=0xff7d25)
	embed.set_image(url=allGameInfo[random.randint(0,len(allGameInfo)-1)][3])
	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	# print(str(ctx.channel.id))
	return embed
	
def sleepOneHours():
	todayNew = datetime.datetime.today()
	todayM = int(todayNew.strftime("%M"))
	sleepHOne = 3600 - (todayM * 60)
	return sleepHOne

@bot.command(pass_context= True)
async def time(ctx):
	today = datetime.datetime.today()
	await ctx.send(today.strftime("%H.%M.%S"))


# @bot.command(pass_context= True)
# async def check(ctx):
	
# 	caps = DesiredCapabilities().CHROME
# 	caps["pageLoadStrategy"] = "none" # interactive
# 	chrome_options = webdriver.ChromeOptions()
# 	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# 	chrome_options.add_argument("--headless")
# 	chrome_options.add_argument("--disable-dev-shm-usage")
# 	chrome_options.add_argument("--no-sandbox")
# 	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options,desired_capabilities=caps)
	

# 	driver.get('https://crackwatch.com/')
# 	await asyncio.sleep(8)
# 	viewGameImg = driver.find_elements_by_xpath("//div[@class='game-gallery-hot'] // div[@class='game-box'] // div[@class='image-box'] // img")

# 	viewGameStatus = driver.find_elements_by_xpath("//div[@class='game-gallery-hot'] // div[@class='game-box'] // div[@class='title-box']  // div[@class='sub-title'] // div[@class='inline-block'] // font")
# 	viewGameNameAndSrc = driver.find_elements_by_xpath("//div[@class='game-gallery-hot'] // div[@class='game-box'] // div[@class='title-box']  // div[@class='main-title main-title-cap'] // a")


# 	gameImg = viewGameImg[0].get_attribute('src')
# 	gameStatus = (viewGameStatus[0].text[: int(viewGameStatus[0].text.find('D+'))]).strip()
# 	gameTimeCrack = (viewGameStatus[0].text[int(viewGameStatus[0].text.find('D+')+2):]).strip()
# 	gameName = viewGameNameAndSrc[0].text
# 	gameSrc = viewGameNameAndSrc[0].get_attribute('href')
# 	print(gameImg)
# 	print(gameStatus)
# 	print(gameName)
# 	print(gameSrc)
# 	print(gameTimeCrack)

# 	if gameStatus != "CRACKED":
# 		driver.get(str(gameSrc))
# 		await asyncio.sleep(8)
# 		dataRelease = driver.find_elements_by_xpath("//div[@class='game-page-header-over'] // div[@class='grid'] // div[2] // div[@class='info-data']")
# 		gameTeamCrack = driver.find_elements_by_xpath("//div[@class='game-page-header-over'] // div[@class='grid'] // div[4] // div[@class='info-data']")
# 		gameTeamCrack = gameTeamCrack[0].text
# 		dataRelease = dataRelease[0].text
# 		print(dataRelease)
# 		today = datetime.datetime.today() - timedelta(hours=5)
		
# 		today = today.strftime("%b %d, %Y")
# 		print(today)
# 		#if dataRelease == str(today):
			
# 	else:
# 		print("Игра не взломана")
# 	driver.quit()
# 	embed=discord.Embed(title=f"Игра {gameName} взломана и доступна на торрентах", description=f"Сегодня команда ``{gameTeamCrack}``, успешно взломала игру ``{gameName}``.\n\nНа взлом этой команде понадобилось {gameTimeCrack} д.", color=0x89be5c)
	
# 	todayNew = datetime.datetime.today()
# 	embed.set_image(url=""+str(gameImg)+"")
# 	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
# 	await ctx.send(embed=embed)







@bot.command(pass_context= True)
async def pars(ctx):
	embed = EpicGamesFreeGame()
	await ctx.send(embed=embed)

@bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def parsInChannel(ctx, idChannel):
	embed = EpicGamesFreeGame()
	channel = bot.get_channel(int(idChannel))
	await channel.send(embed=embed) 

@bot.command(pass_context= True)
async def ds(ctx):
	global mainLoopStatus
	global dataConfig  # Gets config values
	global langM

	# await ctx.send(str(langM["start_success"]))

	# Here is where the real function starts

	mainLoopStatus = True  # Changes It to True so the main loop can start


	# Epic Games methods
	epic_mod.obj.make_request()
	epic_mod.obj.process_request()
	print(epic_mod.obj.gameData)
	await ctx.send(epic_mod.obj.gameData)


@bot.command(pass_context= True)
async def GamePlayGroundZakaz(ctx, *, url):
	# todayNew = datetime.datetime.today() 
	# todayH = int(todayNew.strftime("%H"))
	# todaym = int(todayNew.strftime("%M"))
	# if todayH + 5 < 24:
	# 	todayH = todayH + 5
	# else:
	# 	todayH = todayH + 5 - 24

	# driver = chromeOpen()
	channel = bot.get_channel(615296305144660008)
	# driver.get('https://www.playground.ru/news/')
	# pageListUrl = driver.find_element_by_xpath('//a[@class="item story-container"]')
	# pageGame = pageListUrl.get_attribute('href')
	# pageGame = str(url)
	# driver.get(pageGame)
	# nameNews = driver.find_element_by_xpath('//h1[@class="post-title"]')
	# nameNews = nameNews.text
	# imgNews = driver.find_element_by_xpath('//figure//img').get_attribute('src')
	# titleNews = driver.find_element_by_xpath('//div[@itemprop="articleBody"]/p')
	# titleNews = titleNews.text
	# driver.quit()
	# embed=discord.Embed(title=f"{nameNews}", description=f"{titleNews}\n\n[Читать далее...]({pageGame})", color=0x0078f2)
	# embed.set_image(url=""+str(imgNews)+"")
	# embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	await channel.send("123")
# Now you can start using Selenium


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


		
#ALL EVENTS ----------------------------------------

	

async def goodMorning():
	while not bot.is_closed():
		await bot.wait_until_ready()
		channel = bot.get_channel(619497569298546709)
		todayNew = datetime.datetime.today()
		todayH = int(todayNew.strftime("%H"))
		todaym = int(todayNew.strftime("%M"))
		if todayH + 5 < 24:
			todayH = todayH + 5
		else:
			todayH = todayH + 5 - 24

		if todayH == 9:
			driver = chromeOpen()
			driver.get('https://finewords.ru/sluchajnye-citaty')
			await asyncio.sleep(5)
			goodMornText = driver.find_elements_by_xpath("//p[starts-with(@id, 'sluchaino')]")
			goodMorningTextOk = goodMornText[0].text
			driver.quit()
			todayWeekDay = str(todayNew.strftime("%A"))

			
			if todayWeekDay != 'Saturday' and todayWeekDay != 'Sunday':
				embed=discord.Embed(title="Доброе утро!", description=""+str(goodMorningTextOk)+"\n Свежий выпуск игровых новостей ждет вас чуть ниже, удачи!", color=0xfaff22)
				embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/21/mountain.png')
				embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
				await channel.send(embed=embed)
				#--- Парсинг сайтов
				chrome_options = webdriver.ChromeOptions()
				chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
				chrome_options.add_argument("--headless")
				chrome_options.add_argument("--disable-dev-shm-usage")
				chrome_options.add_argument("--no-sandbox")
				driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
				#--- Парсинг сайтов
				driver.get('https://www.youtube.com/playlist?list=PLZfhqd1-Hl3CHweF-pR0c0zFveLB-HSWw')
				pageListUrl = driver.find_element_by_xpath('//ytd-playlist-thumbnail/a').get_attribute("href")
				driver.quit()
				await channel.send(str(pageListUrl))
			else:
				embed=discord.Embed(title="Доброе утро!", description=""+str(goodMorningTextOk)+"", color=0xfaff22)
				embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/21/mountain.png')
				embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
				await channel.send(embed=embed)

			sleepHOne = 3600 - (todaym * 60)
			await asyncio.sleep(int(sleepHOne)) #3600
		else:
			sleepHOne = 3600 - (todaym * 60)
			await asyncio.sleep(int(sleepHOne)) #3600

async def freeGameEpic():
	while not bot.is_closed():
		await bot.wait_until_ready()
		# channel = bot.get_channel(412939700748419086) #615296305144660008
		todayNew = datetime.datetime.today()
		todayWeekDay = str(todayNew.strftime("%A"))
		todayH = int(todayNew.strftime("%H"))
		todayM = int(todayNew.strftime("%M"))
		if todayH + 5 < 24:
			todayH = todayH + 5
		else:
			todayH = todayH + 5 - 24

		if todayWeekDay == 'Friday' or todayWeekDay == 'Wednesday':

			if todayH == 18 and todayM == 0:
				embed = EpicGamesFreeGame()
				for Guild in bot.guilds:
					channel = bot.get_channel(Guild.system_channel.id)
				await channel.send(embed=embed)

				# todayNew = datetime.datetime.today()
				# todayM = int(todayNew.strftime("%M"))
				# sleepHOne = 3600 - (todayM * 60)
				# await channel.send('Сплю: '+str(sleepHOne)+' секунд')
				await asyncio.sleep(int(sleepOneHours()))
			else:
				# todayNew = datetime.datetime.today()
				# todayM = int(todayNew.strftime("%M"))
				# sleepHOne = 3600 - (todayM * 60)
				await asyncio.sleep(int(sleepOneHours()))
				
		else:
			# todayNew = datetime.datetime.today()
			# todayM = int(todayNew.strftime("%M"))
			# sleepHOne = 3600 - (todayM * 60)
			await asyncio.sleep(int(sleepOneHours()))

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(412939700748419086)
	embed=discord.Embed(title="Пользователь ``"+str(member.display_name)+"`` присоединился к нашему серверу.", description="Добро пожаловать! Располагайся, чувствуй себя как дома.\nФура достойных каток и интересных тимейтов уже выехала.", color=0x5458bc)
	embed.set_thumbnail(url=''+str(member.avatar_url)+'')
	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	await channel.send(embed=embed)
	await member.add_roles(discord.utils.get(member.guild.roles, name='Новичок'))

@bot.event
async def on_message(message):
	randIntOtvMessage = random.randint(0,100)
	if randIntOtvMessage == 0 and message.author.display_name != "Maxim" and not message.author.bot:
		await asyncio.sleep(4)
		massAllOtvMessage = ['https://media.giphy.com/media/YWWeEeFThzFS6VKmyX/giphy.gif','https://media.giphy.com/media/2Y7lZAxlutI5MuVEzb/giphy.gif','https://media.giphy.com/media/a5viI92PAF89q/giphy.gif','https://media.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif','https://media.giphy.com/media/FxEwsOF1D79za/giphy.gif','https://media.giphy.com/media/Lcn0yF1RcLANG/giphy.gif','https://media.giphy.com/media/uHox9Jm5TyTPa/giphy.gif', 'https://media.giphy.com/media/s8Aix99cRIwyk/giphy.gif', 'https://media.giphy.com/media/5h9AIbcxZospnLbmbl/giphy.gif','https://media.giphy.com/media/3LugygiVMlZDXTakyb/giphy.gif','https://media.giphy.com/media/oOxBQwNqGwxeWLDF6A/giphy.gif','https://media.giphy.com/media/5hs5eKmprnJK5hTVGq/giphy.gif','https://media.giphy.com/media/tRzd704xXId2w/giphy.gif']
		imgGif = random.choice(massAllOtvMessage)
		await message.channel.send(message.author.mention)
		await message.channel.send(str(imgGif))

	await bot.process_commands(message)

@bot.event
async def on_message(message):
	await bot.process_commands(message)


# @bot.event
# async def on_member_update(before, after):
# 	print('1')
# 	# Пользователь начал играть
# 	if after.activity != None:
# 		if before.activity != None:
# 			oldGameStatus = before.activity.name
# 		else:
# 			oldGameStatus = ''
# 		newGameStatus = after.activity.name
# 	# Пользователь начал играть


# 	for guild in bot.guilds:
# 		if str(guild.id) == '412939700748419084' and not after.bot:
# 			gameTeam = False
# 			for channel in guild.channels:
# 				if after.activity != None:
# 					if str(channel.type) == 'voice':
# 						NameVoiceChannel = channel.name
# 						for user in channel.members:
# 							if str(user.display_name) == str(after.display_name):
# 								allGameUser = []
# 								for user in channel.members:
# 									if user.activity != None:
# 										if str(user.activity.name) == str(newGameStatus):
# 											allGameUser.append(str(user.display_name))
# 								if len(allGameUser) >= 2:
# 									gameTeam = True
# 									allGameUser1 = ' , '.join(allGameUser)
# 									print(allGameUser1)
# 									nameChannelV = str(channel.name)
# 								else:
# 									gameTeam = False


# 			for channel in guild.channels:
# 				print("-----------"+str(channel.name)+" : "+str(channel.type))
# 				if str(channel.id) == '619497569298546709':
# 				# print("-===="+str(channel.name))
# 					if after.activity != None:
# 						if gameTeam:
# 							embed=discord.Embed(title="Пользователи "+str(allGameUser1)+" играют в `"+str(newGameStatus)+"`", description="Если вы хотите присоединиться, заходите в голосовой канал "+str(nameChannelV)+"", color=0xed5565)
# 							embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/19/gamepad.png')
# 							embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
# 							await channel.send(embed=embed)
# 					if after.activity != None:
# 						if oldGameStatus != newGameStatus and not gameTeam:
# 							embed=discord.Embed(title="Пользователь "+str(after.display_name)+" запустил игру\n`"+str(newGameStatus)+"`", description="У вас есть шанс взять в свою команду скилового игрока.\n``(Данное сообщение удалится через 60 минут)``", color=0xed5565)
# 							embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/19/gamepad.png')
# 							embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
# 							await channel.send(embed=embed, delete_after=60*60)
# 						# / Пользователь начал играть

# 						# / Пользователь получил новую роль
# 					roleADD=list(set(after.roles) - set(before.roles))
# 					roleDELL=list(set(before.roles) - set(after.roles))
# 					if len(roleADD) >= 1:
# 						if str(after.display_name) != str(roleADD[0]):
# 							embed=discord.Embed(title="Пользователь "+str(after.display_name)+" получил новую роль `"+str(roleADD[0])+"`", description="Носи данный знак с честью или сразу считай его клеймом.\n``(Данное сообщение удалится через 85 минут)``", color=0x26b99a)
# 							embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/19/id-card.png')
# 							embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
# 							await channel.send(embed=embed, delete_after=60*85)
# 					elif len(roleDELL) >= 1:
# 						if str(after.display_name) != str(roleDELL[0]):
# 							embed=discord.Embed(title="Пользователь "+str(after.display_name)+" лишился своей роли `"+str(roleDELL[0])+"`", description="Тут и добавить то нечего.\n``(Данное сообщение удалится через 85 минут)``", color=0x26b99a)
# 							embed.set_thumbnail(url='https://fotohosting.su/images/2019/08/19/id-card.png')
# 							embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
# 							await channel.send(embed=embed, delete_after=60*85)
							# / Пользователь получил новую роль



#ALL EVENTS ----------------------------------------



@bot.command(pass_context= True)
async def hello(ctx):
	await ctx.send("Привет, {}".format(ctx.message.author.mention))

@bot.command(pass_context= True)
async def mem(ctx):
	driver = chromeOpen()
	driver.get('https://admem.ru/rndm')
	imgMem = driver.find_element_by_xpath('//div[@class="post"]//img')
	imgMemSrc = imgMem.get_attribute('src')
	driver.quit()
	embed=discord.Embed(title="Рандомный мем!", colour= 0x4281f4, description="За качество не ручаюсь, я все же бот а не Джордж Карлин.")
	embed.set_image(url=str(imgMemSrc))
	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	await ctx.send(embed=embed)


# @bot.command(pass_context= True)
# async def addBanMessage(ctx, *, word):
# 	allword = word.split( )
# 	allword = len(allword)
# 	if allword == 1:
# 		await ctx.send("Я тебя понял, сча все будет!")
# 		text_file=open("listBunMessage.txt", "r", encoding="utf-8")
# 		allBanMessage = text_file.readlines()
# 		text_file.close()
# 		text_file=open("listBunMessage.txt", "w", encoding="utf-8")
# 		allBanMessage+=str(word)+"\n"
# 		await ctx.send(str(allBanMessage))
# 		text_file.writelines(allBanMessage)
# 		text_file.close()
# 		author = ctx.message.author
# 		infoUser = discord.Embed(title= "Слово `"+str(word)+"` добавлено в список запрещенных слов.", colour= 0xf9d506, description=""+str(author)+" спасибо за то что внес вклад в мое развитие!")
# 		await ctx.send(embed=infoUser)
# 	else:
# 		await ctx.send("Чтобы добавить слово в список запрещенных нужно указать только одно слово. \nДанное правило `Максим` разработал чтобы исключить вырывание слов из контекста.")

@bot.command(pass_context= True)
async def sendMessage(ctx,*, title):
	name = ''
	on = False
	for x in title:
		if str(x) == ')':
			on = False
		if on:
			name += str(x) 
		if str(x) == '(':
			on = True
	words = ("(", ")")
	titleText = title[:title.find(words[0]) + len(words[0])] + title[title.find(words[1]):]
	titleText = titleText.replace('(','').replace(')','')
	wordsImg = ("<img>", "</img>")
	Img = re.findall(r'<img>(.*?)</img>',titleText)
	titleText = titleText[:titleText.find(wordsImg[0]) + len(wordsImg[0])] + titleText[titleText.find(wordsImg[1]):]
	titleText = titleText.replace('<img>','').replace('</img>','')
	embed = discord.Embed(title= ""+name+"", colour= 0x6c82cb, description= ""+titleText+"")
	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	embed.set_image(url=""+str(Img[0])+"")
	await ctx.message.delete()
	await ctx.send(embed=embed)

@bot.command(pass_context= True)
async def sendMessageNews(ctx,*, title):
	name = ''
	on = False
	for x in title:
		if str(x) == ')':
			on = False
		if on:
			name += str(x) 
		if str(x) == '(':
			on = True
	words = ("(", ")")
	titleText = title[:title.find(words[0]) + len(words[0])] + title[title.find(words[1]):]
	titleText = titleText.replace('(','').replace(')','')
	wordsImg = ("<img>", "</img>")
	Img = re.findall(r'<img>(.*?)</img>',titleText)
	titleText = titleText[:titleText.find(wordsImg[0]) + len(wordsImg[0])] + titleText[titleText.find(wordsImg[1]):]
	titleText = titleText.replace('<img>','').replace('</img>','')
	embed = discord.Embed(title= ""+name+"", colour= 0x6c82cb, description= ""+titleText+"")
	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	embed.set_image(url=""+str(Img[0])+"")
	channel = bot.get_channel(412939700748419086)
	await ctx.message.delete()
	await channel.send(embed=embed)


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

# @bot.command()
# async def clean(ctx, TextChannel = discord.TextChannel):
# 	# messages = channel.history(limit=123).flatten()
# 	allMessageChanelList = []
# 	for message in channel.history(limit=200, oldest_first= True):
# 		allMessageChanelList.append(message)
# 	await ctx.send(allMessageChanelList)

 

@bot.command(pass_context=True)
async def cleanChat(ctx, allNumMessage):
	levelProtect = 0
	for xRole in ctx.author.roles:
		if str(xRole) == 'Яндекс.Уборщик' and levelProtect != 2:
			levelProtect = 1
		if str(xRole) == 'МАКСИМ':
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
# bot.bg_task = bot.loop.create_task(goodMorning())
bot.bg_task = bot.loop.create_task(freeGameEpic())
# bot.bg_task = bot.loop.create_task(checkCrackGame())
# bot.bg_task = bot.loop.create_task(newsGamePlayGround())
# bot.bg_task = bot.loop.create_task(deleteVoiceChannel())
bot.run(str(token))

