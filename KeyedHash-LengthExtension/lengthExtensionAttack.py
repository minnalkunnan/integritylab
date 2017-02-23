#import requests
import sha1

def hash(message, tag, prevSize):
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
   a = sha1.sha(h0, h1, h2, h3, h4, message, prevSize)
   return (str(hex(a))[2:len(str(hex(a))) - 1])


def attack():
	secretsize = 40
	ourMessage = 'Funny%20names?'
	msgsize = 12 + secretsize
	size = msgsize
	i = 0
	#for i in range(60 - size):
	ourMessage = ourMessage + '%80'
	size += 1
	while (size * 8) % 512 != 448:
		ourMessage = ourMessage + '%00'
		size += 1
	
	zeros = '%00' * (59 - size)
	sizeStr = ""
	for j in range(7, -1, -1):
		#print(hex(size >> (j * 4)))
		partial = (str(hex(((msgsize*8) >> (j * 8)) & 0xff)))[2:]
		if len(partial) % 2 == 1:
			partial = "0" + partial
		sizeStr += '%' + partial
	size += len(sizeStr) / 3
	ourMessage = ourMessage + sizeStr
	tag = hash('sup', '121dcea87e135cf769e22add789fba74ca40ad0d', size)
	url = 'http://localhost:8080/?who=Costello&what=' + ourMessage + '&mac=' + '121dcea87e135cf769e22add789fba74ca40ad0d'
	print("SIZE MESSAGE: " + str(msgsize))
	print("SIZE OF EVERYTHING: " + str(size))
	print("SIZE OF SIZE STRING: " + str(len(sizeStr) / 3))
	print(url)
	size += 1
	#print(url)
	#r = requests.get(url)
	#if 'Invalid signature' in r.text:
	#	print "we suck"
	#else:
	#	print "deal with it"
	#	print url
			
attack()
