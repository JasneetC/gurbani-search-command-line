# set requests
#http://igurbani.com/iGurbaniService.php?&mode=1&q=gmsshn&src=0&type=0&writer=0&raag=0&ang=&recnum=0&format=json
#http://igurbani.com/iGurbaniService.php?&mode=2&shabadNo=1528&format=json
import json, requests
import convert

def searchFirstLetters(firstLetters):
	url = "http://igurbani.com/iGurbaniService.php"
	params = dict(mode=1,q=firstLetters,src=0,type=0,writer=0,raag=0,ang='',recnum=0,format="json")
	resp = requests.get(url=url, params=params)
	data = resp.json()
	for shabad in data['shabads']:
		print [shabad][0]['shabad']['ShabadNo'] + " : " + [shabad][0]['shabad']['Transliteration']

def searchShabadWithID(shabadID):
	url = "http://igurbani.com/iGurbaniService.php"
	params = dict(mode=2,shabadNo=shabadID,format="json")
	resp = requests.get(url=url, params=params)
	data = resp.json()
	for shabad in data['gurbani']:
		# convert the line
		gurmukhi = convert.convertLine([shabad][0]['shabad']['Gurmukhi'])
		print gurmukhi
		print " "
		print [shabad][0]['shabad']['Transliteration']
		print " "
		print [shabad][0]['shabad']['English']
		print "----------------------------------------"

def main():
	inputItem = "continue"
	while inputItem != "quit":
		print "----------------------------------------------"
		print "----    Gurbani Command Line Interface    ----"
		print "----    Use iGurbani.com to search        ----"
		print "----    for shabads from your terminal!   ----"
		print "----                                      ----"
		print "----    Search by first letters           ----"
		print "----    Enter 'quit' to exit              ----"
		print "----------------------------------------------"
		inputItem = raw_input()
		if inputItem == "quit":
			print "exiting"
			break
		elif inputItem.isdigit():
			searchShabadWithID(inputItem)
		elif isinstance(inputItem,str):
			searchFirstLetters(inputItem)




if __name__ == "__main__":
	main()