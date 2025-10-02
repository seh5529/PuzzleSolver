
class Node:
    def __init__(self, neighbors, character,x, y):
        self.neigbors = neighbors
        self.character = character
        self.x = x
        self.y = y
    def to_string(self):
        return str(f'{self.x},{self.y}')