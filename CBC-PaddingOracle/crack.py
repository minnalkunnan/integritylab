import os
import binascii
import requests

def checkValidPadding():
	cipherText = '57a2b3801521051afd045182a11e7ac3689beed332666eba4efdd540b9d316ba214bc4a5ecb25394265a45b70cca5dc4'
	ourCipherText = binascii.b2a_hex(os.urandom(48))
	guess = cipherText + ourCipherText

	r = requests.post("http://localhost:8080/?enc=" + guess)
	print(r)
	return r

checkValidPadding()