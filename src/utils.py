import re
import csv
from itertools import tee, islice, chain

# Returns {'Jurong East': ['NS1', 'EW24'],....}
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

def get_string_from_string_number(str):
  return re.split('(\d+)', str)[0]

def compare_split_string(a, b):
  if not a or not b:
    return False
  return get_string_from_string_number(a) == get_string_from_string_number(b)

def get_station_name(station):
  return location_per_station()[station]

def translate_route_to_sentence(routes):
  sentences = []
  for previous, current, next in previous_current_next(routes):
    if not next:
        return sentences
    else:
      if compare_split_string(current, next):
        sentences.append("Take " +  get_string_from_string_number(current) + " line from " + get_station_name(current)+ " to " + get_station_name(next))
      else:
        sentences.append("Change from " + get_string_from_string_number(current) + " line to " + get_string_from_string_number(next) + " line")

def print_output(start, destination, new_path):
      print("\nTravel from", get_station_name(start), "to", get_station_name(destination))
      print("Stations travelled:", len(new_path))
      print("Route: (", *new_path, ")\n")
      for sentence in translate_route_to_sentence(new_path):
        print(sentence)