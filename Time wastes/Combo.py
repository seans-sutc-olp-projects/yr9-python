yes = 'true'
storageFile =  open('Count-to-infinite-multiple.txt',  'a')
number1 = 0
array1 = []

number2 = 0
array2 = []

number3 = 0
array3 = []

number4 = 0
array4 = []

number5 = 0
array5 = []

number6 = 0
array6 = []

number7 = 0
array7 = []

number8 = 0
array8 = []

number9 = 0
array9 = []

number10 = 0
array10 = []

number11 = 0
array11 = []

number12 = 0
array12 = []

number13 = 0
array13 = []

number14 = 0
array14 = []

number15 = 0
array15 = []

number16 = 0
array16 = []
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
    oldnumber = number1
    number1 = oldnumber + 1
    array1.append(number1)
    storageFile.append(number1)
    print(array1)
    oldnumber = number2
    number2 = oldnumber + 1
    array2.append(number2)
    print(array2)
    oldnumber = number3
    number3 = oldnumber + 1
    array3.append(number3)
    print(array3)
    oldnumber = number4
    number4 = oldnumber + 1
    array4.append(number4)
    print(array4)
    if number1 >= 10:
        oldnumber = number5
        number5 = oldnumber + 1
        array5.append(number5)
        print(array5)
        oldnumber = number6
        number6 = oldnumber + 1
        array6.append(number6)
        print(array6)
        oldnumber = number7
        number7 = oldnumber + 1
        array7.append(number7)
        print(array7)
        oldnumber = number8
        number8 = oldnumber + 1
        array8.append(number8)
        print(array8)
    if number1 >= 20 & number5 >= 10:
        oldnumber = number9
        number9 = oldnumber + 1
        array9.append(number9)
        print(array9)
        oldnumber = number10
        number10 = oldnumber + 1
        array10.append(number10)
        print(array10)
        oldnumber = number11
        number11 = oldnumber + 1
        array11.append(number11)
        print(array11)
        oldnumber = number12
        number12 = oldnumber + 1
        array12.append(number12)
        print(array12)
    if number1 >= 30 & number5 >= 20 & number12 >= 10:
        oldnumber = number13
        number13 = oldnumber + 1
        array13.append(number13)
        print(array13)
        oldnumber = number14
        number14 = oldnumber + 1
        array14.append(number14)
        print(array14)
        oldnumber = number15
        number15 = oldnumber + 1
        array15.append(number15)
        print(array15)
        oldnumber = number16
        number16 = oldnumber + 1
        array16.append(number16)
        print(array16)

