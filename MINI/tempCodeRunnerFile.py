word = input('Enter a word: ')
k = int(input('Amount to shift by: '))
for char in word.lower(): 
    if char.isalpha():
        cip = ord(char) + k
        cip -= 97
        num = cip%26 
        cip = num
        cip += 97
        print(chr(cip))