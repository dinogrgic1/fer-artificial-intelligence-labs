from util import Utils

import math
import copy

class Node():
    value = ''
    subtrees = []

    def __init__(self, atr, subtrees):
        self.value = atr
        self.subtrees = subtrees

    def __lt__(self, o):
        if isinstance(o, Node):
            return self.value < o.value
        return False

class Leaf():
    value = ''

    def __init__(self, value):
        self.value = value

class ID3():
    final_feature_num = 0
    model = None

    def __init__(self, dataset, y):
        self.final_feature_num = len(ID3.__args__num__(dataset, y))

    @staticmethod
    def __args__num__(dataset, v):
        values = {}
        for entry in dataset:
            if v not in entry:
                return
            
            if entry[v] not in values:
                values[entry[v]] = 1
            else:
                values[entry[v]] += 1
        return values

    @staticmethod
    def __argmax__(dataset, v):
        values = ID3.__args__num__(dataset, v)
        return max(values, key=values.get)

    @staticmethod
    def __dataset_same_feature__(dataset, v):
        values = ID3.__args__num__(dataset, v)
        return len(values)

    @staticmethod
    def __entropy__(entropy_values, base):
        size = sum(entropy_values.values())
        entropy = 0
        
        for e in entropy_values:
            
            entropy += (entropy_values[e] / size) * math.log(entropy_values[e] / size, base)
        entropy = -entropy
        return entropy

    @staticmethod 
    def __remove_except_feature(D, feature, value, y):
        res = []
        for entry in D:
            if entry[feature] == value:
                res.append(entry)
        return res

    def __IG__(self, D, X, x, y):
        e_d = ID3.__args__num__(D, y)
        entropy_values = ID3.__args__num__(D, x)
        entropy = ID3.__entropy__(e_d, self.final_feature_num)
        
        size = sum(entropy_values.values())
        for e in entropy_values:
            dic = ID3.__remove_except_feature(D, x, e, y)
            tmp = (len(dic) / size) * ID3.__entropy__(ID3.__args__num__(dic, y), self.final_feature_num)
            entropy -= tmp
        return entropy

    def fit(self, D, D_parent, X, y):
        if len(D) == 0:
            v = argmax(D_parent, y)
            return Leaf(v)
        v = ID3.__argmax__(D, y)
        if X == [] or ID3.__dataset_same_feature__(D, y) == 1:
            return Leaf(v)

        max_val = -1
        max_x = None
        for x in X:
            val = self.__IG__(D, X, x, y)
            if val > max_val:
                max_val = val
                max_x = x
        
        subtrees = []
        V = ID3.__args__num__(D, max_x)
        for v in V:
            tmp_X = copy.deepcopy(X)
            tmp_X.remove(max_x)
            t = self.fit(ID3.__remove_except_feature(D, max_x, v, y), D, tmp_X, y)
            subtrees.append(Node(v, [t]))
        subtrees.sort()
        
        n = Node(max_x, subtrees) 
        self.model = n 
        return n

    def predict(self, test_dataset):
        Utils.print_dataset(test_dataset)
        return None

    def print_recursive_tree(self, node, lvl, strr):
        if isinstance(node, Leaf):
            strr += f'{node.value}'
            print(strr)
            return

        if lvl % 2 != 0:
            strr += f'{math.ceil(lvl / 2)}:{node.value}'
        else:
            strr += f'={node.value} '

        for n in node.subtrees:            
            self.print_recursive_tree(n, lvl + 1, strr)

    def print(self):
        print('[BRANCHES]:')
        self.print_recursive_tree(self.model, 1, '')