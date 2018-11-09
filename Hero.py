import csv

re = 0
heroCount = 0
comicCount = 0
heroList = []
comicList = []

def incrementR():
    global re
    re = re + 1

def incrementH():
    global heroCount
    heroCount = heroCount + 1


def incrementC():
    global comicCount
    comicCount = comicCount + 1


def readIn():
    with open('nodes.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        line_count = 0
        for row in csv_reader:
            if row[1] == "comic":
                comicList.append(row[0])
                incrementC()
            elif row[1] == "hero":
                heroList.append(row[0])
                incrementH()
                line_count += 1
        print("Number of Hero =", heroCount)
        print(f'Number of Comic =', comicCount)

def heroSearch(hero, startIndex):
    for i in range(startIndex, len(heroList)):
        if heroList[i] == hero:
            return i


def ListSearch(searchfor, searchIn):
    low = 0
    high = len(comicList)-1
    while low < high:
        mid = int((low + high)/2)
        if searchIn[mid] == searchfor:
            return mid
        elif searchIn[mid] < searchfor:
            low = mid + 1
        else:
            high = mid - 1
        if low == high:
            if searchIn[mid] == searchfor:
                return mid
        if low == high:
            if searchIn[low] == searchfor:
                return low
    if low == high:
        if searchIn[low] == searchfor:
            return low

def matrixInsert(hero,comic):
    #row - col
    matrix[comic][hero] = True
    incrementR()
    print(re)

def read2():
    with open('edges.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        line_count = 0
        heroindex = 0
        for row in csv_reader:
            currenthero = row[0]
            currentcomic = row[1]
            heroindex = ListSearch(currenthero, heroList)
            comicindex = ListSearch(currentcomic, comicList)
            matrixInsert(heroindex, comicindex)
            line_count += 1
    print(line_count)

readIn()
comicList.sort()
heroList.sort()
matrix = [[None]*6439]*12651
print(matrix[12650][6438])
print("ok")
read2()
print("done")