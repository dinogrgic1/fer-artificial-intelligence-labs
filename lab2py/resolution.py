import copy

class Resoltuion:

    @staticmethod
    def check_tautology(list):
        if len(list) == 2:
            if list[0] == '~' + list[1] or '~' + list[0] == list[1]:
                return True
        return False

    @staticmethod
    def print_resolution(knowledge, sos, goal):
        is_true = False
        for rule in knowledge:
            conj = ' v '.join(knowledge[rule])
            print(f'{rule}. {conj}')
        print('===============')
        for rule in sos.items():
            if rule[0] != len(knowledge):
                if rule[1] == []:
                    conj = 'NIL'
                    is_true = True
                else:
                    conj = ' v '.join(rule[1])
                print(f'{rule[0]}. {conj}')
        print('===============')

        if is_true == True:
            print(f'[CONCLUSION]: {goal} is true')
        else:
            print(f'[CONCLUSION]: {goal} is unknown')

    @staticmethod
    def resolve(rule1, rule2):
        tmp = None
        for r1 in rule1:
            symb_tmp = str(r1)
            if symb_tmp[0] != '~':
                symb_tmp = '~' + symb_tmp
            else:
                symb_tmp = symb_tmp[1:]

            for r2 in rule2:
                if symb_tmp == r2:
                    rule1cp = copy.deepcopy(rule1)
                    rule2cp = copy.deepcopy(rule2)
                    rule2cp.remove(r2)
                    rule1cp.remove(r1)
                    if tmp == None:
                        tmp = [rule1cp + rule2cp]
                        #print(rule1cp + rule2cp)
                    else:
                        tmp.append(rule1cp + rule2cp)
        return tmp

    @staticmethod
    def resolution(knowledge, sos):
        knowledge_cpy = copy.deepcopy(knowledge)

        sos_num = len(knowledge_cpy)
        sos[sos_num] = knowledge_cpy[sos_num]
        sos_num += 1
        checked = []

        sos_list = list(sos.keys())
        for r1 in sos_list:
            new = []
            rule1 = sos[r1]
            knowledge_and_sos = list(knowledge.keys()) + sos_list
            for r2 in knowledge_and_sos:
                if r2 > len(knowledge):
                   rule2 = sos[r2]
                else:
                   rule2 = knowledge_cpy[r2]

                if r1 != r2 and r1 not in checked and r2 not in checked:
                    resolvents = Resoltuion.resolve(rule1, rule2)

                    if resolvents == []:
                        checked.append(r1)
                        checked.append(r2)
                        sos[sos_num] = []
                        sos_num += 1
                        return
                    elif resolvents != None:
                        if len(resolvents) > 1:
                            continue
                        new.append(resolvents)
                        checked.append(r1)
                        checked.append(rule2[0])

            if new == []:
                return

            if sos_num == 30:
                break
            sos[sos_num] = new[0][0]
            sos_list.append(sos_num)
            sos_num += 1 