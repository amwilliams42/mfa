from pysat.solvers import Solver

def find_factors(factors, attribute_constraints):
    """
    Find all sets of factors that satisfy the given attribute constraints using a SAT solver.

    Args:
    - factors (dict): A dictionary where keys are factor names and values are dictionaries of attributes.
    - attribute_constraints (dict): A dictionary where keys are attribute names and values are (min, max) pairs.

    Returns:
    - list of lists: Each sublist contains factor names that satisfy the constraints.
    """
    # Initialize the SAT solver
    solver = Solver(name='g4')

    # Assign a unique integer identifier to each factor
    factor_vars = {name: idx + 1 for idx, name in enumerate(factors)}

    # Create clauses for each factor based on attribute constraints
    for name, attrs in factors.items():
        var = factor_vars[name]
        
        for attr_name, (min_value, max_value) in attribute_constraints.items():
            # Ensure that the factor's attribute value is within the defined min and max range
            if attr_name in attrs:
                if attrs[attr_name] < min_value or attrs[attr_name] > max_value:
                    solver.add_clause([-var])
                    break

    solver.add_clause([var for var in factor_vars.values()])
    all_solutions = []

    while solver.solve():
        # Get the current solution as a list of selected factor variables
        model = solver.get_model()
        
        # Extract the factors that are set to True
        selected_factors = [name for name, var in factor_vars.items() if model[var - 1] > 0]
        all_solutions.append(selected_factors)
        
        # Negate the current solution to ensure it's not found again
        solver.add_clause([-x for x in model if x > 0])

    # Clean up the solver instance
    solver.delete()

    return all_solutions
