import sys


def parse_state_space_file():
    pass

def parse_args(args):
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

if __name__ == '__main__':
    alg, ss, h, optimistic, consistent = parse_args(sys.argv[1:])
    print(alg, ss, h, optimistic, consistent)