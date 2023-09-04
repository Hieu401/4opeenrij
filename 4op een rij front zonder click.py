import turtle

turtle.speed(0)
# elements expressed in ((begin x coo, end x coor, #), (begin y, end y, #), State), State = O/R/Y
ListCoordinates = []
ListSize = []
input1 = []


def SetCoordinates(RowNum, ColumnNum):
    # Adds de begin x coordinate and end x coordinate of each cell in a set.
    setRow = set([])
    beginx = -0.5 * (70 * RowNum)
    endx = beginx + 70
    rownumber = 0
    for i in range(RowNum):
        setRow.add((beginx, endx, rownumber))
        beginx = endx
        endx = endx + 70
        rownumber = rownumber + 1
    # Adds de begin y coordinate and end y coordinate of each cell in a set.
    setColumn = set([])
    beginy = -0.5 * (70 * ColumnNum)
    endy = beginy + 70
    columnnumber = 0
    for i in range(ColumnNum):
        setColumn.add((beginy, endy, columnnumber))
        beginy = endy
        endy = endy + 70
        columnnumber = columnnumber + 1
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


def undo():
    test = 123


def player1input(columninput):
    if columninput == undo:
        undo()
    elif any(columninput == str(row[0][2]) for row in ListCoordinates):
        input1.append(columninput)
    else:
        print('Invalid command. Please try again.')
        gamesequence1()
    return


def player2input(columninput):
    if columninput == undo:
        undo()
    elif any(columninput == str(row[0][2]) for row in ListCoordinates):
        input1.append(columninput)
    else:
        print('Invalid command. Please try again.')
        gamesequence2()
    return



def executeplayer1input():
    playerinput = input1[-1]
    ListOfCellsInColumn = []
    for cell in ListCoordinates:
        if cell[0][2] == playerinput:
            ListOfCellsInColumn.append(cell)
            beginy = (-0.5 * (70 * ListSize[1]))
            for i in range(len(ListOfCellsInColumn)):
                for row in ListOfCellsInColumn:
                    if row[1][0] == beginy and row[2] == 'O':
                        turtle.setposition((-0.5 * (70 * ListSize[0])) + 70 * playerinput, beginy)
                        DrawCell1()
                        row[2] = 'R'
                        break
                beginy = beginy + 70
            return


def executeplayer2input():
    playerinput = input1[-1]
    ListOfCellsInColumn = []
    for cell in ListCoordinates:
        if cell[0][2] == playerinput:
            ListOfCellsInColumn.append(cell)
            beginy = (-0.5 * (70 * ListSize[1]))
            for i in range(len(ListOfCellsInColumn)):
                for row in ListOfCellsInColumn:
                    if row[1][0] == beginy and row[2] == 'O':
                        turtle.setposition((-0.5 * (70 * ListSize[0])) + 70 * playerinput, beginy)
                        DrawCell2()
                        row[2] = 'Y'
                        break
                beginy = beginy + 70
            return


def gamesequence1():
    checkwin()
    player1input(input('Player 1, please declare the column number you wish to insert your coin into (starting at 0) '
                       'or type undo to undo the previous move'))
    executeplayer1input()
    gamesequence2()


def gamesequence2():
    checkwin()
    player2input(input('Player 2, please declare thw column number you wish to insert your coin into (starting at 0) '
                       'or type undo to undo the previous move'))
    executeplayer2input()
    gamesequence1()


def playgame(RowNum, ColumnNum):
    # need these to use the values within a onclick function
    ListSize.append(RowNum)
    ListSize.append(ColumnNum)
    DrawBoard(RowNum, ColumnNum)
    SetCoordinates(RowNum, ColumnNum)
    gamesequence1()

playgame(int(input('Please call the number of rows')),  int(input('Please call the number of columns')))

