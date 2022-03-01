data1 = open('PCCRASH1.txt', 'r')
data2 = open('PCCRASH2.txt', 'r')
data3 = open('PCCRASH1.txt', 'r')
array  = []
for line1 in data1:
    replaced = line1.replace('\n', '')
    array.append(replaced)
    print(replaced)
    print(array)
    print(data2)
    print(data3)
print(array)
