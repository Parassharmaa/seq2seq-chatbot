import requests
from bs4 import BeautifulSoup

url = "https://bigbangtrans.wordpress.com"

data = requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")

all_links = []

data_folder = "raw/"
characters = ['Leonard', 'Sheldon', 'Raj', 'Howard', 'Penny', 'Bernadette', 'Amy']

for i in soup.find_all("div", {"id": "pages-2"})[0].find_all("a")[1:]:
	all_links.append(i['href'])

for l in all_links:
	data = requests.get(l)
	soup = BeautifulSoup(data.text, "html.parser")
	text_data = []
	dialogs = soup.find("div", {"class": 'entrytext'}).find_all("p")
	title = soup.title.text + ".txt"
	for p in dialogs:
		if p.text.split(":")[0] in characters:
			print(">> " + " ".join(p.text.split()[1:]))
			text_data.append(p.text)
	try:
		with open(data_folder+title, 'w') as f:
			for s in text_data:
				f.write(">> " + s + "\n")
	except:
		pass
