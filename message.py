import read


def printWelcomeMessage():
    # Prints a welcome message for the Land Management System
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\tHello and Welcome to the Land Management System")
    print("\t        Techno Property Nepal")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def printTableOfLand():
    # Prints the current table of lands with their details
    data = read.readDataFromFile("land.txt")
    landDict = read.createLandDict(data)

    print(
        "------------------------------------------------------------------------------------------------------------------------------------------")
    print("Land ID\t", "Kitta No\t", "City/District Name\t", "Direction\t", "Anna\t", "Price\t", "Availability Status")
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------")
    for key, value in landDict.items():
        print(key, "\t", value[0], "\t\t", value[1], "\t\t", value[2], "\t\t", value[3], "\t", value[4], "       ", value[5])
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------")


def printThankYouMessage():
    # Prints a thank you message for using the system
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Thank you for using our Land Management System")
    print("\t        Techno Property Nepal")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def printInvalidMessage():
    # Prints an error message for invalid input
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Invalid input! Please enter a valid choice (1, 2, or 3).")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
