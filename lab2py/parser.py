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
        
        #TODO(Dino): Concluscion may have many litterals
        goal = knowledge[num-1][0]
        if goal != '~':
            knowledge[num-1][0] = '~' + knowledge[num-1][0]
        else:
            knowledge[num-1][0] = knowledge[num-1][0][1:]
        knowledge_file.close()
        return knowledge, goal