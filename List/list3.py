numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text of number : ")

for i in text:
    i = i.lower()
    if i >= 'a' and i <= 'z':
        numOfLetters = numOfLetters + 1

    elif i >= '0' and i <= '9':
        numOfDigits = numOfDigits + 1

    elif i == ' ':
        numOfWords = numOfWords + 1

print("Number of Letters:", numOfLetters)
print("Number of Digits:", numOfDigits)
print("Number of Words:", numOfWords + 1)
