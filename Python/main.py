import sys
import time
import os

from lexer_rules import lexer
from parser_rules import parser

# ==========================================
# Punto de Entrada Principal
# ==========================================

def main():
    """
    Punto de entrada. Lee el archivo de entrada, ejecuta el parser
    y mide el tiempo de ejecución.
    """
    # Buscar el archivo entrada.txt en el directorio de Java
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Java', 'entrada.txt')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'.", file=sys.stderr)
        sys.exit(1)

    start_time = time.perf_counter()
    
    # Ejecutar el parser pasándole nuestro lexer
    parser.parse(data, lexer=lexer)
    
    end_time = time.perf_counter()
    
    elapsed_ms = (end_time - start_time) * 1000
    print(f"\nTiempo de ejecución: {elapsed_ms:.6f} ms")

if __name__ == '__main__':
    main()
