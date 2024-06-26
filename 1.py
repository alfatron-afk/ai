def solveWaterJugProblem(capacity_jug1, capacity_jug2, desired_quantity):
    if desired_quantity > capacity_jug1 + capacity_jug2:
        return "No solution found"

    stack = []
    visited = set()
    stack.append((0, 0))  # Initial state: both jugs empty
    visited.add((0, 0))
    
    while stack:
        current_state = stack.pop()
        
        if current_state[0] == desired_quantity or current_state[1] == desired_quantity:
            return current_state
        
        next_states = generateNextStates(current_state, capacity_jug1, capacity_jug2)
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                stack.append(state)
    
    return "No solution found"

def generateNextStates(state, capacity_jug1, capacity_jug2):
    next_states = []
    
    # Fill Jug 1
    next_states.append((capacity_jug1, state[1]))
    
    # Fill Jug 2
    next_states.append((state[0], capacity_jug2))
    
    # Empty Jug 1
    next_states.append((0, state[1]))
    
    # Empty Jug 2
    next_states.append((state[0], 0))
    
    # Pour water from Jug 1 to Jug 2
    pour_amount = min(state[0], capacity_jug2 - state[1])
    next_states.append((state[0] - pour_amount, state[1] + pour_amount))
    
    # Pour water from Jug 2 to Jug 1
    pour_amount = min(state[1], capacity_jug1 - state[0])
    next_states.append((state[0] + pour_amount, state[1] - pour_amount))
    
    return next_states

# Example usage:
solution = solveWaterJugProblem(4, 3, 2)
print("Solution:", solution)
