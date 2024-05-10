from pysat.solvers import Solver

def find_modalities(modalities, attribute_constraints):
    """
    Find all sets of modalities that satisfy the given attribute constraints using a SAT solver.

    Args:
    - modalities (dict): A dictionary where keys are modality names and values are dictionaries of attributes.
    - attribute_constraints (dict): A dictionary where keys are attribute names and values are (min, max) pairs.

    Returns:
    - list of lists: Each sublist contains modality names that satisfy the constraints.
    """
    # Initialize the SAT solver
    solver = Solver(name='g4')

    # Assign a unique integer identifier to each modality
    modality_vars = {name: idx + 1 for idx, name in enumerate(modalities)}

    # Create clauses for each modality based on attribute constraints
    for name, attrs in modalities.items():
        var = modality_vars[name]
        
        for attr_name, (min_value, max_value) in attribute_constraints.items():
            # Ensure that the modality's attribute value is within the defined min and max range
            if attr_name in attrs:
                if attrs[attr_name] < min_value or attrs[attr_name] > max_value:
                    solver.add_clause([-var])
                    break

    # Ensure that at least one modality is selected
    solver.add_clause([var for var in modality_vars.values()])

    # To find all solutions that satisfy the constraints
    all_solutions = []

    while solver.solve():
        # Get the current solution as a list of selected modality variables
        model = solver.get_model()
        
        # Extract the modalities that are set to True
        selected_modalities = [name for name, var in modality_vars.items() if model[var - 1] > 0]
        all_solutions.append(selected_modalities)
        
        # Negate the current solution to ensure it's not found again
        solver.add_clause([-x for x in model if x > 0])

    # Clean up the solver instance
    solver.delete()

    return all_solutions

# Example usage:
modalities = {
    'Facial Recognition': {'Security': 9, 'Intrusiveness': 3, 'Privacy': 8},
    'Fingerprint': {'Security': 9, 'Intrusiveness': 2, 'Privacy': 8},
    'Password': {'Security': 8, 'Intrusiveness': 5, 'Privacy': 6},
    'PIN': {'Security': 8, 'Intrusiveness': 4, 'Privacy': 7},
    'Geolocation': {'Security': 7, 'Intrusiveness': 3, 'Privacy': 6}
}

# Attribute constraints (example)
attribute_constraints = {
    'Security': (6, 10),       # Min 6, Max 10
    'Intrusiveness': (0, 5),   # Min 0, Max 5
    'Privacy': (5, 10)         # Min 5, Max 10
}

# Find all solutions that meet the constraints
solutions = find_modalities(modalities, attribute_constraints)

# Print the results
for i, solution in enumerate(solutions, start=1):
    print(f"Solution {i}: {solution}")
