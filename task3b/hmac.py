import sha1

def hmac(message, key):
   blocksize = 64
   keylen = len(key)
   
   if keylen > blocksize:
      hashKey = str(hex(sha1.sha(key)))
      key = sha1.hex_to_ascii(hashKey[2:len(hashKey)-1])

   while len(key) != blocksize:
      key += chr(0)

   ipad = sha1.hex_to_ascii("36" * blocksize)
   opad = sha1.hex_to_ascii("5c" * blocksize)
   
   firstSha = str(hex(sha1.sha(sha1.XOR_text_key(key, ipad) + message)))
   firstSha = sha1.hex_to_ascii(firstSha[2:len(firstSha)-1])
   fh = sha1.sha(sha1.XOR_text_key(key, opad) + firstSha)
   
   return fh

print("Sample 1")   
finalHash = hmac("Sample #1", sha1.hex_to_ascii("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f"))
hashStr = str(hex(finalHash))
hashStr = hashStr[2:len(hashStr)-1]
if len(hashStr) % 2 == 1:
   hashStr = "0" + hashStr
print(hashStr)

print("Sample 2")
finalHash = hmac("Sample #2", sha1.hex_to_ascii("303132333435363738393a3b3c3d3e3f40414243"))
hashStr = str(hex(finalHash))
hashStr = hashStr[2:len(hashStr)-1]
if len(hashStr) % 2 == 1:
   hashStr = "0" + hashStr
print(hashStr)

print("Sample 3")
finalHash = hmac("Sample #3", sha1.hex_to_ascii("505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3"))
hashStr = str(hex(finalHash))
hashStr = hashStr[2:len(hashStr)-1]
if len(hashStr) % 2 == 1:
   hashStr = "0" + hashStr
print(hashStr)

print("Sample 4")
finalHash = hmac("Sample #4", sha1.hex_to_ascii("707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0"))
hashStr = str(hex(finalHash))
hashStr = hashStr[2:len(hashStr)-1]
if len(hashStr) % 2 == 1:
   hashStr = "0" + hashStr
print(hashStr)
