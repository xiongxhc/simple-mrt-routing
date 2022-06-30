def BFS_SP(graph, start, destination):
    visited = []
    queue = [[start]]

    if start not in graph:
      print("\nInvalid [Start] Station!\n")
      return
    elif destination not in graph:
      print("\nInvalid [Destination] Station!\n")
      return
     
    if start == destination:
        print("\nSame Station\n")
        return
     
    while queue:
        path = queue.pop(0)
        station = path[-1]
         
        if station not in visited:
            neighbours = graph[station]
             
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
     
    graph = {"X": ["Y", "A", "Z"],
            "Y": ["X", "Y", "W"],
            "Z": ["X", "S", "D"],
            "W": ["Y", "W"],
            "A": ["Y", "D", "Z"],
            "S": ["Z", "D"],
            "D": ["Z", "K", "L"]}

    BFS_SP(graph, input("Starting Station: "), input("Destination Station: "))