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

    def current_token():
        return tokens[pos[0]] if pos[0] < len(tokens) else None

    def match(expected):
        if current_token() == expected:
            pos[0] += 1
            return expected
        raise SyntaxError(f"Se esperaba '{expected}', pero se encontró '{current_token()}'")
    
    def E():
        t_node, t_val = T()
        ep_node, ep_val = E1(t_val)
        return Node("E", [t_node, ep_node]), ep_val
    
    def E1(inherited):
        if current_token() == '+':
            match('+')
            t_node, t_val = T()
            ep_node, ep_val = E1(inherited + t_val)
            return Node("E1", [Node('+'), t_node, ep_node]), ep_val
        else:
            return Node("E1", [Node('ε')]), inherited
    
    def T():
        f_node, f_val = F()
        tp_node, tp_val = T1(f_val)
        return Node("T", [f_node, tp_node]), tp_val
    
    def T1(inherited):
        if current_token() == '*':
            match('*')
            f_node, f_val = F()
            tp_node, tp_val = T1(inherited * f_val)
            return Node("T1", [Node('*'), f_node, tp_node]), tp_val
        else:
            return Node("T1", [Node('ε')]), inherited
    def F():
        if current_token() == '(':
            match('(')
            e_node, e_val = E()
            match(')')
            return Node("F", [Node('('), e_node, Node(')')]), e_val
        elif current_token().replace('.', '', 1).isdigit():
            value = float(current_token())
            match(current_token())
            return Node("F", [Node(str(value))]), value
        else:
            raise SyntaxError(f"Token inesperado: {current_token()}")
    tree, value = E()
    if current_token() != '#':
        raise SyntaxError("No se consumieron todos los tokens.")
    return tree, value
