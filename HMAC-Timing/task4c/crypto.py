import os, time
from Crypto import Hash
from Crypto.Hash import SHA
from Crypto.Hash import HMAC as hmac

def ascii_to_hex ( ascii_text ):
   #print(len(ascii_text))
   hex_text = ascii_text.encode("hex");
   #print(hex_text)
   return hex_text

class HMAC:
	def __init__(self):
		self.key = os.urandom(SHA.digest_size)
		h =  hmac.new(self.key,'test',SHA)
		tag = h.digest()
		print(ascii_to_hex(tag))

	def hmac_sha1_sign(self, key, msg):
		h =  hmac.new(key,msg,SHA)
		value = h.digest()
		print(ascii_to_hex(value))
		return value

	def hmac_sha1_verify(self, key, msg, tag):
		h = hmac.new(key,msg,SHA)
		tag_new = h.digest()
		#print(ascii_to_hex(tag_new))
		#An obvious check
		if len(tag) != len(tag_new):
			return False
		#Now, for extra security, check each byte, one at a time
		flag = True
		for i in range(len(tag)):
			if tag[i] != tag_new[i]:
				flag = False
			time.sleep(.005)	
		return flag

	def verify_query(self, msg, tag):
		try:
			ret = self.hmac_sha1_verify(self.key, msg, tag.decode("hex"))
		except:
			ret = False
		return ret
	
	def mac_query(self, msg):
		return self.hmac_sha1_sign(self.key, msg).encode("hex")
