"""
Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de seus colegas não concluiu. O objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela:

1- A quantidade de números pares e ímpares.
2- A quantidade de números positivos e negativos.
3- A quantidade de números inseridos.
4- O maior e o menor número.
5- A média de números pares.
6- A média de números ímpares.
7- A média de todos os números inseridos.
8- Mostrar os números lidos na ordem inversa.


"""


import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE = 5
contador = 0

# Variáveis para armazenar os números
for i in range(QUANTIDADE):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)
    contador += 1


def verificando_pares():
    lista_pares = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)


    return lista_pares
        
def verificando_impares():
    lista_impares = []
   

    for numero in lista_numeros:
        if numero % 2 != 0:
            lista_impares.append(numero)
    
    
    return lista_impares


        
def verificando_positivo():
    lista_positivo = []
    
    for numero in lista_numeros:
       if numero > 0:
            lista_positivo.append(numero)
 
    return lista_positivo

def verificando_negativos():
    lista_negativos = []
    
    for numero in lista_numeros:
        if numero < 0:
            lista_negativos.append(numero)
 
    return lista_negativos

def calculando_media(n1):
    QUANTIDADE = len(n1)
    soma = sum(n1)
    if soma != 0:
        media = soma / QUANTIDADE 
        return media
    else:
        return 0
        

max_numero = max(lista_numeros)
min_numero = min(lista_numeros)


lista_atualizada_impares = verificando_impares()
lista_atualizada_pares = verificando_pares()
lista_atualizada_positivo = verificando_positivo()
lista_atualizada_negativos = verificando_negativos()


resultado_media_impar = calculando_media(lista_atualizada_impares)
resultado_media_par = calculando_media(lista_atualizada_pares)

soma_pares = sum(lista_atualizada_pares)
soma_impares = sum(lista_atualizada_impares)
soma_maxima = sum(lista_numeros)

quantidade_de_pares = len(lista_atualizada_pares)
quantidade_de_impares = len(lista_atualizada_impares)
quantidade_de_postivos = len(lista_atualizada_positivo)
quantidade_de_negativos = len(lista_atualizada_negativos)


media_maxima = soma_maxima / QUANTIDADE

print("\n=== Exibindo ordem inversa ===")
for i, numero in enumerate(reversed(lista_numeros)):
    print(f"{len(lista_numeros)- i}º - {numero}")

print("\n=== Exibindo quantidade de números inseridos ===")
print(f"Números inseridos: {contador}")
print(f"Quantidade de números ímpares: {quantidade_de_impares}")
print(f"Quantidade de números pares: {quantidade_de_pares}")
print(f"Quantidade de números positivos: {quantidade_de_postivos}")
print(f"Quantidade de números negativos: {quantidade_de_negativos}")

print("\n=== Exibindo maior e menor numero ===")
print(f"Maior: {max_numero}")
print(f"Menor: {min_numero}")

print("\n=== Exibindo Média ===")
print(f"Média dos números pares: {resultado_media_par}")
print(f"Média dos números impares: {resultado_media_impar}")
print(f"Média dos números inseridos: {media_maxima}")
