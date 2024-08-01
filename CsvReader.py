import csv

"""Takes a csv file delimited by * then turns it into a dictionary that can be used"""


def read_csv(files):  # files needs to be a list
    mh = {}

    for file in files:
        with open(file, 'r', newline='') as csvfile:
            cr = csv.reader(csvfile, delimiter='*')
            for line in cr:
                lis = line[0].split('*')
                #  print(lis)
                key = lis.pop(0)
                # print(key)
                # print(lis)
                mh[key] = lis
    return mh


class CsvReader:
    all_files = ["writeTest.csv"]

    read_csv(all_files)
