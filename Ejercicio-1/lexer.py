import re

def lexer(input_string):
    # Corrige el grupo de captura con (?:...) para evitar tuplas vacías
    token_regex = r'\d+(?:\.\d+)?|[()+\-*/^]'
    tokens = re.findall(token_regex, input_string.replace(" ", ""))
    return tokens + ['#']  # '#' representa fin de entrada
