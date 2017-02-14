import os
import binascii
import requests

def ascii_to_hex ( ascii_text ):
   hex_text = ascii_text.encode("hex");
   #print(hex_text)
   return hex_text
   
def hex_to_ascii ( hex_text ):
   ascii_text = hex_text.decode("hex");
   #print(ascii_text)
   return ascii_text
   
def hex_to_base64 ( hex_text ):
   base64_text = hex_text.decode("hex").encode("base64");
   #print(base64_text)
   return base64_text
   
def base64_to_hex ( base64_text ):
   hex_text = base64_text.decode("base64").encode("hex");
   #print(hex_text)
   return hex_text
   
def XOR_text_key ( text , key ):
   main_key = key
   new_text = ""
   while len(main_key) < len(text):
      main_key += key
   main_key = main_key[:len(text)]
   
   hex_text = ascii_to_hex(text)
   hex_key = ascii_to_hex(main_key)
   
   hex_new_text = hex(int(hex_text, 16) ^ int(hex_key, 16))
   hex_new_text = hex_new_text[2:len(hex_new_text)-1]

   #print(len(hex_new_text))
   while len(hex_new_text) != len(hex_text):
      hex_new_text = "0" + hex_new_text
      
   new_text = hex_to_ascii(hex_new_text)
   return new_text
   
def checkValidPadding():
   cipherText = '57a2b3801521051afd045182a11e7ac3689beed332666eba4efdd540b9d316ba214bc4a5ecb25394265a45b70cca5dc4'
   aCT = hex_to_ascii(cipherText)
   ourCipherText = os.urandom(48)
   IS = ['\0'] * 16
   #firstCT = ourCipherText[0:len(ourCipherText) - 16]
   firstCT = aCT[0:16]
   lastCT = aCT[32:48]
   #ourCipherText[len(ourCipherText) - 16:len(ourCipherText)]
   errCode = 403
   
   curTry = -1
   
   for i in range (15, -1, -1):
      curPad = 16 - i
      block = list(os.urandom(16))
      
      for j in range(15, i, -1):
	      block[j] = chr(curPad ^ ord(IS[j]))
         
      print(block)

      while errCode != '404':
            curTry += 1
            block[i] = chr(curTry)
            r = requests.get("http://localhost:8080/?enc=" + ascii_to_hex(firstCT) + ascii_to_hex("".join(block)) + ascii_to_hex(lastCT))
            errCode = str(r).split("[")[1].split("]")[0].strip("\n")
            
      IS[i] = chr(curPad ^ ord(block[i]))
      errCode = '403'
      curTry = -1

   print(ascii_to_hex("".join(IS)))

checkValidPadding()
