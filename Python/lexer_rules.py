import sys
import ply.lex as lex

# ==========================================
# Lexer (Análisis Léxico)
# ==========================================

# Lista de tokens
tokens = (
    'ID',
    'NUM',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'IGUAL',
    'EOL',
)

# Reglas de expresiones regulares para tokens simples
t_SUMA  = r'\+'
t_RESTA = r'-'
t_MULT  = r'\*'
t_DIV   = r'/'
t_IGUAL = r'='

# Ignorar espacios y retornos de carro (no EOL)
t_ignore = ' \t\r'

# Regla para identificadores
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

# Regla para números
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para contar líneas y capturar saltos de línea
def t_EOL(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Manejo de errores léxicos
def t_error(t):
    print(f"Error léxico: Carácter no válido '{t.value[0]}' en línea {t.lexer.lineno}", file=sys.stderr)
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
