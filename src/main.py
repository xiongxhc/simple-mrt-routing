from collections import defaultdict
from utils.utils import stations_per_location, location_per_station, previous_current_next, compare_split_string

class Graph:
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
  
    # Add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Return adjacency list {'NS2': ['NS1', 'NS3'],...}
    def create_mrt_single_line_adjacency_list(self, station):
      for previous, current, next in previous_current_next(station):
        if not previous:
          self.add_edge(current, next)
        elif not next:
          self.add_edge(current, previous)
        elif compare_split_string(current, previous):
          self.add_edge(current, previous)
          self.add_edge(current, next)
    
    # Return adjacency list {'NS2': ['NS1', 'NS3'],...}
    def create_mrt_connected_station_adjacency_list(self, location):
      for stations in location:
        if len(location[stations]) > 1:
          self.create_mrt_single_line_adjacency_list(location[stations])
        
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
                        print("\nTravel from", start, "to", destination)
                        print("Stations travelled:", len(new_path))
                        print("Route: (", *new_path, ")\n")
                        return
                visited.append(station)
 
        print("\n NO PATH BETWEEN STATION (NOT POSSIBLE)\n")
        return
    
if __name__ == "__main__":
  
  station = location_per_station()
  location = stations_per_location()
  graph = Graph(len(station))
  graph.create_mrt_single_line_adjacency_list(station)
  graph.create_mrt_connected_station_adjacency_list(location)
  graph.print_mrt_adjacency_list()
  graph.BFS_SP(input("Starting Station: "), input("Destination Station: "))