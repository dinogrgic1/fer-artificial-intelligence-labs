from util import Utils

import collections
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
    max_lvl = math.inf
    final_feature_num = 0
    model = None

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
        values = collections.OrderedDict(sorted(values.items()))
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
        entropy = ID3.__entropy__(e_d, len(self.final_feature))
        
        size = sum(entropy_values.values())
        for e in entropy_values:
            dic = ID3.__remove_except_feature(D, x, e, y)
            tmp = (len(dic) / size) * ID3.__entropy__(ID3.__args__num__(dic, y), len(self.final_feature))
            entropy -= tmp
        return entropy

    def __fit_alg(self, D, D_parent, X, y, lvl):
        if len(D) == 0:
            v = ID3.__argmax__(D_parent, y)
            return Leaf(v)
        v = ID3.__argmax__(D, y)
        if X == [] or ID3.__dataset_same_feature__(D, y) <= 1 or lvl > self.max_lvl:
            return Leaf(v)

        max_val = -1
        max_x = None
        for x in X:
            val = self.__IG__(D, X, x, y)
            if val > max_val:
                max_val = val
                max_x = x
            elif val == max_val:
                if x < max_x:
                    max_x = x
        
        subtrees = []
        V = ID3.__args__num__(D, max_x)
        for v in V:
            tmp_X = copy.deepcopy(X)
            tmp_X.remove(max_x)
            t = self.__fit_alg(ID3.__remove_except_feature(D, max_x, v, y), D, tmp_X, y, lvl+1)
            subtrees.append(Node(v, [t]))
        subtrees.sort()
        n = Node(max_x, subtrees) 
        self.model = n 
        return n

    def fit(self, D, lvl=math.inf):
        if(lvl != math.inf):
            self.max_lvl = int(lvl)
        self.final_feature = ID3.__args__num__(D, list(D[0].keys())[-1])
        self.__fit_alg(D, D, list(D[0].keys())[:-1], list(D[0].keys())[-1], 1)

    def predict(self, D, y):
        dataset = copy.deepcopy(D)
        confusion_dict = {}

        for f1 in sorted(self.final_feature):
            for f2 in sorted(self.final_feature):
                confusion_dict[f'{f1}|{f2}'] = 0
        
        predictions = ''
        correct = 0

        for entry in dataset:
            entry_cpy = copy.deepcopy(entry)
            del entry_cpy[y]

            true_value = entry[y]
            predicted_value = self.predict_recursive(self.model, entry)
            predictions += f' {predicted_value}'
            
            confusion_dict[f'{predicted_value}|{true_value}'] += 1
            if true_value == predicted_value:
                correct += 1
        
        print(f'[PREDICTIONS]: {predictions}')
        print(f'[ACCURACY]: {(correct / len(D)):.5f}')
        print(f'[CONFUSION_MATRIX]:')
        confusion = ''
        for f1 in sorted(self.final_feature):
            for f2 in sorted(self.final_feature):
                confusion += str(confusion_dict[f'{f2}|{f1}'])
                confusion += ' '
            confusion = confusion[:-1]
            confusion += '\n'
        confusion = confusion[:-1]
        print(confusion)

    def predict_recursive(self, node, entry):
        if isinstance(node, Leaf):
            return node.value

        value = entry[node.value]
        for n in node.subtrees:
            if n.value == value:
                return self.predict_recursive(n.subtrees[0], entry)
        
        # unseen
        l = {}
        for n in node.subtrees:            
            val = self.predict_recursive(n.subtrees[0], entry)
            if val not in l:
                l[val] = 1
            else:
                l[val] += 1

        l = collections.OrderedDict(sorted(l.items()))
        v = max(l, key=l.get)
        return v

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

    def print_tree(self):
        print('[BRANCHES]:')
        self.print_recursive_tree(self.model, 1, '')