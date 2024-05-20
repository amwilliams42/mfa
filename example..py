from pysat.formula import CNF
from pysat.solvers import Solver
import json

def solve_with_constraints(factors, constraints):
    # Create a new CNF formula
    formula = CNF()

    # Define Boolean variables for each authentication factor
    variables = {}
    for i, factor in enumerate(factors, start=1):
        variables[factor] = i

    print(variables)

    # Add clauses to the formula based on the dynamic constraints
    for constraint in constraints:
  
        condition = constraint["condition"]
        implication = constraint["implication"]
        print(f"cond {condition}")
        print(f"impl {implication}")

        # Parse condition and implication expressions
        condition_clauses = parse_expression(condition, factors, variables)
        implication_clauses = parse_expression(implication, factors, variables)

        # Add clauses to the formula
        for clause in condition_clauses:
            formula.append(clause)
        for clause in implication_clauses:
            formula.append(clause)

    print(formula)

    # Create a solver instance and add the CNF formula
    solver = Solver(bootstrap_with=formula.clauses)

    # Solve the SAT problem
    if solver.solve():
        model = solver.get_model()
        selected_factors = [factor for factor, variable in variables.items() if variable in model]
        print(selected_factors)
        print(model)
        return selected_factors
    else:
        return None
    
def parse_expression(expr, factors, variables):
    clauses = []
    if expr:
        conditions = expr.split("and")
        for condition in conditions:
            parts = condition.strip().split()
            score_type = parts[0]
            operator = parts[1]
            value = int(parts[2])

            for factor, scores in factors.items():
                if score_type in scores:
                    score = scores[score_type]
                    variable = variables[factor]
                    if operator == ">":
                        if score <= value:
                            clauses.append([-variable])
                    elif operator == "<":
                        if score >= value:
                            clauses.append([-variable])
    print(clauses)
    return clauses

def run_test_case(factors, constraints, expected_result):
    selected_factors = solve_with_constraints(factors, constraints)
    print(f"Input factors: {factors}")
    print(f"Input constraints: {constraints}")
    print(f"Expected result: {expected_result}")
    print(f"Actual result: {selected_factors}")
    print("Test passed:", selected_factors == expected_result)
    print()

def main():
    # Load test cases from the JSON file
    with open("test_cases.json") as file:
        test_cases = json.load(file)

    for i, test_case in enumerate(test_cases, start=1):
        print(f"Running Test Case {i}:")
        run_test_case(test_case["factors"], test_case["constraints"], test_case["expected_result"])

if __name__ == "__main__":
    main()