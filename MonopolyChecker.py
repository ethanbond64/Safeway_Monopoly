piecesFile = open('MonopolyPieces.txt','r')
piecesList = []
for line in piecesFile:
    piecesList.append(line[0:5])
print(piecesList)

def manyToOne(inputString):
    outList = []
    comma = []

    for letter in range(len(inputString)):
        if inputString[letter] == ',':
            comma.append(letter)
    if len(comma) > 0:
        outList.append(inputString[0:comma[0]])

        for loc in range(len(comma)-1):
            nextWord = inputString[comma[loc]+1:comma[loc+1]]
            outList.append(nextWord)

        outList.append(inputString[comma[-1]+1:])

    else:
        outList.append(inputString)

    return outList

while True:
    userInput = input('Enter the next set (no spaces,only commas):')
    nextSet = manyToOne(userInput)
    for piece in nextSet:
        if piece not in piecesList:
            print('new piece! ' + str(nextSet.index(piece)+1,) + " "  +  piece)
            piecesList.append(piece)
            with open ('MonopolyPieces.txt','a') as writeMe:
                writeMe.write(piece + '\n')
#
# userInput = input('Enter the next set (no spaces,only commas):')
# print(manyToOne(userInput))
