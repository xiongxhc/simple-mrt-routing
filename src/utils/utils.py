import csv
from itertools import tee, islice, chain

# Returns {'Station Name': ['NS1', 'EW24'],....}
def stationsPerLocation():
  dic = dict()
  with open("src/data/station_map.csv", "r") as file:
      csvreader = csv.reader(file)
      next(csvreader)
      for row in csvreader:
        if row[1] in dic:
          dic[row[1]].append(row[0])
        else:
          dic[row[1]] = [row[0]]
  return dic

# Returns {'NS1': 'Jurong East',....}
def locationPerStation():
  dic = dict()
  with open("src/data/station_map.csv", "r") as file:
      csvreader = csv.reader(file)
      next(csvreader)
      for row in csvreader:
          dic[row[0]] = row[1]
  return dic

def previousCurrentNext(iterable):
    prev, curr, next = tee(iterable, 3)
    prev = chain([None], prev)
    next = chain(islice(next, 1, None), [None])
    return zip(prev, curr, next)