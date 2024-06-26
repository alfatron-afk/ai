import heapq

class Node:
    def __init__(self, position, parent, g, h):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, Node(start, None, 0, heuristic(start, goal)))
    closed_set = set()
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if current.position == goal:
            return reconstruct_path(current)
        
        closed_set.add(current.position)
        
        for neighbor in get_neighbors(current.position):
            if neighbor in closed_set:
                continue
            
            new_g = current.g + 1
            new_h = heuristic(neighbor, goal)
            new_f = new_g + new_h
            
            if not any(node.position == neighbor for node in open_set) or new_f < get_node(open_set, neighbor).f:
                heapq.heappush(open_set, Node(neighbor, current, new_g, new_h))
    
    return None

def reconstruct_path(current):
    path = []
    while current is not None:
        path.append(current.position)
        current = current.parent
    path.reverse()
    return path

def heuristic(position, goal):
    # Manhattan distance heuristic
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def get_neighbors(position):
    # Get all possible neighbors of the given position
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:  # Exclude the position itself
                neighbor = (position[0] + i, position[1] + j)
                if 0 <= neighbor[0] < width and 0 <= neighbor[1] < height and grid[neighbor[0]][neighbor[1]] != 1:
                    neighbors.append(neighbor)
    return neighbors

def get_node(nodes, position):
    for node in nodes:
        if node.position == position:
            return node
    return None

# Example usage:
width = 10
height = 10
grid = [[0 for i in range(width)] for j in range(height)]
grid[1][1] = 1  # Example obstacle
start = (0, 0)
goal = (9, 9)

path = a_star(start, goal)

if path is not None:
    print("Path found:", path)
else:
    print("No path found")
