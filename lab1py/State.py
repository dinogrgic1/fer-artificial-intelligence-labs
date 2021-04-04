class State:
    state = ''
    depth = ''
    path = 0
    h = 0

    def __init__(self, state, depth, h=0):
        self.state = state
        self.depth = depth
        self.h = h
    
    def __repr__(self):
        return repr((self.state, self.depth, self.h))

    def __str__(self):
        return f'({self.state}, {self.depth}, {self.h})'
