
def descomponer(numero):
    if numero < 2020:
        return False
    if numero % 2020 == 0:
        return True
    for i in range(numero // 2020 + 1):
        residuo = numero - i * 2020
        if residuo % 2021 == 0:
            return True
    return False
num = int(input())
for _ in range(num):
    n = int(input())
    if descomponer(n) == True:
        print("YES")
    else:
        print("NO")
#Otra solucion
lol = set()
for n in range(500):
    for nu in range(500):
        lol.add(n*2020 + nu*2021)        
num = int(input())
for _ in range(num):
    k = int(input())
    if k in lol:
        print("YES")
    else:
        print("NO")