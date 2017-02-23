import requests
import time

def attack():
	mac = ['0'] * 16
	url = 'http://localhost:8080/?q=foo&mac=' + ''.join(mac)
	r = requests.get(url)

	for i in range(16):
		mac[0] = str(hex(i))[2:]
		url = 'http://localhost:8080/?q=foo&mac=' + ''.join(mac)
		print(url)
		start_time = time.time()
		r = requests.get(url)
		print(r.text)
		#if 'Invalid signature' not in r.text:
		#	print 'Success'
		#	print mac
		#	break
		elapsed_time = time.time() - start_time
		print(elapsed_time)
		

attack()

