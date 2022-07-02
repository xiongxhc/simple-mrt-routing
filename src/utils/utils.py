import re
import csv
from itertools import tee, islice, chain

# Returns {'Station Name': ['NS1', 'EW24'],....}
def stations_per_location():
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
def location_per_station():
  dic = dict()
  with open("src/data/station_map.csv", "r") as file:
      csvreader = csv.reader(file)
      next(csvreader)
      for row in csvreader:
          dic[row[0]] = row[1]
  return dic

def previous_current_next(iterable):
    prev, curr, next = tee(iterable, 3)
    prev = chain([None], prev)
    next = chain(islice(next, 1, None), [None])
    return zip(prev, curr, next)

def compare_split_string(a, b):
  return re.split('(\d+)', a)[0] == re.split('(\d+)', b)[0]