from lexer import lexer
from parser import parse

def main():
    text = "3+2 * 4"
    tokens = lexer(text)
    tree, result = parse(tokens)
    print("Result:", result)

main()
