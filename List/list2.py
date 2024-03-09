
n = input("Enter a text of number : ")

list = n.split()
sum = 0

for num in list:
    sum = sum + int(num)

print(sum)