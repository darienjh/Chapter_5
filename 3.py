father = {"Bob":"jason","Ralph":"chicken"}




while choice != "0":
    print(
        """
    Welcome to Who's Your Daddy!

    0 - Quit
    1 - Add
    2 - Replace
    3 - Delete
    """)
    choice = input("Please pick your choice ")
    print()

    if choice == "0":
        print("Well thank you for playing")

    elif choice == "1":
        name = input("What is the first name?")
        father[name] = input("Enter a name")

    elif choice == "2":
        name = input("Pick a name")
        if name in father:
            new = input("What is the new name")
            father[name] = new
            print("The pair has now been replaced")

    elif choice == "3":
        name = input("What is the first name?")
        if term in father:
            del father[name]
            print("The pair is now deleted")
    

        
