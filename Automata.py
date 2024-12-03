from TokenType import TokenType
from Token import Token
from AutomataEstado import AutomataEstado
from ASTNodes import *

class Automata:
    def __init__(self):
        self.transitions = {
            AutomataEstado.INICIO: {TokenType.SI: AutomataEstado.COND_1, TokenType.PALABRA: AutomataEstado.PROP, TokenType.NOT: AutomataEstado.NEG},
            AutomataEstado.NEG: {TokenType.PALABRA: AutomataEstado.PROP},
            AutomataEstado.PROP: {TokenType.O: AutomataEstado.COND_2, TokenType.Y: AutomataEstado.COND_2, TokenType.PALABRA: AutomataEstado.PROP, TokenType.EOL: AutomataEstado.FIN},
            AutomataEstado.COND_1: {TokenType.NOT: AutomataEstado.NEG_PA, TokenType.PALABRA: AutomataEstado.PROP_A},
            AutomataEstado.NEG_PA: {TokenType.PALABRA: AutomataEstado.PROP_A},
            AutomataEstado.PROP_A: {TokenType.PALABRA: AutomataEstado.PROP_A, TokenType.ENTONCES: AutomataEstado.COND_2},
            AutomataEstado.COND_2: {TokenType.NOT: AutomataEstado.NEG_PB, TokenType.PALABRA: AutomataEstado.PROP_B},
            AutomataEstado.NEG_PB: {TokenType.PALABRA: AutomataEstado.PROP_B},
            AutomataEstado.PROP_B: {TokenType.PALABRA: AutomataEstado.PROP_B, TokenType.EOL: AutomataEstado.FIN}
        }
        self.state = AutomataEstado.INICIO
        self.ast = None
        self.current_node = None

    def transition(self, input_token: Token):
        if input_token.tipo in self.transitions[self.state]:
            self.state = self.transitions[self.state][input_token.tipo]
            self.build_ast(input_token)
        else:
            # No hay transicion, cambiar a error
            self.state = AutomataEstado.ERROR

    def build_ast(self, input_token):
        if self.state == AutomataEstado.PROP:
            self.current_node = PropNode(input_token)
            self.ast = self.current_node
        elif self.state == AutomataEstado.NEG:
            self.current_node = NegNode(self.current_node)
            self.ast = self.current_node
        elif self.state in [AutomataEstado.COND_1, AutomataEstado.COND_2]:
            operator = 'O' if input_token == TokenType.O else 'Y'
            self.current_node = CondNode(self.ast, operator, None)
            self.ast = self.current_node
        elif self.state == AutomataEstado.PROP_A:
            self.current_node.right = PropNode(input_token)
        elif self.state == AutomataEstado.PROP_B:
            self.current_node.right = PropNode(input_token)

    def is_accepting(self):
        return self.state == AutomataEstado.FIN

    def evaluar(self, listaTokens):
        for token in listaTokens:
            self.transition(token)
            if self.state == AutomataEstado.ERROR:
                return None
        return self.ast if self.is_accepting() else None