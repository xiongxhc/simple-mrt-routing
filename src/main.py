from collections import defaultdict
from utils import (
  stations_per_location, 
  location_per_station, 
  previous_current_next, 
  compare_split_string, 
  print_output
)

class MRT_GRAPH:
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
  
    # Add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Return adjacency list {'NS1': ['NS2'],...}
    def create_mrt_single_line_adjacency_list(self, stations):
      for previous, current, next in previous_current_next(stations):
        if not previous:
          self.add_edge(current, next)
          continue
        if not next:
          self.add_edge(current, previous)
          continue
        if compare_split_string(current, previous):
          self.add_edge(current, previous)
        if compare_split_string(current, next):
          self.add_edge(current, next)
            
    # Return adjacency list {'NS1': ['NS2', 'EW24'],...}
    def create_mrt_connected_station_adjacency_list(self, locations):
      for stations in locations:
        if len(locations[stations]) > 1:
          for previous, current, next in previous_current_next(locations[stations]):
            if not previous:
              self.add_edge(current, next)
              continue
            if not next:
              self.add_edge(current, previous)
              continue
            self.add_edge(current, previous)
            self.add_edge(current, next)
              
        
    def print_mrt_adjacency_list(self):
        print(self.graph)

    # Breadth first search shortest path to determine route
    def BFS_SP(self, start, destination):
        visited = []
        queue = [[start]]

        if start not in self.graph:
          print("\nInvalid [Start] Station!\n")
          return
        elif destination not in self.graph:
          print("\nInvalid [Destination] Station!\n")
          return
        
        if start == destination:
            print("\nSame Station\n")
            return
        
        while queue:
            path = queue.pop(0)
            station = path[-1]
            
            if station not in visited:
                neighbours = self.graph[station]
                
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    
                    if neighbour == destination:
                      print_output(start, destination, new_path)
                      return
                visited.append(station)
 
        print("\n NO PATH BETWEEN STATION (NOT POSSIBLE)\n")
        return
    
if __name__ == "__main__":
  
  stations = location_per_station()
  locations = stations_per_location()
  graph = MRT_GRAPH(len(stations))
  graph.create_mrt_single_line_adjacency_list(stations)
  graph.create_mrt_connected_station_adjacency_list(locations)
  graph.print_mrt_adjacency_list()
  graph.BFS_SP(input("\nStarting Station: "), input("Destination Station: "))