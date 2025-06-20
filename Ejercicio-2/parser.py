class SymbolTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type_):
        if name in self.table:
            raise ValueError(f"Error: Variable '{name}' ya declarada.")
        self.table[name] = type_

    def __str__(self):
        return str(self.table)


class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def __str__(self, level=0):
        result = "  " * level + self.label + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

def parse(tokens):
    pos = [0] 
    symbol_table = SymbolTable()

    def current_token():
        return tokens[pos[0]] if pos[0] < len(tokens) else None

    def match(expected_type):
        token = current_token()
        if token and token[0] == expected_type:
            pos[0] += 1
            return token  # Retorna el token completo (tipo y lexema)
        raise SyntaxError(f"Se esperaba '{expected_type}', pero se encontró '{token}'")

    def D():
        t_node, t_type = T() 
        l_node = L(t_type, symbol_table)  
        match(';')   
        return Node("D", [t_node, l_node])

    def T():
        token = current_token()
        if token and token[0] == 'int':
            match('int')
            return Node("T", ['int']), 'int'  
        elif token and token[0] == 'float':
            match('float')
            return Node("T", ['float']), 'float'  
        else:
            raise SyntaxError(f"Tipo no reconocido: {token}")

    def L(type_, symbol_table):
        identifier = L1(type_, symbol_table)
        if current_token() and current_token()[0] == ',':
            match(',')
            identifiers = L(type_, symbol_table)
            return Node("L", [f'{identifier.label}, {identifiers.label}'])
        else:
            return identifier

    def L1(type_, symbol_table):
        token = current_token()
        if token and token[0] == 'id':
            id_node = match('id') 
            symbol_table.add(id_node[1], type_)
            return Node('id', [id_node[1]])
        else:
            raise SyntaxError(f"Se esperaba 'id', pero se encontró '{token}'")
    value = D()
    return value, symbol_table