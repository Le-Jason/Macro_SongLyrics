import os

def readData():
    fileName = os.path.join("Data","RedFishBlueFish.txt")
    with open(fileName,'r') as f:
        f_content = f.readline()
        print(f_content)

readData()