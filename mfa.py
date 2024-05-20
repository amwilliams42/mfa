import json
import importlib
from sat_updated import solve_with_constraints, load_constraints

# Function to dynamically load and evaluate factors from Python files
def load_and_evaluate_factors(factor_modules, env, device, context):
    factors = {}
    for module_name in factor_modules:
        # Dynamically import the factor's evaluation function from the `factors` subfolder
        module = importlib.import_module(f"factors.{module_name}")
        evaluate_function = getattr(module, 'evaluate')
        factors[module_name] = evaluate_function(env, device, context)
    return factors


# Function that integrates the dynamic loading and SAT solver
def evaluate_and_select_factors(json_file, factor_modules):
    """
    Evaluate the factor functions based on environment, device, and context variables from a JSON file,
    then pass the values into the SAT solver to find suitable factor combinations.

    Args:
    - json_file (str): Path to the JSON file containing environment, device, and context variables.
    - factor_modules (list of str): List of factor module names to import.

    Returns:
    - List of lists containing all solutions that satisfy the constraints.
    """
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Evaluate the factors using the provided variables
    environment = data['environment']
    device = data['device']
    context = data['context']
    factors = load_and_evaluate_factors(factor_modules, environment, device, context)

    # attribute_constraints = attribute_constraints_function(environment,device,context)
    # Use the SAT solver function to find valid factor combinations
   # return find_factors(factors, attribute_constraints)
    
    rules = load_constraints("constraints.json")
    result = solve_with_constraints(factors, rules)
    return result