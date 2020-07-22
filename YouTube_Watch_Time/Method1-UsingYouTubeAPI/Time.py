from bs4 import BeautifulSoup

import YouTubeAPI


with open('MyActivity.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')



times =0;
seconds =0
minutes = 0
hours =0

# videoID = soup.find('div', class_ = 'content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1').a['href'].split('=')[1]

# YouTubeAPI.util('r4ddFYrK_Fk')


for x in soup.find_all('div', class_ = 'content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1'):
	if(x.text.split()[0] == "Watched"):
		times += 1
		
		try:
			
			
			if x.a['href']:
				
				seconds += YouTubeAPI.util(x.a['href'].split('=')[1])

		except Exception as e: 
			print(x)
			print(e)
			print(times)

		# if(times % 100 == 0):
		# 	print(seconds)
		# 	break
			
	
	
		


carry = int(seconds/60)

seconds = seconds - (carry*60) 
minutes += carry

carry = int(minutes/60)

minutes = minutes-(carry*60)


hours += carry

carry = int(hours/24)

hours = hours -(carry*24)

days = carry

days = carry

print(f'Days : {days}') 

print(f'Hours : {hours}') 

print(f'Minutes : {minutes}') 

print(f'Seconds : {seconds}') 


print(f'Total No. of Videos watched on YouTube : {times}')


