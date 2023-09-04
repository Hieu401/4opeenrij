import turtle

turtle.speed(0)
# elements expressed in ((begin x coo, end x coor), (begin y, end y), State), State = O/R/Y
ListCoordinates = []
ListSize = []


def SetCoordinates(RowNum, ColumnNum):
    # Adds de begin x coordinate and end x coordinate of each cell in a set.
    setRow = set([])
    beginx = -0.5 * (70 * RowNum)
    endx = beginx + 70
    for i in range(RowNum):
        setRow.add((beginx, endx))
        beginx = endx
        endx = endx + 70
    # Adds de begin y coordinate and end y coordinate of each cell in a set.
    setColumn = set([])
    beginy = -0.5 * (70 * ColumnNum)
    endy = beginy + 70
    for i in range(ColumnNum):
        setColumn.add((beginy, endy))
        beginy = endy
        endy = endy + 70
    # Adds the x and y coordinates and the state of each cell in a list.
    for xcoord in setRow:
        state = 'O'
        for ycoord in setColumn:
            ListCoordinates.append((xcoord, ycoord, state))


# draws width lines 40 longer than all circle cells altogether width
def DrawWidth(RowNum):
    turtle.forward((RowNum * 70) + 40)
    turtle.left(90)


# draws length lines 40 longer than all circle cells altogether in length
def DrawLength(ColumnNum):
    turtle.forward((ColumnNum * 70) + 40)
    turtle.left(90)


# Draws the outer border of the bord/rectangle
def DrawRec(RowNum, ColumnNum):
    # set begin position of the rectangle making sure it is 20 beyond the starting point
    turtle.penup()
    turtle.setposition(-0.5 * (70 * RowNum) - 20, -0.5 * (70 * ColumnNum) - 20)
    turtle.pendown()
    # fills rectangle blue
    turtle.fillcolor('blue violet')
    turtle.begin_fill()
    # gives rectangle form
    DrawWidth(RowNum)
    DrawLength(ColumnNum)
    DrawWidth(RowNum)
    DrawLength(ColumnNum)
    turtle.end_fill()
    turtle.penup()
    # return turtle to standard position for the circles
    turtle.setposition(-0.5 * (70 * RowNum), -0.5 * (70 * ColumnNum))


# draws rows for the number of columns the player specified
def DrawColumn(RowNum, ColumnNum):
    # makes sure to start 70 below the start position, because the first move it makes is to go up 70
    turtle.setposition((-0.5 * (70 * RowNum)), (-0.5 * (70 * ColumnNum) - 70))
    # Goes up 70 and then draws row * the amount of columns specified
    for Col in range(ColumnNum):
        turtle.penup()
        turtle.left(90)
        turtle.forward(70)
        turtle.right(90)
        turtle.pendown()
        DrawRow(RowNum)
    # return to the start position (go down the length of a cell * amount of cells in a column)
    turtle.right(90)
    turtle.forward(70 * ColumnNum)
    turtle.left(90)


# draws the amount of circles in a row specified by the player
def DrawRow(RowNum):
    for Row in range(RowNum):
        DrawCell()
    # returns turtle all the way back to the left but not the bottom (go left the width of a cell * amount of cells
    # in a row)
    turtle.left(180)
    turtle.forward(70 * RowNum)
    turtle.left(180)


# draws r = 30 circle with 5 extra spaces on both sides of the circle (70 in total) and coloring it white
def DrawCell():
    turtle.penup()
    turtle.forward(35)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(35)


def DrawCell1():
    turtle.penup()
    turtle.forward(35)
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(35)


def DrawCell2():
    turtle.penup()
    turtle.forward(35)
    turtle.pendown()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(35)


def DrawBoard(RowNum, ColumnNum):
    turtle.penup()
    # makes sure the board is central
    turtle.setposition(-0.5 * (70 * RowNum), -0.5 * (70 * ColumnNum))
    # Draws border of the bord
    DrawRec(RowNum, ColumnNum)
    # Draws all the circles in the bord
    DrawColumn(RowNum, ColumnNum)
    # Sets the coordinates in a list
    SetCoordinates(RowNum, ColumnNum)


# Makes a coin drop to the bottom
def player1drop(x, y):
    # take x-mouse coord
    xmouse = x
    # for every coord in thelist, give the begin x-pos and end x-pos of each cell
    for cor in ListCoordinates:
        beginx = cor[0][0]
        endx = cor[0][1]
        # check if x-pos of mouse falls under the column
        if xmouse >= beginx and xmouse <= endx:
            # start at the bottom
            beginy = (-0.5 * (70 * ListSize[1]))
            # if it does, take those cells in the col and check if they are open, starting at the lowest open cell
            while beginy <= (beginy + (70 * ListSize[1])):
                # if the current lowest position is open, fill it in with red and mark it as 'R'
                # break the loop to prevent from filling in others on top
                if cor[2] == 'O' and cor[1][0] == beginy:
                    turtle.setposition(beginx, beginy)
                    DrawCell1()
                    cor = list(cor)
                    cor[2] = 'R'
                    cor = tuple(cor)
                    break
                # if the lowest was not open, check the one above if it is open
                else:
                    beginy = beginy + 70
        break
    return


# same as player1drop, but with other mark and color
def player2drop(x, y):
    # take x-mouse coord
    xmouse = x
    # for every coord in thelist, give the begin x-pos and end x-pos of each cell
    for cor in ListCoordinates:
        beginx = cor[0][0]
        endx = cor[0][1]
        # check if x-pos of mouse falls under the column
        if xmouse >= beginx and xmouse <= endx:
            # start at the bottom
            beginy = (-0.5 * (70 * ListSize[1]))
            # if it does, take those cells in the col and check if they are open, starting at the lowest open cell
            # if it is not open, go to the cell above and check again
            while beginy <= (beginy + (70 * ListSize[1])):
                    # if the current lowest position is open, fill it in with red and mark it as 'Y'
                    # break the loop to prevent from filling in others on top
                if cor[2] == 'O' and cor[1][0] == beginy:
                    turtle.setposition(beginx, beginy)
                    DrawCell2()
                    cor = list(cor)
                    cor[2] = 'Y'
                    cor = tuple(cor)
                    break
                # if the lowest was not open, check the one above if it is open
                else:
                    beginy = beginy + 70


# makes a coin drop on click
def player1():
    turtle.onscreenclick(player1drop)


def player2():
    turtle.onscreenclick(player2drop)


# check if someone has won horizontally
def checkwin1():
    # take every cell on the board
    for cell in ListCoordinates:
        # and take the 3 cells horizontally after
        wincell1 = (cell[0][0], cell[0][1], cell[1], 'W')
        wincell2 = (wincell1[0] + 70, wincell1[1] + 70, cell[1], 'W')
        wincell3 = (wincell2[0] + 70, wincell2[1] + 70, cell[1], 'W')
        wincell4 = (wincell3[0] + 70, wincell3[1] + 70, cell[1], 'W')
        winlist = [wincell1, wincell2, wincell3, wincell4]
        # bind those 4 cells to the cells on the bord
        for check in ListCoordinates:
            for wincell in winlist:
                # and take the state of that cell: O, R or Y
                if wincell[0] == check[0][0] and wincell[1] == check[0][1] and wincell[2] == check[1]:
                    checklist = []
                    checklist.append(check[2])
                    # if those 4 cells are all red, player 1 wins and exit the game
                    if checklist.count('R') == 4:
                        print('Player 1 wins')
                        exit()
                    # if those 4 cells are all red, player 2 wins and exit the game
                    elif checklist.count('Y') == 4:
                        print('Player 2 wins')
                        exit()
                    # if none of those conditions are met, go back to the previous function and check for other wins


# check if someone has won vertically
def checkwin2():
    for cell in ListCoordinates:
        wincell1 = (cell[0], cell[1][0], cell[1][1], 'W')
        wincell2 = (wincell1[0], wincell1[1] + 70, wincell1[2] + 70, 'W')
        wincell3 = (wincell2[0], wincell2[1] + 70, wincell2[2] + 70, 'W')
        wincell4 = (wincell3[0], wincell3[1] + 70, wincell3[2] + 70, 'W')
        winlist = [wincell1, wincell2, wincell3, wincell4]
        for check in ListCoordinates:
            for wincell in winlist:
                if wincell[0] == check[0] and wincell[1] == check[1][0] and wincell[2] == check[1][0]:
                    checklist = []
                    checklist.append(check[2])
                    if checklist.count('R') == 4:
                        print('Player 1 wins')
                        exit()
                    elif checklist.count('Y') == 4:
                        print('Player 2 wins')
                        exit()


# check if someone has won diagonally
def checkwin3():
    for cell in ListCoordinates:
        wincell1 = (cell[0][0], cell[0][1], cell[1][0], cell[1][1], 'W')
        wincell2 = (wincell1[0] + 70, wincell1[1] + 70, wincell1[2] + 70, wincell1[3] + 70, 'W')
        wincell3 = (wincell2[0] + 70, wincell2[1] + 70, wincell2[2] + 70, wincell2[3] + 70, 'W')
        wincell4 = (wincell3[0] + 70, wincell3[1] + 70, wincell3[2] + 70, wincell3[3] + 70, 'W')
        winlist = [wincell1, wincell2, wincell3, wincell4]
        for check in ListCoordinates:
            for wincell in winlist:
                if wincell[0] == check[0][0] and wincell[1] == check[0][1] and wincell[2] == check[1][0] and \
                        wincell[3] == check[1][1]:
                    checklist = []
                    checklist.append(check[2])
                    if checklist.count('R') == 4:
                        print('Player 1 wins')
                        exit()
                    elif checklist.count('Y') == 4:
                        print('Player 2 wins')
                        exit()


# check if someone has won diagonally the other way
def checkwin4():
    for cell in ListCoordinates:
        wincell1 = (cell[0][0], cell[0][1], cell[1][0], cell[1][1], 'W')
        wincell2 = (wincell1[0] - 70, wincell1[1] - 70, wincell1[2] + 70, wincell1[3] + 70, 'W')
        wincell3 = (wincell2[0] - 70, wincell2[1] - 70, wincell2[2] + 70, wincell2[3] + 70, 'W')
        wincell4 = (wincell3[0] - 70, wincell3[1] - 70, wincell3[2] + 70, wincell3[3] + 70, 'W')
        winlist = [wincell1, wincell2, wincell3, wincell4]
        for check in ListCoordinates:
            for wincell in winlist:
                if wincell[0] == check[0][0] and wincell[1] == check[0][1] and wincell[2] == check[1][0] and \
                        wincell[3] == check[1][1]:
                    checklist = []
                    checklist.append(check[2])
                    if checklist.count('R') == 4:
                        print('Player 1 wins')
                        exit()
                    elif checklist.count('Y') == 4:
                        print('Player 2 wins')
                        exit()


def checkwin():
    checkwin1()
    checkwin2()
    checkwin3()
    checkwin4()
    return


def gamesequence():
    checkwin()
    player1()
    checkwin()
    player2()


def playgame(RowNum, ColumnNum):
    # need these to use the values within a onclick function
    ListSize.append(RowNum)
    ListSize.append(ColumnNum)
    DrawBoard(RowNum, ColumnNum)
    SetCoordinates(RowNum, ColumnNum)
    for turns in range(int(0.5 * RowNum * ColumnNum) + 1):
        gamesequence()
        if turns == int((0.5 * RowNum * ColumnNum) + 1):
            print('draw')

playgame(int(input('Please call the number of rows')),  int(input('Please call the number of columns')))

