#1
# x
# if eded%2==0:
#     print("cutdur")
# else:
#     print("tekdir")

#2
# eded1 =  int(input("eded 1 daxil edin"))
# eded2 = int(input("eded 2 daxil edin"))
# if eded1< eded2:
#     print(eded2)
# else:
#     print(eded1)

#3
# eded =int(input("eded daxil edin"))
# if eded<0:
#     print("menfidir")
# elif eded > 0:
#     print("musbetdir")
# else:
#     print("beraberdir")

#4
# a = float(input("eded 1 daxil edin"))
# b = float(input("eded 2 daxil edin"))
# toplam = a+b
# cixma=a-b
# vurma= a*b
# bolme = a /b
# print(toplam)
# print(cixma)
# print(vurma)
# print(bolme)

#5
# eded = int(input("eded  daxil edin"))
# if eded>=1 and eded<= 50:
#     print("true")
# else:
#     print("false")


a = input("enter hereket:")
b = input("enter hereket:")

if (a =="r" and b =="s") or(a =="s" and b =="p") or (a =="p" and b =="r") :
    print ( "A WINS")
elif(b =="r" and a =="s") or(b =="s" and a =="p") or (b =="p" and a =="r") :
    print("B wins")
else:
    print("TIE")