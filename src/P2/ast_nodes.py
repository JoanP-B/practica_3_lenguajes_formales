class ProgramNode:
    def __init__(self, rules):
        self.rules = rules  # Lista de RuleNode

class RuleNode:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

class AndConditionNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class ComparisonNode:
    def __init__(self, identifier, operator, value):
        self.identifier = identifier
        self.operator = operator
        self.value = value

class FactConditionNode:
    def __init__(self, identifier):
        self.identifier = identifier

class ActionNode:
    def __init__(self, identifier):
        self.identifier = identifier