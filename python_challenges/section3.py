# Section3

# Q1:
print('Q1')
age = int(input('What is your age? '))
    # CHECKS AGE
if age <= 12:
    print('You are a child')
elif age <= 13:
    print('You are a teenager')
else:
    print('You are an adult')

# Q2:
print('Q2')
    # 5 MEMBERS OF THE CLASS
classMembers = ['Rhys', 'Oliver', 'Conan', 'Ethan', 'Samuel']
    # Shoe Size
classMembersShoeSize = [1, 2, 3, 4, 5]

# Q3:
print('Q3')
    # DOES SMTH 6 TIMES
for i in range(6):
    # DOES THE IF CHECK
    if classMembersShoeSize[i - 1] >= 8:
        print('**BIG FEET** Name: ' + str(classMembers[i - 1]) + ', Size: ' + str(classMembersShoeSize[i - 1]))
    else:
        print('**SMALL FEET** Name: ' + str(classMembers[i - 1]) + ', Size: ' + str(classMembersShoeSize[i - 1]))

# Q4:
print('Q4')

# Q5:
print('Q5')
name1 = input('Whats your name? ')
name2  = ''
    # CHECKS IF NAME2 IS DIFFERENT FROM NAME1
while name2 != name1:
    name2 = input('Whats your name? ')

# Q6:
print('Q6')
number  = int(input('Input a number. '))
    # CHECKS THAT THE NUMBER MEETS SOME VALUES
if number <= 100 and number >= 1:
    print('Well done!')
else:
    print('Better luck next time')

# Q7:
print('Q7')
number = int(input('Input a number. '))
if number > 0:
    print('positive')
else:
    print('negative')


# Q8:
print('Q8')
name = input('What is your name? ')
    # CHECKS IF NAME IS IN THE CLASSMEMBERS ARRAY
if name in classMembers: print('Hello World!')
else:
    print('NO')
