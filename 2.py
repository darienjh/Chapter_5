stats = {"Strength": "",
         "Health": "",
         "Wisdom": "",
         "Dexterity" : ""}

stre = []
heal = []
wis = []
dex = []


while choice != "0":
    print(
        """
    Welcome to CharacterCreator

    0 - quit
    1 - strength
    2 - health
    3 - wisdom
    4 - dexterity
    """)
    print("You have 30 points to spend")

    if choice == "0":
        print("Goodbye! Thanks for playing!")

    elif choice == "1":
        point = int(input("please enter a number for strength"))
        stre.append(point)
        stats["Strength"] = stre
        total1 = int(point) - 30
        print("You have" ,total1, "to spend")

    elif choice == "2":
        point = int(input("Please enter a number for Health"))
        heal.append(point)
        stats["Health"] = heal
        total2 = int(total1) - 30
        print("You have" ,total2, "to spend")

    elif choice == "3":
        point = int(input("Please Enter a number for wisdom"))
        wis.append(point)
        stats["Wisdom"] = wis
        total3 = int(total2) - 30
        print("You have" ,total3, "to spend")

    elif choice == "4":
        point = int(input("Please Enter a number for dexterity"))
        dex.append(point)
        stats["dexterity"] = dex
        total4 = int(total3) - 30
        print("You have" ,total4, "to spend")
