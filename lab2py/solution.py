import sys
from parser import Parser
from resolution import Resoltuion

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        system = sys.argv[1]
        #input_file = sys.argv[3]
        knowledge, goal = Parser.parse_knowledge_file(sys.argv[2])
    else:
        raise AttributeError("Wrong number of input parameters")

    sos = dict()
    Resoltuion.resolution(knowledge, sos, goal)
    Resoltuion.print_resolution(knowledge, sos, goal)
