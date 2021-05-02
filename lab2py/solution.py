import sys
import copy

from parser import Parser
from resolution import Resoltuion

if __name__ == "__main__":
    if sys.argv[1] == 'resolution' and len(sys.argv) == 3:
        knowledge, goal = Parser.parse_knowledge_file(sys.argv[2], True)
        sos = dict()
        checked, out = Resoltuion.resolution(knowledge, sos, goal)
        Resoltuion.print_resolution(knowledge, sos, goal, checked, out)

    
    elif sys.argv[1] == 'cooking' and len(sys.argv) == 4:
        knowledge, goal = Parser.parse_knowledge_file(sys.argv[2], False)
        commands = Parser.parse_input_file(sys.argv[3])
        Resoltuion.print_knowledge(knowledge)

        for command in commands:
            joined = ' v '.join(commands[command])
            print(f'User\'s command: {joined} {command[0]}')
            if command[0] == '?':
                sos = dict()
                tmp_knowledge = copy.deepcopy(knowledge)
                Parser.knowledge_add_goal(tmp_knowledge, commands[command])
                checked, out = Resoltuion.resolution(tmp_knowledge, sos, joined)
                Resoltuion.print_resolution(tmp_knowledge, sos, joined, checked, out)
            elif command[0] == '+':
                Parser.knowledge_add_clause(knowledge, commands[command])
                print(f'Added {joined}')
            elif command[0] == '-':
                Parser.knowledge_remove_clause(knowledge, commands[command])
                print(f'Removed {joined}')
            print()

    else:
        raise AttributeError("Wrong number of input parameters")

    