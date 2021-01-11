import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Name of the csv file containing CSV datas")
args = parser.parse_args()
print(args.file)
with open(args.file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    for row in spamreader:
        print(', '.join(row))
