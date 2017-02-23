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
   return (str(hex(a))[2:len(str(hex(a))) - 1])


def attack():
	message = 'Funny%20names?'
	size = 12
	i = 0
	for i in range(60 - size):
		zeros = '%00' * (59 - size)
		sizeStr = ""
		for j in range(3, -1, -1):
			#print(hex(size >> (j * 4)))
			partial = (str(hex((size >> (j * 8)) & 0xff)))[2:]
			if len(partial) % 2 == 1:
				partial = "0" + partial
			sizeStr += '%' + partial
			
		ourMessage = message + '%80' + zeros + sizeStr
		tag = hash('sup', '121dcea87e135cf769e22add789fba74ca40ad0d')
		url = 'http://localhost:8080/?who=Costello&what=' + ourMessage + '&mac=' + '121dcea87e135cf769e22add789fba74ca40ad0d'
		#print(url)
		size += 1
		#print(url)
		r = requests.get(url)
		if 'Invalid signature' in r.text:
			print "we suck"
		else:
			print "deal with it"
			print url
			
attack()
