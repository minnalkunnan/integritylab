import requests
import time

def attack():
	mac = 0x0
	url = 'http://localhost:8080/?q=minnal&mac=' + mac
	r = requests.get(url)

	for i in range(26):
		#print('Attempting ' + mac)
		start_time = time.time()
		r = requests.get(url)
		#if 'Invalid signature' not in r.text:
		#	print 'Success'
		#	print mac
		#	break
		elapsed_time = time.time() - start_time
		print(elapsed_time)
		mac = chr(ord(mac) + 1)


attack()

