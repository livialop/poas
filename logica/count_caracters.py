'''
Implemente uma função que receba uma string de texto e retorne a contagem de
frequência de cada caractere presente.

Case-Insensitivity: O algoritmo não deve diferenciar maiúsculas de minúsculas (ex: 'A' e 'a' devem ser contados como o mesmo caractere).
Filtro de Espaços: Espaços em branco devem ser completamente ignorados e não devem constar no resultado final.
Símbolos: Caracteres especiais e pontuação devem ser contados normalmente, seguindo a regra de ignorar apenas os espaços

# Lista de casos de teste: (Entrada, Saída_Esperada)
test_cases = [
    (
        "Banana", 
        {'b': 1, 'a': 3, 'n': 2}
    ),
    (
        "Hello World!", 
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}
    ),
    (
        "122 333", 
        {'1': 1, '2': 2, '3': 3}
    ),
    (
        "   ", 
        {}
    ),
    (
        "Python 3.10!", 
        {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '3': 1, '.': 1, '1': 1, '0': 1, '!': 1}
    )
]
'''

def count_caract(text: str) -> dict:
    lower_text = text.lower()
    char_count = {}
    
    for letter in lower_text:
        if letter != ' ':
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1

    return char_count

print(count_caract("Banana"))