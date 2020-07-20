from bs4 import BeautifulSoup


with open('MyActivity.html') as html_file:  # Here MyActivity.html is the file needed from Google, make sure the .html file is in the same directory as this program or alternatively give path of "MyActivity.html" file.
	soup = BeautifulSoup(html_file, 'lxml')



visited = 0
searched = 0


for x in soup.find_all('div', class_ = 'content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1'):
	
	if(x.text.split()[0] == "Visited"):
		visited += 1
	elif x.text.split()[0] == "Searched":
		searched += 1
	

length = len(soup.find_all('div', class_ = 'content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1'))

print(f'Total Activity : {length}')

print(f'Total No. of Websites Visited : {visited}')

print(f'Total No. of searches on Google : {searched}')