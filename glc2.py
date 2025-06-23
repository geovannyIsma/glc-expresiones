class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def token_actual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None  # Fin de entrada

    def match(self, esperado):
        if self.token_actual() == esperado:
            self.pos += 1
            return True
        return False

    def parse_S(self):
        saved_pos = self.pos
        # S -> A a
        if self.parse_A():
            if self.match('a'):
                return True
            else:
                self.pos = saved_pos
        # S -> b
        self.pos = saved_pos
        if self.match('b'):
            return True
        return False

    def parse_A(self):
        saved_pos = self.pos
        # A -> A c
        if self.parse_A():
            if self.match('c'):
                return True
            else:
                self.pos = saved_pos
        # A -> S b
        self.pos = saved_pos
        if self.parse_S():
            if self.match('b'):
                return True
            else:
                self.pos = saved_pos
        # A -> ε
        return True

def tokerizar(expr):
    return [ch for ch in expr if not ch.isspace()]  # elimina espacios

def validar_expresion(expr):
    tokens = tokerizar(expr)
    parser = Parser(tokens)
    result = parser.parse_S()
    return result and parser.pos == len(tokens)

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

