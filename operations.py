import datetime
import write
import message
import read


def handleLandRental(landDict, data):
    # Handles the rental of land based on user input
    rentals = []
    grandTotal = 0
    renterName = ""  # Initialize the renter's name variable

    while True:
        try:
            message.printTableOfLand()
            landId = int(input("Enter the land ID you want to rent: "))

            if landId <= 0 or landId > len(landDict):
                print("Invalid land ID! Please enter a valid ID.")
            else:
                landStatus = data[landId - 1][5]
                if landStatus.lower() == "available":
                    if renterName == "":
                        renterName = input("Enter the name of the person renting the land:")  # Ask for the name once

                    rentalDate = datetime.datetime.now()
                    duration = int(input("Enter the number of months to rent: "))

                    # Update land status
                    write.updateLandAvailability(landDict[landId][0], "Not Available")
                    landDict[landId][5] = "Not Available"

                    landPrice = landDict[landId][4] * duration
                    grandTotal += landPrice

                    # Store rental details
                    rentals.append((landId, renterName, duration, rentalDate))

                    decision = input("Do you want to rent another land? (n to stop, anything else to continue): ")
                    if decision.lower() == 'n':
                        invoice = generateInvoice(rentals, renterName, rentalDate, landDict, grandTotal)
                        write.writeInvoiceToFile(renterName, invoice)
                        print(invoice)
                        break
                else:
                    print(f"Land ID {landId} is not available for rental.")
                    decision = input("Do you want to rent another land? (n to stop, anything else to continue): ")
                    if decision.lower() == 'n':
                        break

        except ValueError:
            print("Invalid input! Please enter valid data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def handleLandReturn(landDict, data):
    # Handles the return of land based on user input
    rentalsToReturn = []
    renterName = ""
    totalAmount = 0  # Cumulative total for all returns

    try:
        while True:
            message.printTableOfLand()
            landId = int(input("Enter the land ID you want to return (or -1 to stop): "))

            if landId == -1:  # Exit condition for loop
                break

            if landId <= 0 or landId > len(landDict):
                print("Invalid land ID! Please enter a valid ID.")
                continue

            landDetails = data[landId - 1]
            landStatus = landDetails[5]

            if landStatus.lower() == "not available":
                if renterName == "":
                    renterName = input("Enter the name of the person returning the land: ")

                # Collect rental details
                rentalDateStr = input("Enter the rental start date (YYYY-MM-DD): ")
                rentalDate = parseDate(rentalDateStr)
                rentalDuration = int(input("Enter the expected rental duration in months: "))
                expectedDuration = 30 * rentalDuration

                # Calculate the fine and total amount
                returnDate = datetime.datetime.now()  # Current date and time
                actualDuration = (returnDate - rentalDate).days
                monthlyRate = landDict[landId][4]
                fine = calculateFine(actualDuration, expectedDuration, monthlyRate)

                # Update total amounts
                landRent = rentalDuration * monthlyRate
                totalAmount += landRent + fine

                # Update land availability
                write.updateLandAvailability(landDict[landId][0], "Available")
                landDict[landId][5] = "Available"

                # Add to list of rentals to return
                rentalsToReturn.append({
                    "landId": landId,
                    "landDetails": landDetails,
                    "rentalDate": rentalDate,
                    "returnDate": returnDate,
                    "fine": fine,
                    "totalAmount": landRent,
                })

                print(f"Land ID {landId} has been returned and is now available.")
            else:
                print(f"Land ID {landId} is already available or not currently rented.")

        # Generate the return invoice for all returned lands
        if rentalsToReturn:
            totalFine = sum(rental["fine"] for rental in rentalsToReturn)
            grandTotal = totalAmount + totalFine

            # Generate the return invoice
            returnInvoice = generateReturnInvoice(renterName, rentalsToReturn, totalFine, grandTotal)

            # Write the invoice to a file and display it in the terminal
            write.writeInvoiceToFileReturn(f"{renterName}_return", returnInvoice)

            # Display the invoice
            print("Here is your return invoice:")
            print(returnInvoice)

        else:
            print("No lands were returned.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred while returning the land: {e}")


def parseDate(dateStr):
    # Parses a date string into a datetime object
    try:
        return datetime.datetime.strptime(dateStr, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")


def calculateFine(actualDuration, expectedDuration, monthlyRate):
    # Calculates the fine based on the difference between actual and expected durations
    if actualDuration > expectedDuration:
        fine = int(((monthlyRate / 30) * (actualDuration - expectedDuration)))
    else:
        fine = 0
    return fine


def generateInvoice(rentals, customerName, rentalDate, landDict, grandTotal):
    # Generates a rental invoice based on the rental details
    
    invoice = f"""
-----------------------------------------------------------
Invoice for Land Rental
-----------------------------------------------------------

Name of Customer: {customerName}
Date and Time of Rent of Land: {rentalDate}
Total amount for all rented lands: Rs {grandTotal}
-----------------------------------------------------------
"""

    for rental in rentals:
        landId, _, duration, _ = rental
        landDetails = landDict[landId]
        amount = landDetails[4]*duration

        invoice += f"""
Kitta No: {landDetails[0]}
Location: {landDetails[1]}
Direction: {landDetails[2]}
Anna: {landDetails[3]}
Monthly Rate of Land: {landDetails[4]}
Rental Duration: {duration} months
Amount = Rs{amount}
-----------------------------------------------------------
"""
    return invoice


def generateReturnInvoice(renterName, rentalsToReturn, totalFine, grandTotal):
    # Generates a return invoice based on the return details
    returnInvoice = f"""
-----------------------------------------------------------
Land Return Invoice
-----------------------------------------------------------

Name of Customer: {renterName}
Total Fine: Rs {totalFine}
Grand Total: Rs {grandTotal}
-----------------------------------------------------------
"""

    for rental in rentalsToReturn:
        landDetails = rental["landDetails"]
        returnInvoice += f"""
Kitta No: {landDetails[0]}
Location: {landDetails[1]}
Direction: {landDetails[2]}
Rental Start Date: {rental["rentalDate"].date()}
Return Date: {rental["returnDate"].date()}
Fine: Rs {rental["fine"]}
Total Amount: Rs {rental["totalAmount"]}
-----------------------------------------------------------
"""
    return returnInvoice
