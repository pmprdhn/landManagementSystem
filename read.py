import datetime

def readDataFromFile(fileName):
    # Reads data from a specified file and returns a list of lines
    data = []
    try:
        with open(fileName, 'r') as file:
            for line in file:
                lineData = line.strip().split(',')
                lineData[0] = int(lineData[0])  # Convert Kitta No to integer
                lineData[3] = int(lineData[3])  # Convert Anna to integer
                lineData[4] = int(lineData[4])  # Convert Price to integer
                data.append(lineData)
    except FileNotFoundError:
        print(f"Error: The file '{fileName}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return data


def createLandDict(data):
    # Creates a dictionary from the given data
    landDict = {}
    try:
        for i in range(len(data)):
            key = i + 1
            value = data[i]
            landDict[key] = value
    except Exception as e:
        print(f"An error occurred while creating the land dictionary: {e}")
    return landDict
