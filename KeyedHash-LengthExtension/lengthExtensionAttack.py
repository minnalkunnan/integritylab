import requests
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
	ourMessage = 'Nicknames,%20nicknames.%20Now,%20on%20the%20St.%20Louis%20team%20we%20have%20Who%27s%20on%20first,%20What%27s%20on%20second,%20I%20Don%27t%20Know%20is%20on%20third--'
	msgsize = len(ourMessage)
	for c in ourMessage:
		if c == '%':
			msgsize -= 2

	msgsize += secretsize
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
	ourMessage = ourMessage + 'deal%20with%20it'
	tag = hash('deal with it', '4388331c12958f7a92f63062ac1e94ea72de9663', size)
	url = 'http://localhost:8080/?who=Costello&what=' + ourMessage + '&mac=' + tag
	print("SIZE MESSAGE: " + str(msgsize))
	print("SIZE OF EVERYTHING: " + str(size))
	print("SIZE OF SIZE STRING: " + str(len(sizeStr) / 3))
	print(url)
	size += 1
	r = requests.get(url)
	if 'Invalid signature' in r.text:
		print "we suck"
	else:
		print "deal with it"
			
attack()
