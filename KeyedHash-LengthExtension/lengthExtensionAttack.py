import requests
import sha1

def hash(message, tag):
   mac = int(tag, 16)
   
   h0 = (mac >> 128) & 0xffffffff
   h1 = (mac >> 96) & 0xffffffff
   h2 = (mac >> 64) & 0xffffffff
   h3 = (mac >> 32) & 0xffffffff
   h4 = mac & 0xffffffff
   """
   print(hex(h0))
   print(hex(h1))
   print(hex(h2))
   print(hex(h3))
   print(hex(h4))
   """
   a = sha1.sha(h0, h1, h2, h3, h4, message)
   print((str(hex(a)))[2:len(str(hex(a))) - 1])

def attack():
	message = 'Funny%20names?'
	padding = '%80'
	i = 0
	for i in range(512):
		zeros = '%00' * i
		ourMessage = message + '%80' + zeros + '%60' + 'sup'
		tag = hash('sup', 'b8366a6271aec451046ce8892d308e771662d446')
		url = 'http://localhost:8080/?who=Costello&what=' + ourMessage + '&mac=' + tag
		r = requests.get(url)
		print(r)

attack()
