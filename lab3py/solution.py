import sys
from util import Utils
from algorithm import ID3

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        train_dataset = Utils.parse_dataset(sys.argv[1])
        test_dataset = Utils.parse_dataset(sys.argv[2])
        if len(sys.argv) == 4:
            pass
        else:
            model = ID3(train_dataset, list(train_dataset[0].keys())[-1])
            m = model.fit(train_dataset, train_dataset, list(train_dataset[0].keys())[:-1], list(train_dataset[0].keys())[-1])
            model.print_tree()
            model.predict(test_dataset, list(test_dataset[0].keys())[-1])
    else:
        raise AttributeError("Wrong number of input parameters")
