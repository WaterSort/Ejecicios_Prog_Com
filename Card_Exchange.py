num = int(input())
#Este for determina la cantidad de casos
for _ in range(num):
#Aqui se usa el map para tener los dos numeros como int sin tener que usar for, lo mismo en la linea 6
n,k = (map(int,input().split()))
lis = list(map(int,input().split()))
#Se crea un diccionario para comprobar cuantas veces se repite cada numero dentro de la lis
dic = {}
for nu in lis:
    if nu in dic:
        dic[nu] += 1
    else:
        dic[nu] = 1
#Esta flag determinara si la clave entra dentro del for, lo que confirma que el numero se repine al menos k veces
#Si la flag es == True se puede hacer la operacion en la lista
#Si no se puede hacer ninguna operacion porque ningun numero se repite al menos k veces, se imprime el largo de lis
fla = False
for j in dic:
    if dic[j] >= k:
        fla = True
if fla == False:
    print(n)
else:
    print(k-1)
