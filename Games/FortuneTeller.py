fortune = {
    "red": {
        "fortune one": "Be careful or you could fall for some tricks today!",
        "fortune two": "You have a secret admirer!"
    },
    "green": {
        "fortune three": "Now is a good time to buy stock!",
        "fortune four": "Be careful how you spend this week - you are set to lose a lot!"
    },
    "blue": {
        "fortune five": "Failure is the chance to do better next time!",
        "fortune six": "The harder you work, the luckier you get!"
    },
    "yellow": {
        "fortune seven": "Don’t just spend time - invest it!",
        "fortune eight": "Remember to share good fortune as well as bad with your friends!"
    }
}

TRY = 1

print("The Paper Origami Fortune Teller has gone DIGITAL!\nLet me tell you your fortune for this week..")
name = input("First, tell me your name: ")
print("Hi {}, what do you want to know about?".format(name.capitalize()))

while TRY != 0:
    print("Choose a colour:\nRed for Love\nGreen for Money\nBlue for Work \nYellow for Friendship")
    chosen_colour = input()
    chosen_number = int(input("Now choose either 1 or 2: "))

    for colour in fortune:
        if chosen_colour.lower() == "red":
            if chosen_number == 1:
                print(fortune["red"].get("fortune one"))
            else:
                print(fortune["red"].get("fortune two"))
            break
        elif chosen_colour.lower() == "green":
            if chosen_number == 1:
                print(fortune["green"].get("fortune three"))
            else:
                print(fortune["green"].get("fortune four"))
            break
        elif chosen_colour.lower() == "blue":
            if chosen_number == 1:
                print(fortune["blue"].get("fortune five"))
            else:
                print(fortune["blue"].get("fortune six"))
            break
        elif chosen_colour == "yellow":
            if chosen_number == 1:
                print(fortune["yellow"].get("fortune seven"))
            else:
                print(fortune["yellow"].get("fortune eight"))
            break
    go_again = input("So {}, do you want another try? Y/N: ".format(name.capitalize()))
    if go_again.upper() == "Y":
        TRY += 0
    else:
        TRY -= 1
