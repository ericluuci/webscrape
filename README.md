### **Unofficial Overwatch Webscrape Data Pull Written with Python**

This is a webscraper, when given three inputs (platform, region and battletag) will retrieve the available statistics from Blizzard's Career Overview.

'''
What platform do you play on?
Computer - pc, XBOX - xbl, Playstation - psn
Input: **pc**

What region do you play on
North America - us, Europe - eu, Korea - kr, China - cn
Input: **us**

What is battletag (Ex:Toast-12702)
Input: **Toast-12702**

URL: https://playoverwatch.com/en-us/career/pc/us/Toast-12702
''' 

The program will ask for 3 inputs and requires an internet connection in order to parse the information from the website.

The program will create a directory in the current file titled "Stats" which stores all the information found in several excel spreadsheets. Each one spreadsheet is character's entire statistic. Inside each spreadsheet are several individual sheets (up to 9) that stores a character category (Kills, assists, deaths)
