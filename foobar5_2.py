def solution(map):
    mapped = []
    for y, row in enumerate(map):
        for x, element in enumerate(row):
            if element == 1:
                mapped.append(Entity(x,y))
            else:
                mapped.append(Entity(x,y))
    openList = []
    closedList = []
    

class Entity(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.discovered = False

    def getPos(self) -> tuple:
        return(self.x, self.y)

    def setDiscovered(self):
        self.discovered = True

solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
