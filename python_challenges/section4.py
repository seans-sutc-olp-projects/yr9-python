# Section4

#Q1:
print('Q1')
def stutter(word):
    twoLetter = word[:2]
    stuttered= twoLetter + '...'
    finalValue = stuttered + stuttered + word
    print(finalValue)
stutter('LOLZ')

#Q2:
print('Q2')
def discount(price, discount):
    return price / discount
print(discount(1500, 50))
