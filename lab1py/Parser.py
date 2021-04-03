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
        line_num = 0
        start_state = final_state = None
        transition = {}

        for line in state_space_file:
            if line[1] == '#':
                continue

            if line_num == 0:
                start_state = line.strip()
            elif line_num == 1:
                final_state = line.strip().split(' ')
            else:
                splited = line.strip().split(':')
                start_state = splited[0]
                finish_states = splited[1].split(" ")
                transition[start_state] = finish_states[1:]
            line_num += 1
        state_space_file.close()
        return (start_state, final_state, transition)

    @staticmethod
    def parse_heuristic_value_file(file_path):
        """[summary]

        Args:
            file_path ([type]): [description]

        Returns:
            [type]: [description]
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
        """[summary]

        Args:
            args ([type]): [description]

        Returns:
            [type]: [description]
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