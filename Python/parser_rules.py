import sys
import ply.yacc as yacc

# Se deben importar los tokens del lexer para que yacc los reconozca
from lexer_rules import tokens

# ==========================================
# Parser (Análisis Sintáctico)
# ==========================================

# Precedencia y asociatividad de operadores
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
)

def p_sistema(p):
    '''sistema : lista_ecuaciones'''
    pass

def p_lista_ecuaciones(p):
    '''lista_ecuaciones : ecuacion
                        | lista_ecuaciones EOL ecuacion'''
    pass

def p_ecuacion(p):
    '''ecuacion : expresion IGUAL expresion
                | error'''
    # Solo imprimimos si no fue un error (la regla de error tiene longitud 2: [error])
    if len(p) == 4:
        print("✓ Ecuación válida")

def p_expresion_binop(p):
    '''expresion : expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULT expresion
                 | expresion DIV expresion'''
    pass

def p_expresion_term(p):
    '''expresion : ID
                 | NUM'''
    pass

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error Sintáctico en la Línea {p.lineno}. Componente no esperado: '{p.value}'", file=sys.stderr)
    else:
        print("Error Sintáctico: La última ecuación está incompleta (se alcanzó el final del archivo).", file=sys.stderr)

# Construir el analizador sintáctico
parser = yacc.yacc()
