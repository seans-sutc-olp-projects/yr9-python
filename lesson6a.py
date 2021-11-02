values = """
Task1 = Bob
Task2 = Testing
Task3 =
Task4 = 123
Task5 = 123
"""
print(values)
task1 = input("Enter for task 1: ")
task2 = input("Enter for task 2: ")
task3 = input("Enter for task 3: ")
task4 = input("Enter for task 4: ")
task5 = int(input("Enter for task 5: "))
if task1 == "Bob":
    print("Task 1: TRUE")
else:
    print("Task 1: FALSE")
if task2 == "Testing":
    print("Task 2: TRUE")
else:
    print("Task 2: FALSE")  
if task3 == "":
    print("Task 3: TRUE")
else:
    print("Task 3: FALSE")
if task4 == "123":
    print("Task 4: TRUE")
else:
    print("Task 4: FALSE")
if task5 == 123:
    print("Task 5: TRUE")
else:
    print("Task 5: FALSE")
