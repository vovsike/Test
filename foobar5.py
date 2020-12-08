def solution(map:list):
    player = Player(0,0) #type: Player
    # printMap(map)
    openList = [(0,0)]
    closedList = []
    for cords in openList:
        player.setPos(*cords)
        if (map[player.getPos()[0]][player.getPos()[1]] == 1):
            player.revertMovement()
            closedList.append(cords)
        else:
            if (map[player.getPos()[0]+1][player.getPos()[1]] == 0):
                openList.append((player.getPos()[0]+1, player.getPos()[1]))
            if (map[player.getPos()[0]-1][player.getPos()[1]] == 0):
                openList.append((player.getPos()[0]-1,player.getPos()[1]))
            if (map[player.getPos()[0]][player.getPos()[1]+1] == 0):
                openList.append((player.getPos()[0],player.getPos()[1]+1))
            if (map[player.getPos()[0]][player.getPos()[1]-1] == 0):
                openList.append((player.getPos()[0],player.getPos()[1]-1))
        openList.pop(0)
        print(openList)


    map[player.getPos()[0]][player.getPos()[1]] = 2
    printMap(map)

def printMap(map:list):
    for y, row in enumerate(map):
        for x, element in enumerate(row):
            print (map[x][y], end='\t')
        print ("\r")

class Entity(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.discovered = False

    def getPos(self) -> tuple:
        return((self.x, self.y))

class Player(Entity):
    def __init__(self, x, y):
        super(Player,self).__init__(x, y)
        self.numberOfMoves = 0
        self.movements = [(1,0),(-1,0),(0,1),(0,-1)]
        self.prevLoc = self.getPos()

    def move(self, dir: tuple):
        self.prevLoc = self.getPos()
        self.x += dir[0]
        self.y += dir[1]
        self.numberOfMoves += 1

    def revertMovement(self):
        self.setPos(*self.prevLoc)
        self.numberOfMoves -= 1

    def setPos(self,x,y):
        self.prevLoc = self.getPos()
        self.x = x
        self.y = y
        self.numberOfMoves += 1

    def returnNumberOfMoves(self):
        return self.numberOfMoves

class Title(Entity):
    def __init__(self, x, y,wall):
        super(Title,self).__init__(x, y)
        self.wall = wall

    def isWall(self):
        return self.wall


solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])