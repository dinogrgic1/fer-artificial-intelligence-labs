import sys
from Serach import Serach
from Parser import Parser

def print_solution(result, visited, path):
    solution = 'no'
    if result is not None:
        solution = 'yes'
    print(f'[FOUND_SOLUTION]: {solution}')
    print(f'[STATES_VISITED]: {len(visited)}')
    print(f'[PATH_LENGTH]: {len(path)}')
    print(f'[TOTAL_COST]: {result.depth}')
    
    #print(heuristics)
    path_str = str(path.pop(0).state)
    for p in path:
        path_str += f' => {p.state}'
    print(f'[PATH]: {path_str}')
    #print(path)

if __name__ == '__main__':
    alg, ss, h, optimistic, consistent = Parser.parse_args(sys.argv[1:])
    start_state, final_state, transition = Parser.parse_state_space_file(ss)
    if h is not None:
        heuristics = Parser.parse_heuristic_value_file(h)
        
        for t in transition:
            for s in transition[t]:
                s.h = heuristics[t]
    else:
        heuristics = None

    s = Serach(alg)
    result, visited, path = s.search(start_state, transition, final_state, heuristics)
    print_solution(result, visited, path)
