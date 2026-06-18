package com.automatas;
import java_cup.runtime.Symbol;

%%

%{
    private Symbol symbol(int type) {
        return new Symbol(type, yyline, yycolumn);
    }
    private Symbol symbol(int type, Object value) {
        return new Symbol(type, yyline, yycolumn, value);
    }
%}
/*---------------------------------------------------------
 * Configuración de JFlex
 *---------------------------------------------------------*/

/* Nombre de la clase generada */
%class Lexer

/* Indica que usaremos JavaCup */
%cup

/* Habilita el seguimiento de línea y columna */
%line
%column

/*---------------------------------------------------------
 * Expresiones regulares
 *---------------------------------------------------------*/

LETRA = [a-zA-Z]
DIGITO = [0-9]

ID = {LETRA}({LETRA}|{DIGITO})*
NUM = {DIGITO}+

%%

/*---------------------------------------------------------
 * Reglas léxicas
 *---------------------------------------------------------*/

{ID}      { return symbol(sym.ID, yytext()); }

{NUM}     { return symbol(sym.NUM, Integer.parseInt(yytext())); }

"+"       { return symbol(sym.SUMA); }

"-"       { return symbol(sym.RESTA); }

"="       { return symbol(sym.IGUAL); }

"*"       { return symbol(sym.MULT); }

"/"       { return symbol(sym.DIV); }

"\n"     { return symbol(sym.EOL); }

<<EOF>>   { return null; }

/* Ignorar espacios y tabulaciones */
[ \t\r]+ { }

. {
    System.err.println(
        "Error léxico en línea " + (yyline + 1) + ", columna " + (yycolumn + 1) + ": '" + yytext() + "'"
    );
}
