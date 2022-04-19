def standardForm(num):
    compressed = open("compressed.txt", "a")
    n = 0
    while num >= 10:
        num = num / 10
        n = n + 1
    while num < 1:
        num = num * 10
        n = n -1
    compressed.write(str(n) + ": " + str(int((num))))
    compressed.write("\n")
total = 1
counter = 1
uncompressed = open("uncompressed.txt", "a")
while True:
    total = total * counter
    counter += 1
    print(str(counter) + ": " + str(total))
    uncompressed.write(str(counter) + ": " + str(total))
    uncompressed.write("\n")
    #standardForm(total)
