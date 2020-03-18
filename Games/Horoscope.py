import time

print("Let me tell you your horoscope...")
time.sleep(2)

name = input("First, tell me your name: ")
month = input("What is your birth month?: ")
day = int(input("Which day of the month is your birthday in?: "))


if month.lower() == "december" or month.lower() == "dec":
    if day < 21:
        astrology = "Sagittarius"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Capricorn"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "january" or month.lower() == "jan":
    if day < 19:
        astrology = "Capricorn"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Aquarius"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "february" or month.lower() == "feb":
    if day < 18:
        astrology = "Aquarius"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Pisces"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "march" or month.lower() == "mar":
    if day < 20:
        astrology = "Pisces"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Aries"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "april" or month.lower() == "apr":
    if day < 20:
        astrology = "Aries"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Taurus"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "may":
    if day < 20:
        astrology = "Taurus"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Gemini"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "june" or month.lower() == "jun":
    if day < 21:
        astrology = "Gemini"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Cancer"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "july" or month.lower() == "jul":
    if day < 22:
        astrology = "Cancer"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Leo"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "august" or month.lower() == "aug":
    if day < 22:
        astrology = "Leo"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Virgo"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "september" or month.lower() == "sep":
    if day < 22:
        astrology = "Virgo"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Libra"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "october" or month.lower() == "oct":
    if day < 22:
        astrology = "Libra"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Scorpio"
        print("Oh, you're a {}".format(astrology))
elif month.lower() == "november" or month.lower() == "nov":
    if day < 22:
        astrology = "Scorpio"
        print("Oh, you're a {}".format(astrology))
    else:
        astrology = "Sagittarius"
        print("Oh, you're a {}".format(astrology))


if astrology in ["Sagittarius", "Aquarius", "Aries", "Gemini", "Leo", "Libra"]:
    fortune = "you will receive lots of money this week"
else:
    fortune = "you will meet someone new this week!"

print("Interesting. Hmmm.. Give me a few moments...")
time.sleep(2)

print("{}, the universe tells me that".format(name.capitalize()), fortune)
