'''
# 1 + 2 + 3 + ....... + n
n = int(input("Enter the last number : "))

sum = 0

for i in range(1, n+1, 1):
    sum = sum + i

print(sum)

'''

# 1*1 + 2*2 + 3*3 + ....... + n

n = int(input("Enter the last number : "))
sum = 0

for i in range(1, n+1,1):
    sum = sum + i*i

print(sum)