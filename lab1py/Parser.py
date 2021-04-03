from State import State

class Parser:
    
    @staticmethod
    def parse_state_space_file(file_path):
        '''Parses state space file

        Args:
            file_path (string): String to state space file.

        Returns:
            tuple: (start_state, final_state, transition)
        '''

        state_space_file = open(file_path)
        line_num = -1
        start_state = final_state = None
        transition = {}

        for line in state_space_file:
            if line.strip()[0] == '#':
                continue
            line_num += 1

            if line_num == 0:
                start_state = line.strip()
            elif line_num == 1:
                final_state = line.strip().split(' ')
            else:
                splited = line.strip().split(':')
                begin_state = splited[0]
                if splited[1] == '':
                    continue
                else:
                    finish_states = splited[1].strip().split(" ")

                for state in finish_states:
                    if begin_state not in transition:
                        transition[begin_state] = []
                    state_split = state.split(',')
                    s = State(state_split[0], float(state_split[1]))
                    transition[begin_state].append(s)
                transition[begin_state] = sorted(transition[begin_state], key=lambda p: p.state)
        state_space_file.close()
        return (start_state, final_state, transition)

    @staticmethod
    def parse_heuristic_value_file(file_path):
        """Parses heuristic value file

        Args:
            file_path (string): String to state space file.

        Returns:
            dictioniary: Heuristics dictioniary
        """
        heuristics_file = open(file_path)
        heuristics = {}
        for line in heuristics_file:
            if line[1] == '#':
                continue
            strip = line.strip().split(":")
            heuristics[strip[0]] = int(strip[1].strip())
        heuristics_file.close()
        return heuristics

    @staticmethod
    def parse_args(args):
        """Parses arguments of solution.py

        Args:
            args (list): List of arguments passed into solution.py.

        Returns:
            tuple: (alg, ss, h, optimistic, consistent)
        """
        alg = ss = h = optimistic = consistent = None
        flag = None
        for arg in args:
            if '--' in arg:
                flag = arg
            else:
                if flag == '--alg':
                    alg = arg
                elif flag == '--ss':
                    ss = arg
                elif flag == '--h':
                    h = arg
                elif flag == '--check-optimistic':
                    optimistic = arg
                elif flag == '--check-consistent':
                    consistent = arg
        return (alg, ss, h, optimistic, consistent)