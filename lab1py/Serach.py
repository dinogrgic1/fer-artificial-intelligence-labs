from State import State
from collections import deque

class Serach:
    kind = ''

    def __init__(self, kind):
        self.kind = kind

    def search(self, start_state, transition, final_state, heuristic):
        if self.kind == 'bfs':
            return self.__serach(start_state, transition, final_state, self.__deafult__expand, self.__BFS__insert, None)
        elif self.kind == 'ucs':
            return self.__serach(start_state, transition, final_state, self.__deafult__expand, self.__UCS__insert, None)
        elif self.kind == 'astar':
            return self.__serach(start_state, transition, final_state, self.__astar__expand, self.__ASTAR__insert, heuristic)
        else:
            raise NotImplementedError('Serach not implemented')
        
    def __serach(self, start_state, transition, final_state, expand, insert_method, heuristic):
        visited = set()
        q = {}
        q[0] = [State(start_state, 0)]
        
        open_nodes = deque()
        open_nodes.append(State(start_state, 0))
        #closed = deque()

        path_num = 0
        while open_nodes.count:
            node = open_nodes.popleft()
            path = q[node.path]

            visited.add(node.state)
        
            if node.state in final_state:
                return (node, visited, path)        
            exp = expand(node, transition)

            for s in exp:
                #print(exp)
                if s.state not in visited:
                    #if heuristic == None:
                    path_num += 1
                    s.path = node.path = path_num
                    new_path = list(path)
                    new_path.append(s)
                    open_nodes = insert_method(open_nodes, s, heuristic)
                    q[path_num] = new_path

                    # else:
                    #     closed.append(node)
                    #     union = deque(closed)
                    #     union.extend(exp)

                    #     m_s = self.__astar__condition(union, s) 
                    #     if m_s == None:
                    #         if heuristic(m_s) < heuristic(s):
                    #             continue
                    #         else:
                    #             union.remove(m_s)
                    #     path_num += 1
                    #     s.path = node.path = path_num
                    #     new_path = list(path)
                    #     new_path.append(s)
                    #     open_nodes = insert_method(open_nodes, s, heuristic)
                    #     q[path_num] = new_path

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
    def __astar__condition(self, union, m):
        for m_s in union:
            if m.state == m_s.state:
                return m_s
        return None

    @classmethod
    def __astar__expand(self, node, transition):
        ret = []
        if node.state not in transition:
            return ret

        for s in transition[node.state]:
            ret.append(State(s.state, s.depth + node.depth, s.h))
        return ret

    @classmethod
    def __BFS__insert(self, arr, node, heuristics):
        arr.append(node)
        return arr

    @classmethod
    def __UCS__insert(self, arr, node, heuristics):
        arr.append(node)
        return deque(sorted(arr, key=lambda x: x.depth))

    @classmethod
    def __ASTAR__insert(self, arr, node, heuristics):
        arr.append(node)
        return deque(sorted(arr, key=lambda x: (x.depth + x.h)))

