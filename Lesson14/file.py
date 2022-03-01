# 1)
#data = open('data.txt', 'r')
#print(data)

# 2)
#data = open('data.txt', 'r')
#for line in data:
#    print(line)

#  3)
array = []
data = open('data.txt', 'r')
for line in data:
    array.append(line)
print(array)
