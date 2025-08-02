import read
import write
import operations
import message
import datetime


def landManagementSystem():
    # Start point for the Land Management System

    message.printWelcomeMessage()
    data = read.readDataFromFile("land.txt")
    landDict = read.createLandDict(data)

    while True:
        message.printTableOfLand()

        # User menu
        print("Enter '1' to rent land")
        print("Enter '2' to return land")
        print("Enter '3' to exit")
        
        try:
             userChoice = int(input("Please enter a value:"))
                
             if userChoice == 1:
                operations.handleLandRental(landDict, data)
             elif userChoice == 2:
                operations.handleLandReturn(landDict, data)
             elif userChoice == 3:
                message.printThankYouMessage()
                break
             else:
                message.printInvalidMessage()

               
        except ValueError:
            print("Invalid input! Please enter valid value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            

# Run the Land Management System
landManagementSystem()
