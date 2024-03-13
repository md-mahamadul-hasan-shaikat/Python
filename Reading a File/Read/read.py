file = open("student.txt", "r+")
#print(file.readable())
'''
text = file.readline()
print(text)
size = len(text)
print(size)
'''

for line in file:
    print(line)
file.close()