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

def check_optimistic(heuristics, final_state, transition):
    is_optimistic = 'is'
    for h in sorted(heuristics):
        is_ok = 'ERR'
        hstar = Serach('ucs').search(h, transition, final_state, heuristics)[0].depth
        if heuristics[h] <= hstar:
            is_ok = 'OK'
        else:
            is_optimistic = 'is not'
        print(f'[CONDITION]: [{is_ok}] h({h}) <= h*: {heuristics[h]} <= {float(hstar)}')
    print(f'[CONCLUSION]: Heuristic {is_optimistic} optimistic.')

def check_consistent(heuristics, transition):
    is_consistent = 'is'
    for h1 in sorted(transition):
        for h2 in transition[h1]:
            is_ok = 'ERR'
            if heuristics[h1] <= heuristics[h2.state] + h2.depth:
                is_ok = 'OK'
            else:
                is_consistent = 'is not'
            print(f'[CONDITION]: [{is_ok}] h({h1}) <= h({h2.state}) + c: {heuristics[h1]} <= {heuristics[h2.state]} + {h2.depth}')
    print(f'[CONCLUSION]: Heuristic {is_consistent} consistent.')


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

    if alg is not None:
        s = Serach(alg)
        result, visited, path = s.search(start_state, transition, final_state, heuristics)
        print_solution(result, visited, path)

    if optimistic is not None:
        check_optimistic(heuristics, final_state, transition)
    
    if consistent is not None:
        check_consistent(heuristics, transition)
    