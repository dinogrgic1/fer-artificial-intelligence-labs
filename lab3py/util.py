class Utils:
    
    @staticmethod
    def parse_dataset(file_path):
        dataset_file = open(file_path)

        dataset = []
        keys = None
        parsedKeys = False
        
        for line in dataset_file:
            if parsedKeys == False:
               keys = line.strip().split(',')
               parsedKeys = True
               continue
            
            values = line.strip().split(',')
            entry = {}
            for i in range(0, len(keys)):
                entry[keys[i]] = values[i]
            dataset.append(entry) 
        return dataset

    @staticmethod
    def print_dataset(dataset):
        if dataset == None:
            return

        for key in dataset:
            print(f'{key} -- {dataset[key]}')
