import time
import urllib2

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
	largest2 = -1.0
	largest3 = -1.0

	ind = -1
	ind2 = -1
	ind3 = -1

	for i in range(0, len(arr)):
		if arr[i] > largest :
			largest3 = largest2
			ind3 = ind2

			largest2 = largest
			ind2 = ind

			largest = arr[i]
			ind = i
		elif  arr[i] > largest2
			largest3 = largest2
			ind3 = ind2

			largest2 = arr[i]
			ind2 = i
		elif arr[i] > largest3
			largest3 = arr[i]
			ind3 = i

	return [chr(ind), chr(ind2), chr(ind3)]

def attack():
	choices = ['0'] * 3

	mac = [chr(0)] * 20
	url = 'http://localhost:8080/?q=test&mac=' + ascii_to_hex(''.join(mac))
	r = urllib2.urlopen(url).read()
	branch = 0

	for ind in range(20):
		if ind != 0:
			mac[ind-1] = choices[branch]
			branch + 1

		times = []
		for i in range(256):
			mac[ind] = chr(i)
			url = 'http://localhost:8080/?q=test&mac=' + ascii_to_hex(''.join(mac))
			print(url)

			start_time = time.time()
			r = urllib2.urlopen(url)
			elapsed_time = time.time() - start_time

			times.append(elapsed_time)

		choices = maxOfPosFltArr(times)
		#mac[ind] = chr(maxOfPosFltArr(times))
	
	#print(ascii_to_hex(''.join(mac)))

attack()
#3d33728b33b977d5c4c5317fee74398ec93b638a
3d33728b33b977d5c4c5

