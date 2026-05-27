class Environment:
    def __init__(self, variables=None, active_facts=None):
        self.variables = variables if variables else {}        # Mapeo id -> int
        self.active_facts = set(active_facts) if active_facts else set() # Set de hechos

class Interpreter:
    def __init__(self, ast, env):
        self.ast = ast
        self.env = env

    def evaluate(self):
        # Algoritmo de Punto Fijo (Fixed Point Iteration)
        while True:
            new_facts_this_iteration = set()
            
            for rule in self.ast.rules:
                if self._eval_condition(rule.condition):
                    fact_to_activate = rule.action.identifier
                    if fact_to_activate not in self.env.active_facts:
                        new_facts_this_iteration.add(fact_to_activate)
            
            if not new_facts_this_iteration:
                break # Se alcanzó el punto fijo (no hay nuevos hechos)
                
            self.env.active_facts.update(new_facts_this_iteration)
            
        return self.env.active_facts

    def _eval_condition(self, node):
        from .ast_nodes import AndConditionNode, ComparisonNode, FactConditionNode
        
        if isinstance(node, AndConditionNode):
            return self._eval_condition(node.left) and self._eval_condition(node.right)
            
        elif isinstance(node, ComparisonNode):
            val = self.env.variables.get(node.identifier, None)
            if val is None:
                return False # Si la variable no está definida, la comparación falla
            
            if node.operator == '>': return val > node.value
            elif node.operator == '<': return val < node.value
            elif node.operator in ('=', '=='): return val == node.value
            
        elif isinstance(node, FactConditionNode):
            return node.identifier in self.env.active_facts
            
        return False