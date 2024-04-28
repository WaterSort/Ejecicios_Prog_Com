#LINK DEL EJECICIO:
#https://codeforces.com/contest/1475/problem/B
#
#
#La funcion define los casos base y les asigna el return
def descomponer(nume):
    if nume < 2020:
        return False
    if nume % 2020 == 0:
        return True
    for i in range(nume // 2020 + 1):
        resto = nume - i * 2020
        if resto % 2021 == 0:
            return True
    return False
#Teniendo los inputs se llama a la funcion que comprueba si num es resulta de sumas de 2020 y 2021 
num = int(input())
for _ in range(num):
    n = int(input())
    if descomponer(n) == True:
        print("YES")
    else:
        print("NO")
#
#       
#Otra solucion (fuerza bruta)
#Se crea una variable tipo set antes de pedir los input
#El set crea todas las posibilidad de conbinaciones de 2020 y 2021
lol = set()
for n in range(500):
    for nu in range(500):
        lol.add(n*2020 + nu*2021)
#Si los input se encuentran dentro del set significa que se pueden decomponen en sumas de 2020 y 2021       
num = int(input())
for _ in range(num):
    k = int(input())
    if k in lol:
        print("YES")
    else:
        print("NO")