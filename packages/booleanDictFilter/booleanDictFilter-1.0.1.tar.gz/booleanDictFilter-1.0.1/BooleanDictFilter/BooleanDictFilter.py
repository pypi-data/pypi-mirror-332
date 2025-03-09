import ast
import operator
import re


def _fix_equals_operator(expr):
    """
    Replaces '=' with '==' to comply with Python's comparison syntax.
    """
    expr = re.sub(r'(?<![><!])=', '==',
                  expr)  # Ensure '=' is only replaced when it's a standalone equality operator
    return expr


def _parse_expression(expr):
    """
    Converts a filter string into an Abstract Syntax Tree (AST) for safe evaluation.
    """
    expr = re.sub(r'\b(and|or|not)\b', lambda m: f" {m.group(1)} ", expr)
    return ast.parse(expr, mode='eval').body


def _extract_required_keys(node):
    """
    Extracts all keys (variable names) that the filter string depends on.
    """
    required_keys = set()

    def _extract(_node):
        if isinstance(_node, ast.Name):
            required_keys.add(_node.id)
        elif isinstance(_node, ast.BoolOp):
            for value in _node.values:
                _extract(value)
        elif isinstance(_node, ast.Compare):
            _extract(_node.left)
            for comp in _node.comparators:
                _extract(comp)
        elif isinstance(_node, ast.Call):
            for arg in _node.args:
                _extract(arg)

    _extract(node)
    return required_keys


class BooleanDictFilter:
    OPERATORS = {
        'and': operator.and_,
        'or': operator.or_,
        'not': operator.not_,
        '==': operator.eq,  # Corrected equality operator
        '>=': operator.ge,
        '>': operator.gt,
        '<': operator.lt,
        '<=': operator.le,
        'contains': lambda a, b: b in a,
        'anyof': lambda a, b: a in b,  # True if a is in the provided list
        'noneof': lambda a, b: a not in b  # True if a is not in the provided list
    }

    def __init__(self, filter_string):
        self.filter_string = _fix_equals_operator(filter_string)  # Fix '=' to '=='
        self.parsed_expression = _parse_expression(self.filter_string)
        self.required_keys = _extract_required_keys(self.parsed_expression)

    def _evaluate(self, node, data):
        """
        Recursively evaluates an AST node against a dictionary.
        If a required key in the filter is missing from the dictionary, return False immediately.
        """
        if isinstance(node, ast.BoolOp):  # Handle 'and' and 'or'
            if isinstance(node.op, ast.And):
                return all(self._evaluate(v, data) for v in node.values)
            elif isinstance(node.op, ast.Or):
                return any(self._evaluate(v, data) for v in node.values)

        elif isinstance(node, ast.UnaryOp):  # Handle 'not'
            if isinstance(node.op, ast.Not):
                return not self._evaluate(node.operand, data)

        elif isinstance(node, ast.Compare):  # Handle comparisons
            left = self._evaluate(node.left, data)
            if left is None:  # Missing key
                return False
            comparisons = [self._evaluate(c, data) for c in node.comparators]
            for op, right in zip(node.ops, comparisons):
                if right is None:  # Missing key
                    return False
                if isinstance(op, ast.Eq):
                    if not left == right:
                        return False
                elif isinstance(op, ast.Gt):
                    if not left > right:
                        return False
                elif isinstance(op, ast.GtE):
                    if not left >= right:
                        return False
                elif isinstance(op, ast.Lt):
                    if not left < right:
                        return False
                elif isinstance(op, ast.LtE):
                    if not left <= right:
                        return False
                left = right  # Allow for chained comparisons
            return True

        elif isinstance(node, ast.Call):  # Handle 'contains', 'anyof', 'noneof'
            if isinstance(node.func, ast.Name) and node.func.id in {'contains', 'anyof', 'noneof'}:
                left = self._evaluate(node.args[0], data)
                right = self._evaluate(node.args[1], data)
                if left is None or right is None:  # Missing key
                    return False
                return self.OPERATORS[node.func.id](left, right)

        elif isinstance(node, ast.List):  # Handle list literals (for anyof/noneof)
            return [self._evaluate(elem, data) for elem in node.elts]

        elif isinstance(node, ast.Name):  # Handle variable names (keys in dictionary)
            if node.id not in data:  # If key is missing, return False immediately
                return None  # Explicitly indicate missing key
            return data[node.id]

        elif isinstance(node, ast.Constant):  # Handle literals (strings, numbers)
            return node.value

        raise ValueError(f"Unsupported operation: {node}")

    def evaluate(self, data):
        """
        Evaluates the filter condition against a dictionary.
        If a required key is missing, return False.
        """
        # Ensure all required keys exist in the data
        if not all(key in data for key in self.required_keys):
            return False

        return self._evaluate(self.parsed_expression, data)

    def filter_dicts(self, data_list):
        """
        Takes a list of dictionaries and returns only those that evaluate to True.
        """
        return [data for data in data_list if self.evaluate(data)]
