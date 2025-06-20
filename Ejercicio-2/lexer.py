import re

TOKEN_REGEX = [
    ('WHITESPACE', r'\s+'),               
    ('float', r'\bfloat\b'),              
    ('int', r'\bint\b'),                  
    (',', r','),                          
    (';', r';'),                          
    ('id', r'\b[A-Za-z_][A-Za-z0-9_]*\b'), 
]


def lexer(codigo):
    tokens = []
    index = 0
    while index < len(codigo):
        matched = False
        for token_name, token_regex in TOKEN_REGEX:
            regex = re.compile(token_regex)
            match = regex.match(codigo, index)
            if match:
                lexema = match.group(0)

                if token_name != 'WHITESPACE':
                    tokens.append((token_name, lexema))  
                index = match.end()
                matched = True
                break
        if not matched:
            raise RuntimeError(f"Error de tokenización en: '{codigo[index]}'")
    return tokens