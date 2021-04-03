from State import State

class Serach:
    kind = ''

    def __init__(self, kind):
        self.kind = kind

    def search(self, start_state, transition, final_state):
        if self.kind == 'bfs':
            return self.__serach(start_state, transition, final_state, self.__BFS__insert)
        elif self.kind == 'ucs':
            return self.__serach(start_state, transition, final_state, self.__UCS__insert)
        else:
            raise NotImplementedError('Serach not implemented')
        
    def __serach(self, start_state, transition, final_state, insert_method):
        visited = []
        open_nodes = []
        open_nodes.append([State(start_state, 0)])

        while len(open_nodes):
            path = open_nodes.pop(0)
            node = path[-1]

            if node.state not in visited:
                visited.append(node.state)
        
            if node.state in final_state:
                return (node, visited, path)            
                
            exp = self.__deafult__expand(node, transition)
            
            for s in exp:
                if s.state not in visited:
                    new_path = list(path)
                    insert_method(new_path, s)
                    open_nodes.append(new_path)
        return (None, visited, None)

    @classmethod
    def __deafult__expand(self, node, transition):
        ret = []
        if node.state not in transition:
            return ret

        for s in transition[node.state]:
            ret.append(State(s.state, s.depth + node.depth))
        return ret

    @classmethod
    def __BFS__insert(self, arr, node):
        arr.append(node)

    @classmethod
    def __UCS__insert(self, arr, node):
        arr.append(node)
        print(arr)  
        arr = sorted(arr, key=lambda x: x.depth)
        print(arr)

