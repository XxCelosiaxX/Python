import csv

heroCount = 0
comicCount = 0
heroList = []
comicList = []
re = 0

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


def ListSearch(searchfor, searchIn, counter):
    low = 0
    high = len(searchIn)-1
    while low <= high:
        mid = int((low + high)/2)
        if searchIn[mid] == searchfor:
            return mid
        elif searchIn[mid] < searchfor:
            low = mid + 1
        else:
            high = mid - 1
    print("counter", counter)
    # return -1                          # This should never happen because all should exist

def matrixInsert(hero,comic):
    # [row][col]
    print ("The hero number:", hero)
    print ("The comic number:", comic)
    matrix[hero][comic] = True
 #   incrementR()
 #   print(re)

def read2():
    number = 0
    with open('edges.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        line_count = 0
        heroindex = 0
        for row in csv_reader:
            number += 1
            currenthero = row[0]
            currentcomic = row[1]
            heroindex = ListSearch(currenthero, heroList, number)
            comicindex = ListSearch(currentcomic, comicList, number)
#            if heroindex > 6437 or comicindex > 12650:
 #               print(row[0])
            if heroindex != -1 and comicindex != -1:
                matrixInsert(heroindex, comicindex)



def ColCount():                             # how many comic per hero
    min = float("inf")
    max = 0
    mean = 0
    for i in range(0, 6438):
        counter = 0
        for j in range(12650):
            if matrix[i][j]:
                counter += 1
        if min >= counter:
            min = counter
        if max < counter:
            max = counter
        mean+= counter
    mean /= 6438
    print("Max comic per hero is ", max)
    print("Min comic per hero is ", min)
    print("Avg comic per hero is ", mean)

def RowCount():                           #how many hero is in a comic
    min = float("inf")
    max = 0
    mean = 0
    for i in range(0, 12650):
        counter = 0
        for j in range(6438):
            if matrix[j][i]:
                counter += 1
        if min >= counter:
            min = counter
        if max < counter:
            max = counter
        mean += counter
    mean /= 12650
    print("Max hero in comic is ", max)
    print("Min hero in comic is ", min)
    print("Avg hero in comic is ", mean)




readIn()
comicList.sort()
heroList.sort()
#matrix = [[None]*6439]*12651
#matrix = [["Test"]*12651]*6439
matrix = [[False for i in range(12651)]for j in range(6439)]
print("start Read2")
read2()
print("start ColCount")
ColCount()
print("start RowCount")
RowCount()
print("end")
