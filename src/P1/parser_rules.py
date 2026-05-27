from .lexer import Lexer, Token
# Usamos la importación para que busque en el paquete P2
from src.P2.ast_nodes import ProgramNode, RuleNode, AndConditionNode, ComparisonNode, FactConditionNode, ActionNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def _current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return Token('EOF', '', -1)

    def _advance(self):
        self.pos += 1

    def _consume(self, expected_type):
        curr = self._current()
        if curr.type == expected_type:
            self._advance()
            return curr
        raise SyntaxError(f"Error Sintáctico en línea {curr.line}: Se esperaba {expected_type}, se obtuvo {curr.type}")

    def parse_program(self):
        rules = []
        # Parsea todas las reglas secuencialmente hasta agotar los tokens
        while self._current().type == 'RULE':
            rules.append(self.parse_rule())
        return ProgramNode(rules)

    def parse_rule(self):
        self._consume('RULE')
        rule_id_tok = self._consume('ID')
        self._consume('COLON')
        self._consume('IF')
        condition = self.parse_cond()
        self._consume('THEN')
        action_id_tok = self._consume('ID')
        
        return RuleNode(
            name=rule_id_tok.value,
            condition=condition,
            action=ActionNode(action_id_tok.value)
        )

    def parse_cond(self):
        # Transformación de gramática para manejar precedencia y asociatividad de AND sin recursión izquierda
        left = self.parse_atom()
        while self._current().type == 'AND':
            self._advance()
            right = self.parse_atom()
            left = AndConditionNode(left, right)
        return left

    def parse_atom(self):
        id_tok = self._consume('ID')
        curr = self._current()
        
        if curr.type == 'RELOP' or curr.type == 'ASSIGN':
            op = curr.value
            self._advance()
            val_tok = self._consume('VALUE')
            return ComparisonNode(id_tok.value, op, int(val_tok.value))
        else:
            return FactConditionNode(id_tok.value)