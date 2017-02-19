import sys
import numpy

def rotate(l, n):
    return l[n:] + l[:n]

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

def tobits(s):
    result = []
    #print(len(s))
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    #print(len(bits))
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def sha1(message):
   h0 = 0x67452301
   h1 = 0xEFCDAB89
   h2 = 0x98BADCFE
   h3 = 0x10325476
   h4 = 0xC3D2E1F0

   #get message length in bits
   messageLength = len(message) * 8
   originalMessageLength = messageLength

   #pre processing
   bitMessage = tobits(message)
   #bitMessage = ''.join(format(ord(x), 'b') for x in message)
   bitMessage.append(1)
   bitMessageLen = len(bitMessage)

   while bitMessageLen % 512 != 448:
      bitMessage.append(0)
      bitMessageLen += 1

   #appendedLength = bin(originalMessageLength).replace('b', '')
   appendedLength = tobits(str(originalMessageLength))
   zeroesNeeded = 64 - len(appendedLength)
   while zeroesNeeded != 0:
      appendedLength.insert(0, 0)
      zeroesNeeded -= 1

   bitMessage = bitMessage + appendedLength
   bitMessage = [bitMessage[i:i+512] for i in range(0, len(bitMessage), 512)]

   #print(bitMessage)

   for chunk in bitMessage:
      words = [chunk[i:i+32] for i in range(0, len(chunk), 32)]
   #print(words)
   #print("Words length\n" + str(len(words)))

   for i in range(16, 79):
      words.insert(i, rotate(tobits((XOR_text_key(XOR_text_key(XOR_text_key(frombits(words[i - 3]), frombits(words[i - 8])), frombits(words[i - 14])), frombits(words[i - 16])))), 1))
      #print(words[i])

   a = h0
   b = h1
   c = h2
   d = h3
   e = h4

   for i in range(0, 79):
      if 0 <= i <= 19:
         f = (b & c) | ((~b) & d)
         k = 0x5A827999
      elif 20 <= i <= 39:
         f = ((b ^ c) ^ d)
         k = 0x6ED9EBA1
      elif 40 <= i <= 59:
         f = (b & c) | (b & d) | (c & d) 
         k = 0x8F1BBCDC
      elif 60 <= i <= 79:
         f = ((b ^ c) ^ d)
         k = 0xCA62C1D6
      #print("supwitit")
      temp = 5
      #print(a)
      #print(str(a))

      #print("s")
      #print("i: " + str(i))
      #print(a)
      temp = numpy.uint32((int(ascii_to_hex(frombits(rotate(tobits(hex_to_ascii('{:02X}'.format(a))), 5))), 16) + f + e + k + int(ascii_to_hex(frombits(words[i])), 16)))
      #print("e")
      e = d
      d = c
      c = numpy.uint32(int(ascii_to_hex(frombits(rotate(tobits(hex_to_ascii('{:02X}'.format(b))), 30))), 16))
      b = a
      a = temp
      #print("LEN: " + len(tobits(hex_to_ascii('{:02X}'.format(a)))))

   h0 = numpy.uint32(h0 + a)
   h1 = numpy.uint32(h1 + b)
   h2 = numpy.uint32(h2 + c)
   h3 = numpy.uint32(h3 + d)
   h4 = numpy.uint32(h4 + e)

   print(hex(h0 << 128))
   print(h0)
   finalHash = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4

   return finalHash


#print(int(ascii_to_hex(frombits(rotate(tobits('{:02X}'.format(0x67452301)), 5))), 16))
fH = sha1("abc")
print(str(hex(fH)))
#print(tobits('hello'))
#print(frombits('01101000110010111011001101100110111110000000000000000000000000000'))
"""
uhh = frombits(rotate(tobits(hex_to_ascii('{:02X}'.format(a))), 5))
uh = ascii_to_hex(frombits(rotate(tobits('{:02X}'.format(a)), 5)))
for j in range(0, 79):
   print(tobits(hex_to_ascii('{:02X}'.format(a))))
   print(a)
   print('{:02X}'.format(a))
   print("HAHHHHHEEEEYY")
   print(uh)
   a = int(ascii_to_hex(frombits(rotate(tobits(hex_to_ascii('{:02X}'.format(a))), 5))),16)
"""
