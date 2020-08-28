from plyer import notification #pip install plyer
from bs4 import BeautifulSoup	#pip install bs4
import requests #pip install requests
import time #time module
def notifyMe(title, message):
	#create notification system
	notification.notify(
		title=title,
		message=message,
		# app_icon="C:\\Users\\DPE\\Desktop\\projects\\coronavirus.ico",
		timeout=20
	)

def analysis(url):
	r = requests.get(url)
	return r.text

if __name__ == "__main__":
	#get input url
	myData = analysis("https://www.worldometers.info/coronavirus/")

	soup = BeautifulSoup(myData, 'html.parser')
	
	myDataSTr = ""

	for tr in soup.find_all("table")[1].find_all("tr"):
		myDataSTr += (tr.get_text())
	#mydata starts from after 909 escape
	myDataSTr = myDataSTr[909:]
	#split mydata
	itemList = (myDataSTr.split("\n\n"))
	#list of countries i want
	country = ["Bangladesh", "USA", "Italy", "India"]
	#Slicing the list
	for item in itemList[2:23]:
		dataList = (item.split("\n"))
		#dataList[1] is the country name
		if dataList[1] in country:
			nTitle = "Covid-19 Cases"
			nText = f"{dataList[1]}:\nTotal Cases: {dataList[2]} \nNew Cases: {dataList[3]} \nTotal Recovered: {dataList[6]} \nCritical Case: {dataList[8]} \nTotal Test: {dataList[11]} \nPopulation: {dataList[13]}"
			notifyMe(nTitle, nText)
			#after 2nd notify me
			time.sleep(2)
	#sleep for one hour
	time.sleep(10)