# set requests
#http://igurbani.com/iGurbaniService.php?&mode=1&q=gmsshn&src=0&type=0&writer=0&raag=0&ang=&recnum=0&format=json
#http://igurbani.com/iGurbaniService.php?&mode=2&shabadNo=1528&format=json
import json, requests

def searchFirstLetters(firstLetters):
	url = "http://igurbani.com/iGurbaniService.php"
	params = dict(mode=1,q=firstLetters,src=0,type=0,writer=0,raag=0,ang='',recnum=0,format="json")
	resp = requests.get(url=url, params=params)
	data = resp.json()
	for shabad in data['shabads']:
		print [shabad][0]['shabad']['ShabadId'] + " : " + [shabad][0]['shabad']['Transliteration']

def searchShabadWithID(shabadID):
	url = "http://igurbani.com/iGurbaniService.php"
	params = dict(mode=1,q=shabadID,src=0,type=0,writer=0,raag=0,ang='',recnum=0,format="json")
	resp = requests.get(url=url, params=params)
	data = resp.json()
	for shabad in data['shabads']:
		print [shabad][0]['shabad']['ShabadId'] + " : " + [shabad][0]['shabad']['Transliteration']

def main():
	inputItem = "continue"
	while inputItem != "quit":
		print "-------------------------------------------"
		print "---- iGurbani Command Line Interface   ----"
		print "---- Developed by Karandeep Singh      ----"
		print "----                                   ----"
		print "Enter a ShabadID or search by first letters"
		print "-------------------------------------------"
		inputItem = raw_input()
		if isinstance(inputItem,int):
			searchShabadWithID(inputItem)
		if isinstance(inputItem,str):
			searchFirstLetters(inputItem)



if __name__ == "__main__":
	main()