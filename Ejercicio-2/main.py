from lexer import lexer
from parser import parse

def main():
    codigo = "int x, y, z; float a, b;"
    
    tokens = lexer(codigo)
    value, symbol_table = parse(tokens)
    print("Tabla de Símbolos:",symbol_table)


# Ejecutar la función principal
if __name__ == "__main__":
    main()
