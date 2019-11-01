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
bot = commands.Bot(command_prefix='>')
 


def chromeOpen():
	#--- Парсинг сайтов
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	#--- Парсинг сайтов

@bot.command(pass_context= True)
async def time(ctx):
	today = datetime.datetime.today()
	await ctx.send(today.strftime("%H.%M.%S"))


# async def newsGamePlayGround():
# 	while not bot.is_closed():
# 		await bot.wait_until_ready()
# 		todayNew = datetime.datetime.today()
# 		todayH = int(todayNew.strftime("%H"))
# 		todaym = int(todayNew.strftime("%M"))
# 		if todayH + 5 < 24:
# 			todayH = todayH + 5
# 		else:
# 			todayH = todayH + 5 - 24 

# 		if todayH == 14 or todayH == 15 or todayH == 18 or todayH == 19:
# 			if todaym <= 5:
# 				timeSleep = random.randint(60, 120)
# 				print('Сплю: '+str(timeSleep)+' секунд')
# 				await asyncio.sleep(int(timeSleep))
# 				driver = chromeOpen()
# 				channel = bot.get_channel(619497569298546709)
# 				print('---1---')
# 				driver.get('https://www.playground.ru/news/')
# 				print('---1---')
# 				pageListUrl = driver.find_element_by_xpath('//article[@class="post"]// h3[@class="post-title"] //a')
# 				print('---1---')
# 				pageGame = pageListUrl.get_attribute('href')
# 				print('Ссылка:' +str(pageGame))
# 				print('---1---')
# 				driver.get(str(pageGame))
# 				print('---1---')
# 				nameNews = driver.find_element_by_xpath('//h1[@class="post-title"]')
# 				print('---1---')
# 				nameNews = nameNews.text
# 				print('---1---')
# 				imgNews = driver.find_element_by_xpath('//figure//img').get_attribute('src')
# 				print('---1---')
# 				titleNews = driver.find_element_by_xpath('//div[@itemprop="articleBody"]/p')
# 				print('---1---')
# 				titleNews = titleNews.text
# 				print('---1---')
# 				driver.quit()
# 				print('---1---')
# 				embed=discord.Embed(title=f"{nameNews}", description=f"{titleNews}\n\n[Читать далее...]({pageGame})", color=0x0078f2)
# 				print('---1---')
# 				embed.set_image(url=""+str(imgNews)+"")
# 				print('---1---')
# 				embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
# 				print('---1---')
# 				await channel.send(embed=embed)
# 				print('---1---')
# 			todayNew = datetime.datetime.today()
# 			todayM = int(todayNew.strftime("%M")) 
# 			sleepHOne = 3600 - (todayM * 60)
# 			await asyncio.sleep(int(sleepHOne)) #3600
# 		else:
# 			todayNew = datetime.datetime.today()
# 			todayM = int(todayNew.strftime("%M"))
# 			sleepHOne = 3600 - (todayM * 60)
# 			# await channel.send('Сплю: '+str(sleepHOne)+' секунд')
# 			await asyncio.sleep(int(sleepHOne))

@bot.command(pass_context= True)
async def pars(ctx):
	await ctx.message.delete()
	await bot.wait_until_ready()
	channel = bot.get_channel(615296305144660008)#412939700748419086
	driver = chromeOpen()
	driver.get('https://www.epicgames.com/store/ru/')
	# assert 'Yahoo' in browser.title

	# elem = browser.find_element_by_name('p')  # Find the search box
	# elem.send_keys('seleniumhq' + Keys.RETURN)
	# time.sleep(5)
	await asyncio.sleep(5)
	login_formAllSection = driver.find_elements_by_xpath("//*[starts-with(@class, 'Discover-section_')]")

	print("\t 1----- "+ str(login_formAllSection[2].text)+"\n\n")
	login_form = login_formAllSection[2];
	print("\t 2----- "+str(login_form.text)+"\n\n")
	login_form = login_form.find_elements_by_xpath("./*[starts-with(@class, 'CardGrid-card')]")
	#print("\t 3----- "+str(login_form.text)+"\n\n")
	nameGame = login_form[0].find_elements_by_xpath("//*[starts-with(@class, 'Card-title_')]")
	nameGameOk = nameGame[0].text

	for ind, ddd in enumerate(login_form):
		print("\t "+ ddd.text+" ["+str(ind)+"]")
	if nameGameOk != 'Бесплатные игры':
		allImgGame = login_form[0].find_elements_by_xpath("//*[starts-with(@class, 'Picture-image')]")
		ImgGame = allImgGame[0].get_attribute("src")
		allTime = login_form[0].find_elements_by_xpath("//time")
		allUrlGame = login_form[0].find_elements_by_xpath("//a[starts-with(@class, 'Card-root')]")
		UrlGame = allUrlGame[0].get_attribute('href')
		timeGame = str(allTime[0].text)
		timeGameOk = timeGame.replace('.','')
		embed=discord.Embed(title="Бесплатные игры в Epic Games | Store", description=f"Привет всем участникам канала!\nСейчас в магазине Epic Games | Store бесплатно раздается: ``{nameGameOk}``\n\nДанная игра будет бесплатна до {timeGameOk}, успей добавить ее в свою библиотеку!\n[Ссылка на игру]({UrlGame})", color=0xff7d25)
	else:

		allImgGame = login_form[0].find_elements_by_xpath("//*[starts-with(@class, 'Picture-image')]")
		ImgGame = allImgGame[0].get_attribute("src")
		allTime = login_form[0].find_elements_by_xpath("//time")
		timeGame = allTime[0].text
		timeGameOk = timeGame.replace('.','')

		UrlGame = login_form[0].find_elements_by_xpath("//a[starts-with(@class, 'Card-root')]")
		print(str(UrlGame[0].get_attribute("href")))
		UrlGame = UrlGame[0].get_attribute("href")
		driver.get(str(UrlGame))
		# if nameGameOk == 'Free Games Collection':
		# 	driver.get('https://www.epicgames.com/store/ru/collection/free-games-collection')
		# 	UrlGame = 'https://www.epicgames.com/store/ru/collection/free-games-collection'
		# else:
		# 	driver.get('https://www.epicgames.com/store/ru/collection/free-game-collection')
		# 	UrlGame = 'https://www.epicgames.com/store/ru/collection/free-game-collection'
		await asyncio.sleep(5)
		# login_form = driver.find_elements_by_xpath("//*[starts-with(@class, 'FreeGame-game')]")
		nameGame = driver.find_elements_by_xpath("//*[starts-with(@class, 'StoreCard-title')]")
		nameGameOk ="``"+nameGame[0].text +"`` , ``"+ nameGame[1].text+"``"
		embed=discord.Embed(title="Бесплатные игры в Epic Games | Store", description=f"Привет всем участникам канала!\nСейчас в магазине Epic Games | Store бесплатно раздается: {nameGameOk}\n\nДанные игры будут бесплатны до {timeGameOk}, успей добавить их в свою библиотеку!\n[Ссылка на игры]({UrlGame})", color=0xff7d25)
		

		
	driver.quit()
	todayNew = datetime.datetime.today()
	embed.set_image(url=""+str(ImgGame)+"")
	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	await ctx.send(embed=embed)

@bot.command(pass_context= True)
async def GamePlayGroundZakaz(ctx, *, url):
	todayNew = datetime.datetime.today() 
	todayH = int(todayNew.strftime("%H"))
	todaym = int(todayNew.strftime("%M"))
	if todayH + 5 < 24:
		todayH = todayH + 5
	else:
		todayH = todayH + 5 - 24

	driver = chromeOpen()
	channel = bot.get_channel(619497569298546709)
	# driver.get('https://www.playground.ru/news/')
	# pageListUrl = driver.find_element_by_xpath('//a[@class="item story-container"]')
	# pageGame = pageListUrl.get_attribute('href')
	pageGame = str(url)
	driver.get(pageGame)
	nameNews = driver.find_element_by_xpath('//h1[@class="post-title"]')
	nameNews = nameNews.text
	imgNews = driver.find_element_by_xpath('//figure//img').get_attribute('src')
	titleNews = driver.find_element_by_xpath('//div[@itemprop="articleBody"]/p')
	titleNews = titleNews.text
	driver.quit()
	embed=discord.Embed(title=f"{nameNews}", description=f"{titleNews}\n\n[Читать далее...]({pageGame})", color=0x0078f2)
	embed.set_image(url=""+str(imgNews)+"")
	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	await channel.send(embed=embed)
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
		channel = bot.get_channel(412939700748419086)
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
			#Вот свежий выпуск игровых новостей:\n
			# listGoodMorn = ['Стремитесь не к успеху, а к ценностям, которые он дает​.',
			# 'Разочаровавшись в одном, не наказывайте другого. Все люди разные. Не теряйте способность верить и любить.',
			# 'Нет ничего сильнее идеи, время которой пришло!','Иногда мне кажется, что все, чем я хочу заниматься в жизни — это слушать музыку.',
			# 'В погоне за похвалой лучшая приманка — скромность. Maxim © PS: поддерживаю. ',
			# 'Жизнь – игра, не проиграй себя,','Лучше рисоваться многими знаниями, чем хорошо владеть немногими.',
			# 'На самом деле, жизнь проста. Мы сами настойчиво её усложняем.']
			# goodMornText = random.choice(listGoodMorn)
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
	print('--------')
	while not bot.is_closed():
		await bot.wait_until_ready()
		channel = bot.get_channel(412939700748419086) #615296305144660008
		todayNew = datetime.datetime.today()
		todayWeekDay = str(todayNew.strftime("%A"))
		todayH = int(todayNew.strftime("%H"))
		todayM = int(todayNew.strftime("%M"))
		if todayH + 5 < 24:
			todayH = todayH + 5
		else:
			todayH = todayH + 5 - 24
		print(str(todayH))
		if todayWeekDay == 'Friday' or todayWeekDay == 'Wednesday':
			print('2')
			if todayH == 18 and todayM == 0:
				driver = chromeOpen()
				driver.get('https://www.epicgames.com/store/ru/')
				# assert 'Yahoo' in browser.title 

				# elem = browser.find_element_by_name('p')  # Find the search box
				# elem.send_keys('seleniumhq' + Keys.RETURN)
				# time.sleep(5)
				await asyncio.sleep(5)
				login_form = driver.find_elements_by_xpath("//*[starts-with(@class, 'FreeGame-game')]")
				print(login_form)
				print("Всего lf - "+str(len(login_form)))
				nameGame = login_form[0].find_elements_by_xpath("//*[starts-with(@class, 'FreeGame-gameCardMetaGame')]")
				nameGameOk = nameGame[0].text
				if nameGameOk != 'Бесплатные игры':
					allImgGame = login_form[0].find_elements_by_xpath("//*[starts-with(@class, 'FreeGame-inner')]")
					ImgGame = allImgGame[0].get_attribute("src")
					allTime = login_form[0].find_elements_by_xpath("//time")
					allUrlGame = login_form[0].find_elements_by_xpath("//a[starts-with(@class, 'FreeGame-gameCard')]")
					UrlGame = allUrlGame[0].get_attribute('href')
					print(nameGameOk)
					print(str(ImgGame))
					print(str(allTime[0].text))
					timeGame = str(allTime[0].text)
					timeGameOk = timeGame.replace('.','')
					embed=discord.Embed(title="Бесплатные игры в Epic Games | Store", description=f"Привет всем участникам канала!\nСейчас в магазине Epic Games | Store бесплатно раздается: ``{nameGameOk}``\n\nДанная игра будет бесплатна до {timeGameOk}, успей добавить ее в свою библиотеку!\n[Ссылка на игру]({UrlGame})", color=0xff7d25)
				else:
					allImgGame = login_form[0].find_elements_by_xpath("//*[starts-with(@class, 'FreeGame-inner')]")
					ImgGame = allImgGame[0].get_attribute("src")
					allTime = login_form[0].find_elements_by_xpath("//time")
					timeGame = allTime[0].text
					timeGameOk = timeGame.replace('.','')

					UrlGame = login_form[0].find_elements_by_xpath("//a[starts-with(@class, 'FreeGame')]")
					UrlGame = UrlGame[0].get_attribute("href")
					driver.get(str(UrlGame))
					await asyncio.sleep(5)
					# login_form = driver.find_elements_by_xpath("//*[starts-with(@class, 'FreeGame-game')]")
					nameGame = driver.find_elements_by_xpath("//*[starts-with(@class, 'StoreCard-title')]")
					nameGameOk ="``"+nameGame[0].text +"`` , ``"+ nameGame[1].text+"``"
					embed=discord.Embed(title="Бесплатные игры в Epic Games | Store", description=f"Привет всем участникам канала!\nСейчас в магазине Epic Games | Store бесплатно раздается: {nameGameOk}\n\nДанные игры будут бесплатны до {timeGameOk}, успей добавить их в свою библиотеку!\n[Ссылка на игры]({UrlGame})", color=0xff7d25)
					

					
				driver.quit() 
				embed.set_image(url=""+str(ImgGame)+"")
				embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
				await channel.send(embed=embed)
				todayNew = datetime.datetime.today()
				todayM = int(todayNew.strftime("%M"))
				sleepHOne = 3600 - (todayM * 60)
				# await channel.send('Сплю: '+str(sleepHOne)+' секунд')
				await asyncio.sleep(sleepHOne)
			else:
				print('4')
				todayNew = datetime.datetime.today()
				todayM = int(todayNew.strftime("%M"))
				sleepHOne = 3600 - (todayM * 60)
				# await channel.send('Сплю: '+str(sleepHOne)+' секунд')
				await asyncio.sleep(int(sleepHOne))
				
		else:
			todayNew = datetime.datetime.today()
			todayM = int(todayNew.strftime("%M"))
			sleepHOne = 3600 - (todayM * 60)
			# await channel.send('Сплю: '+str(sleepHOne)+' секунд')
			await asyncio.sleep(int(sleepHOne))

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(412939700748419086)
	embed=discord.Embed(title="Пользователь ``"+str(member.display_name)+"`` присоединился к нашему серверу.", description="Добро пожаловать! Располагайся, чувствуй себя как дома.\nФура достойных каток и интересных тимейтов уже выехала.", color=0x5458bc)
	embed.set_thumbnail(url=''+str(member.avatar_url)+'')
	embed.set_footer(text="Сервер "+str(bot.guilds[0].name))
	await channel.send(embed=embed)
	await member.add_roles(discord.utils.get(member.guild.roles, name='Новичок'))
				
@bot.event
async def on_member_update(before, after):
	# Пользователь начал играть
	if before.activity == None and after.activity != None:
		newGameStatus = after.activity.name
		print(str(after.id))
		if newGameStatus != '' and after.id != 450264735368085505 and after.id != 412235680303939595 :

			channel = bot.get_channel(623944345522798603)
			haveGame = False
			for channelInd in channel.voice_channels:
				if (channelInd.name == str(newGameStatus)):
					haveGame = True
			if(not haveGame):
				massAllVC = channel.voice_channels
				if(len(massAllVC) <= 1):
					await channel.create_voice_channel(name=str(newGameStatus), overwrites=None, reason=None)
				else:
					channelDelInd = massAllVC[0]
					await channelDelInd.delete()
					await channel.create_voice_channel(name=str(newGameStatus), overwrites=None, reason=None)

		# Пользователь начал играть


async def deleteVoiceChannel():
	while not bot.is_closed():
		await bot.wait_until_ready()
		todayNew = datetime.datetime.today()
		todayH = int(todayNew.strftime("%H"))
		todayM = int(todayNew.strftime("%M"))
		if todayH + 5 < 24:
			todayH = todayH + 5
		else:
			todayH = todayH + 5 - 24
		print("Часов "+str(todayH))
		if todayH == 10:
			channel = bot.get_channel(623944345522798603)
			for channelInd in channel.voice_channels:
				if(len(channelInd.members) == 0):
					await channelInd.delete()
			todayNew = datetime.datetime.today()
			todayM = int(todayNew.strftime("%M"))
			sleepHOne = 86400 - (todayM * 60)
			print('Сплю: '+str(sleepHOne)+' секунд')
			await asyncio.sleep(int(sleepHOne))
		else:
			todayNew = datetime.datetime.today()
			todayM = int(todayNew.strftime("%M"))
			sleepHOne = 3600 - (todayM * 60)
			print('Сплю: '+str(sleepHOne)+' секунд')
			await asyncio.sleep(int(sleepHOne))


@bot.event
async def on_message(message):
	randIntOtvMessage = random.randint(0,100)
	if randIntOtvMessage == 0 and message.author.display_name != "Maxim" and not message.author.bot:
		print(message.author.display_name)
		await asyncio.sleep(4)
		massAllOtvMessage = ['https://media.giphy.com/media/YWWeEeFThzFS6VKmyX/giphy.gif','https://media.giphy.com/media/2Y7lZAxlutI5MuVEzb/giphy.gif','https://media.giphy.com/media/a5viI92PAF89q/giphy.gif','https://media.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif','https://media.giphy.com/media/FxEwsOF1D79za/giphy.gif','https://media.giphy.com/media/Lcn0yF1RcLANG/giphy.gif','https://media.giphy.com/media/uHox9Jm5TyTPa/giphy.gif', 'https://media.giphy.com/media/s8Aix99cRIwyk/giphy.gif', 'https://media.giphy.com/media/5h9AIbcxZospnLbmbl/giphy.gif','https://media.giphy.com/media/3LugygiVMlZDXTakyb/giphy.gif','https://media.giphy.com/media/oOxBQwNqGwxeWLDF6A/giphy.gif','https://media.giphy.com/media/5hs5eKmprnJK5hTVGq/giphy.gif','https://media.giphy.com/media/tRzd704xXId2w/giphy.gif']
		imgGif = random.choice(massAllOtvMessage)
		await message.channel.send(message.author.mention)
		await message.channel.send(str(imgGif))

	await bot.process_commands(message)
	# # print(message.content)
	# messageUser = message.content[:]
	# messageUser = messageUser.lower()
	# messageUser = messageUser.split()
	# # print(messageUser)
	# # if set(messageUser).intersection(set(listBunMessage)):
	# for ig in listBunMessage:
	# 	if ig in messageUser:
	# 		channel = message.channel
	# 		userBan = message.author
	# 		infoUserBan = discord.Embed(title= "Данное сообщение не прошло модерацию", colour= 0xf9d506, description=''+str(userBan)+', если хочешь использовать мат, заходи в голосовой чат.')
	# 		infoUserBan.set_footer(text="Администрация осуждает данное высказывание. `© Maxim`")
	# 		await discord.Message.delete(message, delay=None)
	# 		await channel.send(embed=infoUserBan)
	#await bot.process_commands(message)


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
bot.bg_task = bot.loop.create_task(goodMorning())
bot.bg_task = bot.loop.create_task(freeGameEpic())
# bot.bg_task = bot.loop.create_task(newsGamePlayGround())
bot.bg_task = bot.loop.create_task(deleteVoiceChannel())
bot.run(str(token))

