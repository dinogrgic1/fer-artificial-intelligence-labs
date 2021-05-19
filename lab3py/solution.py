from util import Utils
from algorithm import ID3

if __name__ == '__main__':
    train_dataset = Utils.parse_dataset("datasets/volleyball.csv")
    test_dataset = Utils.parse_dataset("datasets/volleyball_test.csv")

    model = ID3(train_dataset, list(train_dataset[0].keys())[-1])
    m = model.fit(train_dataset, train_dataset, list(train_dataset[0].keys())[:-1], list(train_dataset[0].keys())[-1])
    model.print()