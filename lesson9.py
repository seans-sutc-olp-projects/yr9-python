# Task 1
print('Task 1')

## Q1
def greeting():
    print('hello!')
    print('Welcome to my program!')
greeting()

## Q2
def name():
    name = input('What is your name? ')
    print('Hello,', name, 'Welcome!')
name()

## Q3
def isBob():
    name = input('What is your name? ')
    if name == 'Bob':
        print('Hello')
    else:
        print("Your're not Bob")
isBob()

#Q4
def untilBob():
    name = input('What is your name? ')
    while name != 'Bob':
        print('You Are Not BOB')
        name = input('What is your name? ')
untilBob()

#Q5
def oneTo100():
    for x in range(101):
        print(x)
oneTo100()
