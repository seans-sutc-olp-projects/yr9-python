name = input("what is your name: ")
pets = input("how many pets you have: ")
favoriteSchoolSubject = input("whats your favorite school subject: ")
schoolJourney = input("What is your school journey: ")

captcha = int(input("please enter the answer to 5 + 5: "))
captchaAnswer = 5 + 5
if captcha == captchaAnswer:
    print("Your name is: ", name, "The amount of pets you own is:", pets, "Your favorite school subject is: ", favoriteSchoolSubject, "Your School Journey is: ", schoolJourney)
else:
    print("Captcha failed")


