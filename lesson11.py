t1Name = "Bob"
t1Day = 1111
def t1Function1():
    global t1Name
    global t1Day
    age = 12
    eyeColour = "blue"
    print(t1Name)
    print(t1Day)
    print(age)
    print(eyeColour)
# t1Function1()

def t2Q1():
    score = int(input("What is your score? "))
    if score > 80:
        print("Distinction")
    elif score > 60:
        print("Merit")
    elif score > 40:
        print("Pass")
    else:
        print("Fail")
def t2Q2():
    age = int(input("What is your age? "))
    if age > 19:
        print("Adult")
    elif age <= 13:
        print("Teenager")
    else:
        print("Child")
# t2Q1()
# t2Q2()
