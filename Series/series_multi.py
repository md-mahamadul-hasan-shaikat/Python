
# 1 * 2 * 3 * ....... * n

n = int(input("Enter the last number : "))
multi = 1

for i in range(1, n+1,1):
    multi = multi * i

print(multi)