from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options




chrome_options = Options()
chrome_options.add_extension('/Users/tejpatel/Desktop/Web-Scraping/YouTube_Watch_Time_Using_YouTubeAPI/ADYoutube.crx') #Provide the path to adblocker for youtube here

with open('MyActivity.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')



times =0;
seconds =0
minutes = 0
hours =0



for x in soup.find_all('div', class_ = 'content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1'):
	if(x.text.split()[0] == "Watched"):
		times += 1
		
		
		if x.a['href']:
			driver = webdriver.Chrome(executable_path ="./chromedriver", options= chrome_options)
			driver.get(x.a['href'])
			try:
				driver.find_element_by_class_name("ytp-ad-skip-button").click()
			except NoSuchElementException:
				print("No Ad")

			try:
				sel_soup = BeautifulSoup(driver.page_source, 'lxml')
				driver.close()
				mixed = sel_soup.find('span' , class_ = 'ytp-time-duration').text
			except Exception as e: 
				print(x)
				print(e)
				print(times)

			
			if mixed:
				print(mixed)
				splitValues =  mixed.split(':')
				if len(splitValues) == 3:
					seconds = seconds + int(splitValues[2])
					minutes = minutes + int(splitValues[1])
					hours = hours +  int(splitValues[0])
				elif len(splitValues) == 2:
					minutes = minutes + int(splitValues[0])
					seconds = seconds + int(splitValues[1])
				elif len(splitValues) == 1:
					seconds = seconds + int(splitValues[0])


	# if(times%10 == 0):
	# 	# print(seconds)
	# 	# print(x)
	# 	break


		# if(times % 100 == 0):
		# 	print(seconds)
	
	
		


carry = int(seconds/60)

seconds = seconds - (carry*60)
minutes += carry

carry = int(minutes/60)

minutes = minutes-(carry*60)

hours += carry

carry = int(hours/24)

hours = hours -(carry*24)

days = carry

print(f'Days : {days}') 

print(f'Hours : {hours}') 

print(f'Minutes : {minutes}') 

print(f'Seconds : {seconds}') 


print(f'Total No. of Videos watched on YouTube : {times}')


