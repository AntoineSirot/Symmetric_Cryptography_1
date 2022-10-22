#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:03:12 2022

@author: antoine
"""

print("Problem 3 : Symetric Cryptography : Problem Set 1")

# 1.
# a)
IntArray = [115, 111, 109, 101, 32, 115, 101, 99, 114, 101, 116, 32, 115, 116, 114, 105, 110, 103]
ChArray = []

for i in IntArray :
  ChArray.append(chr(i)) # Convert every number into his char with ASCII table (chr() vas given in the TD)

ChArray = ''.join(ChArray) # Regrouping terms of ChArray
print("\n1.\n   a) Resulted string : " + ChArray) # Print : some secret string

 
# b) 
Integer = 2438437403287867812943383341690399341847961660385418241405
Hexa = hex(Integer) # Transforming Integer into an Hexadecimal
Hexa = Hexa[2:] # Dropping "0x" before the number for after 
HexaArray = []
IntArray = []
CharArray = []
BytesArray = []

for i in range(0,len(Hexa),2) :
  HexaArray.append(str(Hexa[i:i+2])) # Regrouping Hexa number by 2 

for i in range(len(HexaArray)) :
  BytesArray.append(bytes.fromhex(HexaArray[i])) # Converting Hex to Bytes
  IntArray.append(int.from_bytes(BytesArray[i], "big")) # Converting every number into Int from Bytes
  CharArray.append(chr(IntArray[i])) # Converting Int to Char with ASCII table

CharArray = "".join(CharArray) # Regrouping terms of CharArray
print("   b) Converted to text : " + str(CharArray)) # Print : crypto{a_secret_message}


# 2.
String = "label"
IntArray = []
CharArray = []
for i in range(len(String)) :
  IntArray.append(ord(String[i])^13) # Converting char to his int with ASCII and XoR between every Char and 13
  CharArray.append(chr(IntArray[i])) # Converting int to his char with ASCII
print("2.\n   Message : " + "".join(CharArray)) # Print : aloha


# 3.

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAGKEY1KEY3KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

def XoR(x,y):
  xIntArray = []
  yIntArray = []
  result = []
  for i in range(0,len(x),2) :
    xIntArray.append(int(x[i:i+2], base = 16)) #  Separating x in an array (Bytes to Hex)
    yIntArray.append(int(y[i:i+2], base = 16)) #  Separating y in an array (Bytes to Hex)
  for i in range (len(xIntArray)) :
    result.append((xIntArray[i] ^ yIntArray[i]).to_bytes(1,'big').hex()) # Doing the Xor between x and y, Converting Hex to Bytes
  return "".join(result)  # Return the result of the XoR in bytes


FLAG = XoR(XoR(FLAGKEY1KEY3KEY2,KEY2KEY3),KEY1) # Canceling Key2, Key3, Key1 in this order
BytesArray = []
IntArray = []
CharArray = []
for i in range(0, len(FLAG), 2) :
  BytesArray.append(bytes.fromhex(FLAG[i:i+2])) # Converting Hex to Bytes
for i in range(len(BytesArray)) :
  IntArray.append(int.from_bytes(BytesArray[i], "big")) # Converting Bytes to Int
  CharArray.append(chr(IntArray[i]))

print("3.\n   Decrypted message : " + "".join(CharArray)) # Print : crypto{x0r_i5_ass0c1at1v3}


# 4.
Ciphertext = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
BytesArray = []
IntArray = []
CharArray = []
for i in range(0, len(Ciphertext), 2) :
  BytesArray.append(bytes.fromhex(Ciphertext[i:i+2])) # Converting Hex to Bytes
for i in range(0, len(BytesArray)) :
  IntArray.append(int.from_bytes(BytesArray[i], "big")) # Converting Bytes to Int
"""
for i in range(1, 31) : # We knew that i will be between 0 and 255. We find the result for i = 16
  for j in range(len(IntArray)) :
    CharArray.append(chr((IntArray[j] ^ i))) # Test or the XoR with every possibility
  print("Test with " + str(i) + " : " + "".join(CharArray))
  CharArray = []
"""
for j in range(len(IntArray)) :
    CharArray.append(chr((IntArray[j] ^ 16))) # Doing the XoR with 16
print("4.\n   Result found with " + str(16) + " : " + "".join(CharArray)) # Regrouping the list and Printing : crypto{0x10_15_my_f4v0ur173_by7e}




