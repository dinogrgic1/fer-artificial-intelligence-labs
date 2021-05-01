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
        goal_size = len(goal.split(' v '))

        for rule in sos.items():
            if rule[0] - goal_size >= len(knowledge) - 1:
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
    def is_redundant(rule1, r1, rule2, r2):
        rs1 = set(rule1)
        rs2 = set(rule2)

        if rs1.issubset(rs2):
            return r2
        elif rs2.issubset(rs1):
            return r1
        else:
            return -1

    @staticmethod
    def remove_redundant(rule1, rule2):
        tmp = []
        rule1cp = copy.deepcopy(rule1)
        rule2cp = copy.deepcopy(rule2)
        for r1 in rule1cp:
            for r2 in rule2cp:
                is_r = Resoltuion.is_redundant(rule1[r1], r1, rule2[r2], r2)
                if is_r != -1:
                    tmp.append(is_r)
        return tmp

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
                    else:
                        tmp.append(rule1cp + rule2cp)
        return tmp

    @staticmethod
    def resolution(knowledge, sos, goal):
        knowledge_cpy = copy.deepcopy(knowledge)

        sos_num = len(knowledge_cpy)
        goal_disj = len(goal.split(' v '))
        checked = []

        for i in range(sos_num - goal_disj + 1, sos_num + 1):
            t = knowledge_cpy.pop(i)
            sos[i] = t

        sos_num += 1
        sos_list = list(sos.keys())
        out = []

        for r1 in sos_list:
            if r1 in out:
                continue

            new = []
            rule1 = sos[r1]
            skip = False
            knowledge_and_sos = list(knowledge_cpy.keys()) + sos_list

            for r2 in knowledge_and_sos:
                if r2 in out:
                    continue

                if r2 <= len(knowledge) - goal_disj:
                    rule2 = knowledge_cpy[r2]
                else:
                    rule2 = sos[r2]

                if r1 != r2 and (r1, r2) not in checked:
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

                        if resolvents[0] in sos.values():
                            skip = True
                            continue

                        new.append(resolvents)
                        checked.append((r1, r2))

            if skip == True:
                continue

            for n in new:
                if n not in sos.items():
                    sos[sos_num] = n[0]
                    sos_list.append(sos_num)
                    sos_num += 1
            out.extend(Resoltuion.remove_redundant(sos, knowledge_cpy))
