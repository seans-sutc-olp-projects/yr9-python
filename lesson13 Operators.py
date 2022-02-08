# And:
print("And:")
andUsername = input("USERNAME PLEASE: ")
andPassword = input("PASSWORD PLEASE: ")
if andUsername == "B" and andPassword == "C":
    print("Valid! :)")
else:
    print("Incorrect! :(")

# Or:
print("Or:")
orWeather = input("WEATHER: ")
orTemp = input("TEMP:  ")
if orWeather == "RAINING" or orTemp == "COLD":
    print("Wear a jacket")
else:
    print("Don't wear a Jacket")

# Not:
print("Not:")
notDiet = input("Diet: ")
if not diet == "Vegan"):
    print("Allow Meat")
