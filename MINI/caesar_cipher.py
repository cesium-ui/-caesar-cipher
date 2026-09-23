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