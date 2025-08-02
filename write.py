import datetime

def updateLandAvailability(landId, newStatus, fileName="land.txt"):
    # Updates the availability status of a specific land ID
    try:
        with open(fileName, 'r') as file:
            lines = file.readlines()

        updatedLines = []
        for line in lines:
            lineData = line.strip().split(',')
            currentLandId = int(lineData[0])

            if currentLandId == landId:
                lineData[5] = newStatus

            updatedLine = ','.join(lineData) + '\n'
            updatedLines.append(updatedLine)

        with open(fileName, 'w') as file:
            file.writelines(updatedLines)

    except Exception as e:
        print(f"An error occurred while updating land availability: {e}")


def writeInvoiceToFile(name, invoiceContent):
    # Writes the rental invoice to a file with a unique identifier
    try:
        uniqueValue = str(datetime.datetime.now().minute + datetime.datetime.now().second + datetime.datetime.now().microsecond)
        with open(f"Rent_{name}_{uniqueValue}.txt", 'w') as file:
            file.write(invoiceContent)
    except Exception as e:
        print(f"An error occurred while writing the invoice: {e}")


def writeInvoiceToFileReturn(name, invoiceContent):
    # Writes the return invoice to a file with a unique identifier
    try:
        uniqueValue = str(datetime.datetime.now().minute + datetime.datetime.now().second + datetime.datetime.now().microsecond)
        with open(f"Return_{name}_{uniqueValue}.txt", 'w') as file:
            file.write(invoiceContent)
    except Exception as e:
        print(f"An error occurred while writing the return invoice: {e}")
