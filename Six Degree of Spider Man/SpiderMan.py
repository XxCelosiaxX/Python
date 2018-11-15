import numpy as np

heroList = [0] * 6486                                    # There are 6486 hero total
comicList = [0] * 12942                                  # There are 12942 comic total
Hero_Comic = np.full((6486, 12942), False, dtype=bool)   # This is the matrix of Hero x Comic
Collab = np.full((6486, 6486), False, dtype=bool)             # This is the matrix of Hero x Hero
SpiderManNumber = [-1] * 6486                            # This list store the Spider Man number for all hero


def dataIn(file):                                        # This function will read the input file and store them in respective list or matrix
    line_count = 0
    for line in file:
        fileline = line.replace("\n", "")
        fileline = fileline.replace("\"", "")
        num, hero = fileline.split(" ", 1)               #split only once after spce
        heroList[line_count] = hero
        line_count += 1
        if num == "6486":                                # First 6486 line is the name of hero
            break

    line_count = 0
    for line in file:                                    # By not closing the file till the function exist, when we read agian in the function it will start where it was left off
        fileline = line.replace("\n", "")
        fileline = fileline.replace("\"", "")
        num, comic = fileline.split(" ", 1)
        comicList[line_count] = comic
        line_count += 1
        if num == "19428":                               # from line 6487 to 19428
            break

    for line in file:                                    # from line 19428 to the end is the edges list, with varying length per line
        fileline = line.replace("\n", "")
        linestring = fileline.split()                    # split the line after each space and store as array
        heronum = int(linestring[0])
        for index in linestring[1:]:
            comicindex = int(index) - 6486
            Hero_Comic[heronum-1][comicindex-1] = True   # set the Hero_Comic matrix to true in the respective coordinate


def collab_fill():                                       # This function will fill the Collab matrix if the hero share comic
    share = []
    for i in range(12942):                               # Check each row in the column
        for j in range(6486):
            if Hero_Comic[j][i]:
                share.append(j)
        if len(share) != 1:
            for x in range(0,len(share)-1):
                for z in range(x+1, len(share)):
                    Collab[share[x]][share[z]] = True
                    Collab[share[z]][share[x]] = True

        share.clear()


def Calculate():
    level = 0               # how many degree of separation
    count = 0
    checked = []              # hero that have been check in the previous level
    found = []
    SpiderManNumber[5305] = level
    checked.append(5305)

    while len(checked) != 0:
        level += 1
        print("Calculating Degree ", level)

        for i in range(len(checked)):
            for j in range(6486):
                if Collab[checked[i]][j]:
                        found.append(j)
        checked.clear()

        while len(found) != 0:
            if SpiderManNumber[found[-1]] == -1:              # [-1] get last element of list
                SpiderManNumber[found[-1]] = level
                checked.append(found[-1])
            del found[-1]

    for i in range (-1, 6):                             # actually give -1 to 5
        count = 0
        for j in range (6486):
            if SpiderManNumber[j] == i:
                count += 1
        print("Number of Hero with degree: ",i, " is ", count)


def result(index):
    if SpiderManNumber[index] == -1:
        print(index+1, heroList[index], ":", "> 6")
    else:
        print(index + 1, heroList[index], ":", SpiderManNumber[index])


file = open('porgat.txt', 'r')                  # open input file
dataIn(file)                                    # this is done so DataIn() can continue to read where it ended
file.close()                                    # close input file
collab_fill()
Calculate()
for i in range (6486):
    result(i)


# https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python - last element of list
# https://stackoverflow.com/questions/6903557/splitting-on-first-occurrence - split only once
