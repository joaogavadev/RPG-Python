

import random

sorte = 6 + random.randint(1, 6)
def usar_sorte(sorte):
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    soma_dados = dado_1 + dado_2
    print(dado_1)
    print(dado_2)
    print(soma_dados)

    if soma_dados <= sorte :
        return True
    else:
        return False
    
if usar_sorte(sorte):
    print("yes")
else:
    print("no")


print(f"para retornar yes, o valor da soma de dado1+dado2 tem que ser menor ou igual ao valor inicial de sorte")

print(sorte)
