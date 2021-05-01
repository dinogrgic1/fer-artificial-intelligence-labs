class Parser:
    
    @staticmethod
    def parse_knowledge_file(file_path):
        knowledge_file = open(file_path)
        knowledge = {}
        num = 1

        for line in knowledge_file:
            if line.strip()[0] == '#':
                continue
            line = line.lower().strip()
            line = line.split(' v ')
            
            for i in range(0, len(line)):
                line[i] = line[i].strip()
            
            knowledge[num] = line
            num += 1
        
        goal_arr = knowledge.pop(num-1)
        num -= 1
        goal = ' v '.join(goal_arr)

        for lit in goal_arr:
            if lit[0] != '~':
                lit = '~' + lit
            else:
                lit = lit[1:]
            knowledge[num] = [lit]
            num += 1
        knowledge_file.close()
        return knowledge, goal