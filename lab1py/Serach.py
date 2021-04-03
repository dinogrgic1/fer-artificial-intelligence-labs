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
        queue = {}
        queue[0] = [State(start_state, 0)]
        open_nodes = [State(start_state, 0)]        

        path_num = 0
        while len(open_nodes):
            node = open_nodes.pop(0)
            path = queue[node.path]

            if node.state not in visited:
                visited.append(node.state)
        
            if node.state in final_state:
                for i in queue:
                    print(i)
                    print(queue[i])
                return (node, visited, path)            
                
            exp = self.__deafult__expand(node, transition)
            
            for s in exp:
                if s.state not in visited:
                    path_num += 1
                    s.path = node.path = path_num
                    new_path = list(path)
                    new_path = insert_method(new_path, s)
                    open_nodes = insert_method(open_nodes, s)
                    queue[path_num] = new_path
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
        return arr

    @classmethod
    def __UCS__insert(self, arr, node):
        arr.append(node)
        arr = sorted(arr, key=lambda x: x.depth)
        return arr

