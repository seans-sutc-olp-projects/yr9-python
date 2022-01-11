yes = 'true'
number = 0
array = []
while yes == 'true':
    oldnumber = number
    number = oldnumber + 1
    array.append(number)
    print(array)
    ping.verbose_ping('www.sean-outram.dev', count= number)
    if number >= 10000:
        while yes == 'true':
            array2 = array * 4
            print(array2)
    
