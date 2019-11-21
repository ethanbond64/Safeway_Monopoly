piecesFile = open('MonopolyPieces.txt','r')
piecesList = []
for line in piecesFile:
    piecesList.append(line[0:5])
print(piecesList)
