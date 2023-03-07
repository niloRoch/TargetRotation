string = input("Digite uma palavra ou frase: ")

# cria uma lista vazia para armazenar os caracteres invertidos
invertida = []

# percorre a string da direita para a esquerda e 
for i in range(len(string)-1, -1, -1):
    invertida.append(string[i])

# transforma a lista em uma string novamente
string_invertida = "".join(invertida)

# imprime a string invertida
print("A string invertida é:", string_invertida)
