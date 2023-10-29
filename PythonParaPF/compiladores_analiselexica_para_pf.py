import re

ID = lambda : "^[a-zA-z]([a-zA-z]|[0-9])*$"
NUM = lambda : "^[0-9]+$"
PATTERNS_2_TOKENS = lambda : {
    #Palavras reservadas
      "^if$" : "IF"
    , "^for$" : "FOR"
    , "^while$" : "WHILE"
    #Simbolos
    , "^($" : "LPAREN"
    , "^)$" : "RPAREN"
    , "^{$" : "LBRACE"
    , "^}$" : "RBRACE"
    , "^[$" : "LBRACKET"
    , "^]$" : "RBRACKET"
    , "^.$" : "DOT"
    , "^,$" : "COMMA"
    , "^;$" : "DOTCOMMA"
    #Operadores numericos que retornam booleano
    , "^<$" : "LESSTHAN"
    , "^>$" : "GREATESTTHAN"
    , "^>=$" : "GEQTHAN"
    , "^==$" : "EQUALS"
    #Operadores numericos que retornam numerico
    , "^+$" : "PLUS"
    , "^-$" : "MINUS"
    , "^*$" : "TIMES"
    , "^/$" : "DIV"
    #Operadores booleanos
    , "^&&$" : "AND"
    , "^||$" : "OR"
    , "^!$" : "NOT"
    #Operador de atribuicao
    , "^=$" : "ASSIGNS"
    #ReGex
    , ID () : "IDENTIFIER"
    , NUM () : "NUMBER"
}
PATTERN = lambda lexem, dictok : "^" + lexem + "$" if "^" + lexem + "$" in dictok.keys() else ID () if re.search (ID (), lexem) else NUM () if re.search (NUM (), lexem) else "ERROR"
TOKEN = lambda lexem, dictok : dictok [PATTERN (lexem, dictok)] if PATTERN (lexem, dictok) in dictok.keys() else "LEXERROR"
tok = lambda lexem : TOKEN (lexem, PATTERNS_2_TOKENS())
print (tok ("varname-"))
print (tok ("varname"))
print (tok ("1varname"))
print (tok ("for"))
print (tok ("if"))
print (tok ("while"))
print (tok ("^while$"))
