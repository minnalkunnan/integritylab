import requests
import sha1

def attack():
	payload = []
	r = requests.post("http://localhost:8080/", data=payload)

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

task3a()
