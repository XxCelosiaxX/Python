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
    return -1

def matrixInsert(hero,comic):
    #row - col
    matrix[comic][hero] = True
    incrementR()
    #print(re)

def read2():
    number = 0
    with open('edges.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        line_count = 0
        heroindex = 0
        for row in csv_reader:
            number+=1
            currenthero = row[0]
            currentcomic = row[1]
            heroindex = ListSearch(currenthero, heroList, number)
            comicindex = ListSearch(currentcomic, comicList, number)
            if heroindex != -1 and comicindex != -1:
                matrixInsert(heroindex, comicindex)

def ColCount():                                 #[work in progress]
    for i in 12651:
        for j in 6439:
        matrix[][]




readIn()
comicList.sort()
heroList.sort()
matrix = [[None]*6439]*12651
print("start Read2")
read2()
print("end")