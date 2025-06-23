class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def match(self, expected):
        if self.current_token() == expected:
            self.pos += 1
            return True
        return False

    def parse_E(self):
        if self.parse_T():
            while self.match('+'):
                if not self.parse_T():
                    return False
            return True
        return False

    def parse_T(self):
        if self.parse_F():
            while self.match('*'):
                if not self.parse_F():
                    return False
            return True
        return False

    def parse_F(self):
        if self.match('id'):
            return True
        elif self.match('('):
            if self.parse_E():
                if self.match(')'):
                    return True
        return False

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
        elif expr[i] == '+' or expr[i] == '*' or expr[i] == '(' or expr[i] == ')':
            tokens.append(expr[i])
            i += 1
        elif expr[i:i+2] == 'id':
            tokens.append('id')
            i += 2
        else:
            raise ValueError(f"Token desconocido en la posición {i}: '{expr[i]}'")
    return tokens

def validar_expresion(expr):
    try:
        tokens = tokenize(expr)
        parser = Parser(tokens)
        result = parser.parse_E()
        return result and parser.pos == len(tokens)
    except ValueError as e:
        print(e)
        return False

while True:
    try:
        input_expr = input("Ingrese una expresión (o 'salir' para terminar): ")
        if input_expr.lower() == 'salir':
            break
        if validar_expresion(input_expr):
            print("La expresión es válida.")
        else:
            print("La expresión no es válida.")
    except Exception as e:
        print(f"Error: {e}")
