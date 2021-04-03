from State import State
import queue

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
        visited = set()
        q = {}
        q[0] = [State(start_state, 0)]
        open_nodes = queue.Queue()
        open_nodes.put(State(start_state, 0))

        path_num = 0
        while open_nodes.qsize():
            node = open_nodes.get()
            path = q[node.path]

            visited.add(node.state)
        
            if node.state in final_state:
                return (node, visited, path)            
                
            exp = self.__deafult__expand(node, transition)
            for s in exp:
                if s.state not in visited:
                    path_num += 1
                    s.path = node.path = path_num
                    new_path = list(path)
                    #new_path = insert_method(new_path, s)
                    new_path.append(s)
                    open_nodes = insert_method(open_nodes, s)
                    q[path_num] = new_path
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
        arr.put(node)
        return arr

    @classmethod
    def __UCS__insert(self, arr, node):
        arr.put(node)
        arr.sort(key=lambda x: x.depth)
        return arr

