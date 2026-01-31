import math
meb = int(input("Mebleg: "))
faz = int(input("Faiz: "))
il = int(input("Il: "))
ay = il*12
cavab = meb *(1 + faz/100)** ay
print(round(cavab))