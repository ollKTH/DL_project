import sys
from csv_read import *
from read_images import *

if __name__ == '__main__':

    filename = 'C:/Users/Olle Andersson/PycharmProjects/DL_project_1/labels/labels.csv'
    labels = read_oasis_csv(filename)