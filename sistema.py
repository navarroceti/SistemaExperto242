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
        
    # Recorre los elementos y agrupa toda las palabras consecutivas en una lista
    listaProposiciones = []
    listaPalabras = []
    for token in listaTokens:
        if token.tipo == TokenType.PALABRA:
            listaPalabras.append(token)
        else:
            if len(listaPalabras) > 0:
                listaProposiciones.append(Proposicion(listaPalabras))
                listaPalabras = []
                
    # Imprime la lista de proposiciones
    print("\nLista de proposiciones:")
    for proposicion in listaProposiciones:
        print(proposicion.ObtenerFrase())
        
        
    # Crear un conjunto para que no se repitan las proposiciones
    conjuntoProposiciones = set()
    for proposicion in listaProposiciones:
        conjuntoProposiciones.add(proposicion.ObtenerFrase())
        
    # Imprimir el conjunto de proposiciones
    print("\nConjunto de proposiciones:")
    for proposicion in conjuntoProposiciones:
        print(proposicion)
       
    
if __name__ == "__main__":
    main()