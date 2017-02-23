import requests
import sha1

def attack():
   payload = []
   r = requests.post("http://localhost:8080/", data=payload)

def task3a(message, tag):
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
   a = sha1.sha(h0, h1, h2, h3, h4, message)
   print((str(hex(a)))[2:len(str(hex(a))) - 1])


#attack()

#print(str(hex(a)))

task3a('sup', '93b2c1fbc81bb92ec564918b5974c488f689e33b')
