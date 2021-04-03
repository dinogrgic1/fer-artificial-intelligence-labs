import sys
from Parser import Parser

if __name__ == '__main__':
    try:
        alg, ss, h, optimistic, consistent = Parser.parse_args(sys.argv[1:])
        start_state, final_state, transition = Parser.parse_state_space_file(ss)
        heuristics = Parser.parse_heuristic_value_file(h)
    except Exception as e:
        print(e)
