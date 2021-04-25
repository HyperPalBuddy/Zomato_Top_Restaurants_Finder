import requests
from bs4 import BeautifulSoup


def cuisinelist():
	print("Cuisine Choices")
	print("1-Chinese")
	print("2-Pizza")
	print("3-North Indian")
	print("4-Fast Food")
	print("5-Beverages")
	print("6-Biryani")
	print("7-South Indian")
	print("8-Desserts")
	print("9-Bakery")
	print("10-Ice Cream")
	print("11-Street Food")
	choice = input("Enter Choice=")
	choice = int(choice)

	try:
		choice = int(choice)
	except ValueError:
		output = choice.replace(" ", "-")
		output = output.lower()
	else:
		if choice == 1:
			output = "chinese"
		elif choice == 2:
			output = "pizza"
		elif choice == 3:
			output = "north-indian"
		elif choice == 5:
			output = "beverages"
		elif choice == 6:
			output = "biryani"
		elif choice == 4:
			output = "fast-food"
		elif choice == 7:
			output = "south-indian"
		elif choice == 8:
			output = "desserts"
		elif choice == 9:
			output = "bakery"
		elif choice == 10:
			output = "ice-cream"
		elif choice == 11:
			output = "street-food"

	finally:
		return output


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
location = input("Enter Location: ")
cuisine = cuisinelist()
url1 = 'https://www.zomato.com/'
url2 = "/restaurants/"
url = url1 + location + url2 + cuisine
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')
for item in soup.select('.search-result'):
	try:
		print()
		print('----------------------------------------')
		print(item.select('.result-title')[0].get_text())
	except Exception as e:
		print('')