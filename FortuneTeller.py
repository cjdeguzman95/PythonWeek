# design a programme that tells your weekly horoscope
# need to give a personalised experience
# need to be able to work out which star sign the user is

import time

print("Let me tell you your horoscope...")
time.sleep(2)

name = input("First, tell me your name: ")
month = input("What is your birth month?: ")
day = int(input("Which date of the month is your birthday in?: "))

# how to make this using def?
if month.lower() == "december":
    if day < 21:
        astrology = "Sagittarius"
    else:
        astrology = "Capricorn"
elif month.lower() == "january":
    if day < 19:
        astrology = "Capricorn"
    else:
        astrology = "Aquarius"
elif month.lower() == "february":
    if day < 18:
        astrology = "Aquarius"
    else:
        astrology = "Pisces"
elif month.lower() == "march":
    if day < 20:
        astrology = "Pisces"
    else:
        astrology = "Aries"
elif month.lower() == "april":
    if day < 20:
        astrology = "Aries"
    else:
        astrology = "Taurus"
elif month.lower() == "may":
    if day < 20:
        astrology = "Taurus"
    else:
        astrology = "Gemini"
elif month.lower() == "june":
    if day < 21:
        astrology = "Gemini"
    else:
        astrology = "Cancer"
elif month.lower() == "july":
    if day < 22:
        astrology = "Cancer"
    else:
        astrology = "Leo"
elif month.lower() == "august":
    if day < 22:
        astrology = "Leo"
    else:
        astrology = "Virgo"
elif month.lower() == "september":
    if day < 22:
        astrology = "Virgo"
    else:
        astrology = "Libra"
elif month.lower() == "october":
    if day < 22:
        astrology = "Libra"
    else:
        astrology = "Scorpio"
elif month.lower() == "november":
    if day < 22:
        astrology = "Scorpio"
    else:
        astrology = "Sagittarius"

# how to make this using def?
if astrology in ["Sagittarius", "Aquarius", "Aries", "Gemini", "Leo", "Libra"]:
    fortune = "you will receive lots of money this week"
else:
    fortune = "you will meet someone new this week!"

print("Hmmm.. your fortune for the week is...")
time.sleep(2)
print("{}, the universe tells me that ".format(name), fortune)


