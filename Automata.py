from TokenType import TokenType
from AutomataEstado import AutomataEstado


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

    def transition(self, input_symbol):
        if input_symbol in self.transitions[self.state]:
            self.state = self.transitions[self.state][input_symbol]
        else:
            raise ValueError(f"No transition for symbol {input_symbol} in state {self.state}")

    def is_accepting(self):
        return self.state == AutomataEstado.FIN