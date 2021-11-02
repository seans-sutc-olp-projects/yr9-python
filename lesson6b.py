values = """
task1 = > 15
task2 = == 20
task3 = <= 0
task4 = != 5
task5 = < 30
task6 = >= 100
"""
print(values)
task1 = int(input("Enter A Number: "))
task2 = int(input("Enter A Number: "))
task3 = int(input("Enter A Number: "))
task4 = int(input("Enter A Number: "))
task5 = int(input("Enter A Number: "))
task6 = int(input("Enter A Number: "))
if task1 > 15:
    print("Q1: TRUE")
else:
    print("Q1: FALSE")
if task2 == 20:
    print("Q2: TRUE")
else:
    print("Q2: FALSE")
if task3 <= 0:
    print("Q3: TRUE")
else:
    print("Q3: FALSE")
if task4 != 5:
    print("Q4: TRUE")
else:
    print("Q4: FALSE")
if task5 < 30:
    print("Q5: TRUE")
else:
    print("Q5: FALSE")
if task6 >= 100:
    print("Q6: TRUE")
else:
    print("Q6: FALSE")
