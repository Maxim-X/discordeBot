import requests
import sqlite3
import time
import json
import datetime
import locale

class Scraping:

    def __init__(self):

        self.baseUrl = "https://www.epicgames.com/store/ru-RU/product/"
        self.gameData = []  # Data from free games (name, link)
        self.validGameData = []  # Verified games from the DB method

        self.endpoint = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=ru-RU&country" \
                        "=RU&allowCountries=RU "

        self.data = None

    def reset_request(self):

        self.gameData = []
        self.data = None
        self.validGameData = []

    def searchAtrName(self, allInfo, key):
        if len(allInfo) > 0:
            for info in allInfo:
                print("---------"+str(info["key"])+"---------"+str(info["value"]))
                if info["key"] == str(key):
                    return info["value"]
        return None

    def make_request(self):
        """Makes the request and removes the unnecessary JSON data"""

        self.reset_request()

        try:
            self.data = requests.get(self.endpoint)

            self.data = json.loads(self.data.content)  # Bytes to json object
            print(self.data)
        except:
            print(time.strftime('[%Y/%m/%d]' + '[%H:%M]') +
                  "[ERROR]: Epic Games request failed!")

        # Removes the not relevant information from the JSON object
        self.data = self.data["data"]["Catalog"]["searchStore"]["elements"]

    def process_request(self):  # Filters games that are not free
        """Returns the useful information form the request"""

        for i in self.data:
            # print(i)
            try:
                if not i["promotions"]["promotionalOffers"]:  # If the game isn't free or listed
                    continue
            except TypeError:
                continue
            # Parses relevant data such as name and link and adds It to gameData
            urlName = self.searchAtrName(i["customAttributes"], "com.epicgames.app.productSlug")
            locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
            dateEnd = datetime.datetime.strptime(i["price"]["lineOffers"][0].get("appliedRules")[0].get("endDate"), '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%d %b")
            imagePost = i["keyImages"][0]["url"]
            if urlName is not None:
                temp = (i["title"], str(self.baseUrl+urlName), dateEnd, imagePost) # dateEnd i["customAttributes"]).get("com.epicgames.app.blacklist")
                self.gameData.append(temp)

obj = Scraping()
