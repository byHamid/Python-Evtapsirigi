req = int(input("3 reqemli eded daxil et: "))
while req < 100 and req > 999:
    req = int(input("3 REQEMLI eded daxil et: "))

req1 = int(req / 100)
req2 = int(req / 10 % 10)
req3 = int(req % 10)
reqler = int(req1 + req2 + req3)
print(f"Cavab: {reqler}")