from Automata import *
from Operador import *
from Proposicion import *
from Token import *
from TokenType import *

def main():
    # Solicta al que ingrese una proposicion
    print("Ingrese una proposicion: ")
    proposicion = input()
    
    # Convertir la proposicion a simbolos y verificar que sea una proposicion valida
    tokens = proposicion.lower().split(' ')
    print("\nTokens:", tokens)
    
    # crear una lista y guardar el tipo de token y el valor
    listaTokens = []
    for token in tokens:
        if token == 'y':
            listaTokens.append(Token(TokenType.Y, token))
        elif token == 'o':
            listaTokens.append(Token(TokenType.O, token))
        elif token == 'si':
            listaTokens.append(Token(TokenType.SI, token))
        elif token == 'entonces':
            listaTokens.append(Token(TokenType.ENTONCES, token))
        elif token == 'no':
            listaTokens.append(Token(TokenType.NOT, token))
        else:
            listaTokens.append(Token(TokenType.PALABRA, token))
    listaTokens.append(Token(TokenType.EOL, ''))
    
    # Imprimir la lista de tokens
    print("\nLista de tokens:")
    print("Tipo\tValor")
    for token in listaTokens:
        print(token.tipo, token.valor)
        
    # Analizar tokens con el automata : Analizador Sintactico
    def print_ast(node, level=0):
        indent = "  " * level
        if isinstance(node, PropNode):
            print(f"{indent}PropNode: {node.value}")
        elif isinstance(node, NegNode):
            print(f"{indent}NegNode")
            print_ast(node.child, level + 1)
        elif isinstance(node, CondNode):
            print(f"{indent}CondNode: {node.operator}")
            print_ast(node.left, level + 1)
            print_ast(node.right, level + 1)
            
    print("\nProcesar Automata:")
    automata = Automata()
    resultado = automata.evaluar(listaTokens)

    if resultado:
        print("La proposición es correcta.")
        print("\nAST generado:")
        print_ast(resultado)  # Asumiendo que tienes una función para imprimir el AST
    else:
        print("La proposición es incorrecta.")    
    
if __name__ == "__main__":
    main()