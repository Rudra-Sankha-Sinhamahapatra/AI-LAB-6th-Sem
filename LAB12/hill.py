import random
import math

def objective_function(x):
    """
    Example objective function to maximize.
    Here we use a simple quadratic function: -(x-2)^2 + 4
    The maximum is at x = 2 with value 4
    """
    return -(x - 2)**2 + 4

def generate_neighbor(current_state, step_size=0.1):
    """
    Generate a neighbor solution by adding or subtracting a small random value
    """
    return current_state + random.uniform(-step_size, step_size)

def hill_climbing(
    objective_function,
    initial_state,
    max_iterations=1000,
    step_size=0.1,
    tolerance=1e-6
):
    """
    Implementation of hill climbing algorithm
    
    Parameters:
    - objective_function: Function to maximize
    - initial_state: Starting point
    - max_iterations: Maximum number of iterations
    - step_size: Size of the step to take when generating neighbors
    - tolerance: Minimum improvement required to continue
    
    Returns:
    - best_state: The best solution found
    - best_value: The value of the best solution
    """
    current_state = initial_state
    current_value = objective_function(current_state)
    
    for i in range(max_iterations):
        # Generating a neighbor
        neighbor = generate_neighbor(current_state, step_size)
        neighbor_value = objective_function(neighbor)
        
        # If the neighbor is better, move to it
        if neighbor_value > current_value:
            current_state = neighbor
            current_value = neighbor_value
        else:
            # If no improvement, we might be at a local maximum
            break
            
    return current_state, current_value

def main():
    # Setting  random seed for reproducibility
    random.seed(42)
    
    # Starting point
    initial_state = 0
    
    # Running hill climbing
    best_state, best_value = hill_climbing(
        objective_function=objective_function,
        initial_state=initial_state
    )
    
    print(f"Starting point: {initial_state}")
    print(f"Best solution found: x = {best_state:.6f}")
    print(f"Best value found: f(x) = {best_value:.6f}")

if __name__ == "__main__":
    main()
