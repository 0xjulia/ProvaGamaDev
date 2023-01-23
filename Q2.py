# Elabore um programa que leia um número que o usuário digitar. Dependendo do
# número informado, das frases abaixo, o sistema imprimirá somente as que forem
# verdadeiras.
# ○ O número é menor que 10.
# ○ O número é par.
# ○ O número está entre 8 e 16.
# ○ O número é 51 ou 80.

# Por exemplo, se o usuário digitar o número “12”, o programa irá imprimir:
# O número é par.
# O número está entre 8 e 16.
# Se o usuário digitar o número “51”, então será impresso:
# O número é 51 ou 80.
# Ou, se o usuário digitar “101”, então o programa não imprime nada.

# n1 = input("Digite um número menor ou igual a 80: " )
# n1 = int(n1)

while True:

    while True:
        n1 = input("Digite um número menor ou igual a 80: " )
        n1 = int(n1)

        if n1 > 80:
            print(" ")
            break

        if n1%2==0:
            print("O número é par.")
            
        if n1 < 10:
            print("O número é menor que 10.")

        if n1>=8 and n1<=16:
            print("O número está entre 8 e 16.")

        if n1==51 or n1==80:
            print("O número é 51 ou 80.")