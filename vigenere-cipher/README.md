# vigenere-cipher

This is a python script written by me which encodes and decodes plaintext using the _Vigenere cipher._

## What is the Vigenere cipher?
The vigenere cipher is a method of encryption created by  Giovan Battista Bellaso. It is a very simple method of encryption which uses a table and a keyword to encrypt the plaintext.

In order to encrypt the plaintext, the encrypter will need to select a keyword (of any length) which will be used to encrypt the plaintext by. The user will repeat the keyword repeatedly until its length matches the length of the plaintext. Once this is done, the vigenere table is used to encrypt the plaintext letter on the top, and the corresponding keyword letter along the left, and the letter found at the intersection of the two points will be used to encrypt that letter.

Typically, numbers and spaces are not encrypted. In this script, I ignore spaces and numbers however, I put them in the final string.

## How to use this script:
1) Download this script  
2) Run python vigenere-cipher.py in the terminal  
3) Follow the instructions accordingly  
