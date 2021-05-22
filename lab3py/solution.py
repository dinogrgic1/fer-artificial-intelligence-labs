import sys
from util import Utils
from algorithm import ID3

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        train_dataset = Utils.parse_dataset(sys.argv[1])
        test_dataset = Utils.parse_dataset(sys.argv[2])

        model = ID3()
        if len(sys.argv) == 4:
            m = model.fit(train_dataset, sys.argv[3])
        else:
            m = model.fit(train_dataset)
        model.print_tree()
        model.predict(test_dataset, list(test_dataset[0].keys())[-1])
    else:
        raise AttributeError("Wrong number of input parameters")
