class Parser:
    
    @staticmethod
    def parse_knowledge_file(file_path, goal):
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
        
        goal_arr = []
        if goal == True:
            goal_arr = knowledge.pop(num-1)
            Parser.knowledge_add_goal(knowledge, goal_arr)
        
        knowledge_file.close()
        return knowledge, ' v '.join(goal_arr)
    
    @staticmethod
    def knowledge_add_goal(knowledge, goals):
        num = len(knowledge) + 1

        for lit in goals:
            if lit[0] != '~':
                lit = '~' + lit
            else:
                lit = lit[1:]
            knowledge[num] = [lit]
            num += 1

    @staticmethod
    def knowledge_remove_clause(knowledge, clauses):
        for k in knowledge:
            if knowledge[k] == clauses:
                del knowledge[k]
                break
    
    @staticmethod
    def knowledge_add_clause(knowledge, clauses):
        sos_num = list(knowledge.items())[-1][0]
        knowledge[sos_num + 1] = clauses

    @staticmethod
    def parse_input_file(file_path):
        input_file = open(file_path)
        idx = 0
        goal = dict()
        
        for line in input_file:
            format_line = line.lower().strip()
            command = format_line[-1]
            format_line = format_line[:-1].strip()

            if command == '?':
                goal[f'?{idx}'] = format_line.split(' v ')
            elif command == '+':
                goal[f'+{idx}'] = format_line.split(' v ')
            elif command == '-':
                goal[f'-{idx}'] = format_line.split(' v ')
            else:
                raise Exception('Comamnd not found.')
            idx += 1

        input_file.close()
        return goal