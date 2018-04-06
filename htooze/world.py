import random

class Planet():
    def __init__(self, size=(100, 100)):    
        self.life = {}
        self.size = (100, 100)
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
        pass
