import re
import sys
sys.setrecursionlimit(10000)

mounttree = lambda sqtok : sqtok [0] if len (sqtok) == 1 else (mounttree (sqtok [0]), sqtok [1], mounttree (sqtok [2:]))
#m = mounttree (["2", "+", "3", "+", "4"], 1)
m = mounttree (["2", "+", "3", "+", "5", "+", "7"])
print ("qualquer coisa")
#O trecho daqui para baixo faz parte do script do semestre anterior...

#Este script em Python ira te ajudar a reconhecer expressoes (vetando as nao-compilaveis)
#    e traduzi-las para o codigo-objeto (alvo) do seu projeto
#Ele pode ser utilizado como inspiracao para o reconhecimento de expressoes aritmeticas e booleanas

regex_letter = "[a-zA-z]"
regex_digit = "[0-9]"
regex_d_or_l = "(" + regex_digit + "|" + regex_letter + ")"
regex_valid_var_name = "^" + regex_letter + regex_d_or_l + "*$"
regex_number = "^" + regex_digit + "+$"
rec_word = lambda w: str (w) if re.search(regex_valid_var_name, w) else False
rec_number = lambda w: str (w) if re.search(regex_number, w) else False
rec_operator = lambda op : op if op in ["+", "-", "*", "/"] else False
op_in_list = lambda lst : False in [rec_operator (el) for el in lst]
tokens = lambda sequence : sequence.split()
def divide_expr (sequence, value) :
    toks = list (tokens (sequence))
    count = 0
    if (not op_in_list (toks)) :
        return False
    while not rec_operator (toks [count]) :
        count = count + 1
    ind = count
    if value == 0 :
        return ' '.join(str(x) for x in toks [0 : ind])
    elif value == 1 :
        return ' '.join(str(x) for x in toks [ind])
    else :
        return ' '.join(str(x) for x in toks [ind + 1 : len (sequence)])
extract_left_expr = lambda sequence : divide_expr (sequence, 0)
extract_operator = lambda sequence : divide_expr (sequence, 1)
extract_right_expr = lambda sequence : divide_expr (sequence, 2)
rec_operand = lambda expr : rec_word (expr) or rec_number (expr) or ret_expr (expr)
rec_word_or_num = lambda w : rec_word (w) or rec_number (w)

translate_operator = lambda op : "PLUS" if op == "+" else "MINUS" if op == "-" else "TIMES" if op == "*" else "DIV"
def ret_expr (expr) :
    if rec_word_or_num (expr) :
        return expr
    else :
        left_expr = extract_left_expr (expr)
        operator = extract_operator (expr)
        right_expr = extract_right_expr (expr)
        b_op = rec_operator (operator)
        return str (ret_expr (left_expr)) + " " + translate_operator (operator) + " " + str (ret_expr (right_expr)) if b_op else "ERROR"

rec_expr = lambda expr : "ERROR" if "ERROR" in ret_expr (expr) else ret_expr (expr)

print (rec_expr ("xis + 56 - ypsilon")) #Aqui o reconhecimento e a traducao DEVEM ocorrer ok, pois a expressao eh compilavel
print (rec_word ("1xis")) #Aqui o reconhecimento da expressao NAO deve ocorrer, pois o nome de variavel eh invalido;
print (rec_word ("xis*")) #Aqui o reconhecimento da expressao NAO deve ocorrer, pois o nome de variavel eh invalido;
print (rec_word ("xis")) #Aqui o reconhecimento e a traducao DEVEM ocorrer, pois a expressao (que consiste no nome de variavel) eh valida;
print (rec_expr ("xis + 56")) #Aqui o reconhecimento e a traducao DEVEM ocorrer, pois a expressao eh compilavel
print (rec_expr ("xis + + 56")) #Aqui o reconhecimento NAO deve ocorrer
print (rec_expr ("+ xis + 56")) #Aqui o reconhecimento NAO deve ocorrer
print (rec_expr ("( xis ) + 56")) #Aqui o reconhecimento DEVE ocorrer
