from State import State
from collections import deque
import heapq


class Serach:
    kind = ''

    def __init__(self, kind):
        self.kind = kind

    def search(self, start_state, transition, final_state, heuristic):
        if self.kind == 'bfs':
            return self.__serach(start_state, transition, final_state, self.__BFS__pop, self.__BFS__insert, self.__deafult__expand, None)
        elif self.kind == 'ucs':
            return self.__serach(start_state, transition, final_state, self.__priority__pop, self.__priority__insert, self.__deafult__expand, None)
        elif self.kind == 'astar':
            return self.__serach(start_state, transition, final_state, self.__priority__pop, self.__priority__insert, self.__astar__expand, heuristic)
        else:
            raise NotImplementedError('Serach not implemented')

    def __serach(self, start_state, transition, final_state, pop, insert, expand, heuristic):
        visited = set()
        q = {}

        start_node = State(start_state, 0)
        if heuristic != None:
            start_node.h = heuristic[start_state]

        q[0] = [start_node]
        open_nodes = []
        insert(open_nodes, start_node)
        closed_dict = {}

        path_num = 0
        while len(open_nodes):
            node = pop(open_nodes)
            path = q[node.path]
            visited.add(node.state)

            if node.state in final_state:
                return (node, visited, path)

            exp = expand(node, transition)
            for s in exp:
                if s.state not in visited:
                    path_num += 1
                    s.path = node.path = path_num
                    m_s = closed_dict.get(s.path)
                    if m_s != None:
                        if (m_s.depth) < (s.depth):
                            continue
                    
                    closed_dict[node.path] = s
                    new_path = list(path)
                    new_path.append(s)
                    open_nodes = insert(open_nodes, s)
                    q[path_num] = new_path
            closed_dict[node.path] = node

        return (None, visited, None)

    @classmethod
    def __deafult__expand(self, node, transition):
        ret = []
        if node.state in transition:
            for s in transition[node.state]:
                ret.append(State(s.state, s.depth + node.depth))
        return ret

    @classmethod
    def __astar__expand(self, node, transition):
        ret = []
        if node.state not in transition:
            return ret

        for s in transition[node.state]:
            ret.append(State(s.state, s.depth + node.depth, s.h))
        return ret

    @classmethod
    def __BFS__insert(self, arr, node):
        arr.append(node)
        return arr

    @classmethod
    def __BFS__pop(self, arr):
        return arr.pop(0)

    @classmethod
    def __priority__insert(self, arr, node):
        heapq.heappush(arr, node)
        return arr

    @classmethod
    def __priority__pop(self, arr):
        return heapq.heappop(arr)
