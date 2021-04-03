import sys
from Serach import Serach
from Parser import Parser

def print_solution(result, visited, path):
    print(f'[FOUND_SOLUTION]: {result is not None}')
    print(f'[STATES_VISITED]: {len(visited)}')
    print(f'[PATH_LENGTH]: {len(path)}')
    print(f'[TOTAL_COST]: {result.depth}')
    print(f'[PATH]: {path}')

if __name__ == '__main__':

    alg, ss, h, optimistic, consistent = Parser.parse_args(sys.argv[1:])
    start_state, final_state, transition = Parser.parse_state_space_file(ss)
    if h is not None:
        heuristics = Parser.parse_heuristic_value_file(h)

    s = Serach(alg)
    result, visited, path = s.search(start_state, transition, final_state)
    print_solution(result, visited, path)
