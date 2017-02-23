import requests
import sha1

def attack():
	r = requests.post("http://localhost:8080/")
	print(r)
	print(r.text)
def task3a():
	message = 'sup'
	h0 = 0x67452301
	h1 = 0xefcdab89
	h2 = 0x98badcfe
	h3 = 0x10325476
	h4 = 0xc3d2e1f0

	a = sha1.sha(h0, h1, h2, h3, h4, message)


	attack()

	print(str(hex(a)))

def calculatePadding():
	message = 'Funny%20names?'
	padding = '%80'
	i = 0
	for i in range(512):
		zeros = '%00' * i
		ourMessage = message + '%80' + zeros + '%60'
		url = 'http://localhost:8080/?who=Costello&what=' + ourMessage + '&mac=b8366a6271aec451046ce8892d308e771662d446'
		r = requests.get(url)
		print(r)

calculatePadding()

#url = 'http://localhost:8080/?who=Costello&what=Funny%20names?&mac=b8366a6271aec451046ce8892d308e771662d446'
#r = requests.get(url)
#print(r)