import requests
import time

def ascii_to_hex ( ascii_text ):
   #print(len(ascii_text))
   hex_text = ascii_text.encode("hex");
   #print(hex_text)
   return hex_text
   
def hex_to_ascii ( hex_text ):
   #print(len(hex_text))
   #print(hex_text)
   if len(hex_text) % 2 != 0:
      hex_text = "0" + hex_text
   ascii_text = hex_text.decode("hex");
   #print(ascii_text)
   return ascii_text

def maxOfPosFltArr(arr):
	largest = -1.0
	ind = -1
	for i in range(0, len(arr)):
		if arr[i] > largest:
			largest = arr[i]
			ind = i

	return ind

def attack():
	mac = [chr(0)] * 20
	url = 'http://localhost:8080/?q=foo&mac=' + ascii_to_hex(''.join(mac))
	r = requests.get(url)

	for ind in range(20):
		times = []
		for i in range(256):
			mac[ind] = chr(i)
			print(url)
			url = 'http://localhost:8080/?q=foo&mac=' + ascii_to_hex(''.join(mac))
			#print(url)
			start_time = time.time()
			r = requests.get(url)
			#if 'Invalid signature' not in r.text:
			#	print 'Success'
			#	print mac
			#	break
			elapsed_time = time.time() - start_time
			times.append(elapsed_time)

		mac[ind] = chr(maxOfPosFltArr(times))
	
	print(ascii_to_hex(''.join(mac)))

attack()

