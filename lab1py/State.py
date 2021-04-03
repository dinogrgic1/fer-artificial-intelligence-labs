class State:
    state = ''
    depth = ''
    path = 0

    def __init__(self, state, depth):
        self.state = state
        self.depth = depth
    
    def __repr__(self):
        return repr((self.state, self.depth))

    def __str__(self):
        return f'({self.state}, {self.depth})'
