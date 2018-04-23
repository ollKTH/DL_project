import csv, sys

def read_oasis_csv(filename):

    _labels = {}

    with open(filename, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                _number = float(row[1])
                _labels[row[0]] = float(_number)
            except:
                print('Error!')

    return _labels