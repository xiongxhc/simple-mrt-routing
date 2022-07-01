
from collections import defaultdict
import re
from utils.utils import stationsPerLocation, locationPerStation, previousCurrentNext

class Graph:
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
  
    # Add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Return adjacency list {'NS2': ['NS1', 'NS3'],...}
    def createMrtSingleLineAdjacencyList(self, station):
      for previous, current, next in previousCurrentNext(station):
        if not previous:
          self.addEdge(current, next)
        elif not next:
          self.addEdge(current, previous)
        elif re.split('(\d+)', current)[0] == re.split('(\d+)', previous)[0]:
          self.addEdge(current, previous)
          self.addEdge(current, next)

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
  
  station = locationPerStation()
  location = stationsPerLocation()
  graph = Graph(len(station))
  graph.createMrtSingleLineAdjacencyList(station)
  graph.BFS_SP(input("Starting Station: "), input("Destination Station: "))