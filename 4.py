import heapq

class Graph:
    def __init__(self, graph, heuristicNodeList, startNode):
        # Instantiate graph object with graph topology, heuristic values, and start node.
        self.graph = graph
        self.heuristicNodeList = heuristicNodeList
        self.startNode = startNode

    def ao_star_search(self, goal_node):
        open_set = [(0, self.startNode)]  # Initialize open set with the start node and cost 0
        closed_set = set()  # Initialize closed set
        while open_set:
            current_cost, current_node = heapq.heappop(open_set)
            if current_node in closed_set:
                continue
            closed_set.add(current_node)
            if current_node == goal_node:
                # Goal reached
                return current_cost
            # Expand neighbors
            for neighbor, edge_cost in self.graph.get(current_node, []):
                if neighbor not in closed_set:
                    # Calculate f(n) for the neighbor
                    f_value = current_cost + edge_cost + self.heuristicNodeList.get(neighbor, 0)
                    heapq.heappush(open_set, (f_value, neighbor))
        return float('inf')  # No path found

# Example usage
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
heuristics = {'A': 1, 'B': 5, 'C': 2, 'D': 4}
start_node = 'A'
goal_node = 'D'

graph = Graph(adjacency_list, heuristics, start_node)
result = graph.ao_star_search(goal_node)

if result != float('inf'):
    print(f"Optimal path cost from {start_node} to {goal_node}: {result}")
else:
    print("No path found.")
