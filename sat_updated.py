import json
from sympy import symbols, sympify
from pysat.solvers import Glucose3

def load_constraints(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['rules']

def evaluate_condition(condition, scores):
    try:
        # Create symbols for each score
        symbols_dict = {key: symbols(key) for key in scores}
        # Replace dictionary-style access with symbols
        for key in scores:
            condition = condition.replace(f"scores['{key}']", key)
        # Parse the condition using sympy
        condition = sympify(condition).subs(symbols_dict)
        for key, value in scores.items():
            condition = condition.subs(symbols_dict[key], value)
        return bool(condition)
    except Exception as e:
        print(f"Error evaluating condition {condition}: {e}")
        return False
def apply_constraints(rules, scores):
    for rule in rules:
        if evaluate_condition(rule['condition'], scores):
            for key, constraint in rule['constraints'].items():
                if not evaluate_condition(f"scores['{key}'] {constraint}", scores):
                    return False
    return True

def modality_to_clauses(name, scores, rules):
    clauses = []
    if apply_constraints(rules, scores):
        # Add a clause for each modality that passes the constraints
        clauses.append(name)
    return clauses

def solve_with_constraints(modalities, rules):
    solver = Glucose3()
    clause_to_modality = {}
    idx = 1
    
    # Map each modality to an index and add corresponding clauses
    for name, scores in modalities.items():
        clauses = modality_to_clauses(name, scores, rules)
        for clause in clauses:
            solver.add_clause([idx])
            clause_to_modality[idx] = name
            idx += 1

    if solver.solve():
        model = solver.get_model()
        result = [clause_to_modality[lit] for lit in model if lit > 0]
        return result
    else:
        return None
