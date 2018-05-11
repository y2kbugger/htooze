import random

class Planet():
    def __init__(self, size=(100, 100)):
        self.life = {}
        self.size = size
        for dimension in size:
            if dimension <= 0:
                raise ValueError
            else:
                continue

    def addcell(self, cell):
        ''' Add a cell to the planet at random position

        Parameters
        ----------
        cell : htooze.world.Cell
            A cell is added to the world


        '''
        position = tuple(random.randint(0, n) for n in self.size)
        self.life[position] = cell
        print(position)

class Cell():
    def __init__(self):
        #self.reach = 1
        pass

    def choose_move(self):
        return Move()

class Move(): # Why are classes sometimes defined with parentheses and sometimes without?
    def __init__(self, distance=1):
        self.axis = random.randint(0,1)
        self.distance = distance

