'''
Practice Project 01: Table Printer

Objective(s):
- Write a function named printTable() that takes a list of lists of strings.
- Display it in a well-organized table with each column right-justified.
- Assume that all inner lists will contain the same number (column) of strings.
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)                                # create a list value containing the same number of 0s
                                                                    # as the number of inner list values assigned in variable tableData

    for itemCount in range(len(colWidths)):                         # create a list containing the length of the 1st item of each inner
        colWidths[itemCount] = len(tableData[itemCount][0])         # list value

    for outCount in range(len(tableData)):                          # get the length of each item stored on each inner list values
        for inCount in range(len(tableData[outCount])):
            itemStrLength = len(tableData[outCount][inCount])

            if colWidths[outCount] < itemStrLength:                 # if the current item's length > 1st item's length, replace it
                colWidths[outCount] = itemStrLength

    for strLength in range(len(colWidths)):                         # get the largest number from the list value in variable colWidths
        setPad = colWidths[0]

        if setPad < colWidths[strLength]:
            setPad = colWidths[strLength]                           # this value will be passed as argument to .rjust() method later on

    itemList = len(tableData[0])                                    # display list value items in a formatted way using .rjust() method
    for itemCount in range(itemList):
        print(tableData[0][itemCount].rjust(setPad) + tableData[1][itemCount].rjust(setPad) + tableData[2][itemCount].rjust(setPad))


printTable()
