import string
#print(ord('a')) #97
#basically each alphabet has an ascii/unicode coe point
#print(ord('b')) #98
#print(chr(97)) #a

#caesar cipher basic logic is that we shift the alphabets
# by a certain no. k

#basic try
#word = input('Enter an alphabet: ')
#temp = ord(word)
#temp += 1
#print(chr(temp))

#basic try 2
word = input('Enter a word: ')
while True:
    try:
        k = int(input('Amount to shift by: '))
        break
    except ValueError:
        print('Enter a valid no')
for char in word.lower(): 
    if char.isalpha():
        cip = ord(char) + k
        cip -= 97
        num = cip%26 
        cip = num
        cip += 97
        print(chr(cip), end='')
    else:
        print(char, end='')