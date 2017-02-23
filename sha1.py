import sys
import numpy

def to_bytes(n, length, endianess):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]

def rotate(l, n):
    return l[n:] + l[:n]
    
def _left_rotate(n, b):
    """Left rotate a 32-bit integer n by b bits."""
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

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
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def sha1(message):
   h0 = 0x67452301
   h1 = 0xefcdab89
   h2 = 0x98badcfe
   h3 = 0x10325476
   h4 = 0xc3d2e1f0
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

   appendedLength = "{0:b}".format(originalMessageLength)
   lenArr = []
   for c in appendedLength:
      lenArr.append(int(c))
   zeroesNeeded = 64 - len(lenArr)
   while zeroesNeeded != 0:
      lenArr.insert(0, 0)
      zeroesNeeded -= 1

   bitMessage = bitMessage + lenArr
   bitMessage = [bitMessage[i:i+512] for i in range(0, len(bitMessage), 512)]

   words = []
   for chunk in bitMessage:
      words = [int(ascii_to_hex(frombits(chunk[i:i+32])), 16) for i in range(0, len(chunk), 32)]

      for i in range(16, 80):
         words.insert(i, _left_rotate(words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16], 1))
      
      a = h0
      b = h1
      c = h2
      d = h3
      e = h4

      for i in range(0, 80):
         if 0 <= i <= 19:
            f = (b & c) | ((~b) & d)
            k = 0x5a827999
         elif 20 <= i <= 39:
            f = ((b ^ c) ^ d)
            k = 0x6ed9eba1
         elif 40 <= i <= 59:
            f = (b & c) | (b & d) | (c & d) 
            k = 0x8f1bbcdc
         elif 60 <= i <= 79:
            f = ((b ^ c) ^ d)
            k = 0xca62c1d6
            
         temp = (_left_rotate(a, 5) + f + e + k + words[i]) & 0xffffffff
         e = d
         d = c
         c = (_left_rotate(b, 30)) & 0xffffffff
         b = a
         a = temp


      h0 = (h0 + a) & 0xffffffff
      h1 = (h1 + b) & 0xffffffff
      h2 = (h2 + c) & 0xffffffff
      h3 = (h3 + d) & 0xffffffff
      h4 = (h4 + e) & 0xffffffff
   
   finalHash = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4

   return finalHash

def task2b():
   i = 0
   hashes = set()
   notdone = True
   while notdone:
      if i % 50000 == 0:
         print(i)
      hex_string = '{:02x}'.format(i)
      #print(hex_string)
      #if hex_string[len(hex_string) - 1] == 'L':
      #   hex_string = hex_string[:len(hex_string)-1]
      fh = sha1(hex_string)
      key = str(fh & 0x3ffffffffffff)
      if key in hashes:
         print("Collision!")
         print("Key (Hash): " + key)
         print("Val 1: " + str(i))
         #print("Val 2: " + str(i))
         notdone = False
      else:
         hashes.add(key)
      i += 1

#task2b()
print(str(hex(sha1("13644212") & 0x3ffffffffffff)))
print(str(hex(sha1("16937134") & 0x3ffffffffffff)))

"""
ms = ""
for i in range(16777216):
   ms = ms + "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmno"
fH = sha1(ms)
print(str(hex(fH))[2:len(str(hex(fH)))-1])
"""
"""
def task3a():
   h0 = 0x67452301
   h1 = 0xefcdab89
   h2 = 0x98badcfe
   h3 = 0x10325476
   h4 = 0xc3d2e1f0
   sha1(h0, h1, h2, h3, h4, str(i))
"""
