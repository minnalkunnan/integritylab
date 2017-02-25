import hashlib
from Crypto.Hash import SHA


def findCollision():
	i = 0
	hashes = set()
	notdone = True
	prevsize = 0
	size = 0

	while notdone:
		if i % 50000 == 0:
			 print(i)
		'''
		if i == 13644212:
		 	print(str(i))
		 	result = SHA.new(str(i))
		 	print(str(int(result.hexdigest(), 16) & 0x3ffffffffffff))
		if i == 16937134:
	 		print(str(i))
	 		result = SHA.new(str(i))
	 		print(str(int(result.hexdigest(), 16) & 0x3ffffffffffff))
	 	'''
		fh = str(SHA.new(str(i)).hexdigest())
		key = int(fh, 16) & 0x3ffffffffffff
		hashes.add(key)

		if key == 764686465868945:
	 		print(str(i))
	 		break

		if i == len(hashes):
			print("Collision!")
			print("Key (Hash): " + str(key))
			print("Val 1: " + str(i))
			#print("Val 2: " + str(i))
			notdone = False
		i += 1

findCollision()
