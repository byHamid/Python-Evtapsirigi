san = int(input("Sanye: "))
deq = int(san / 60)
san = deq*60 - san
saat = int(deq / 60)
deq = saat*60 - deq

if san < 1:
    san = -san
if deq<1:
    deq = -deq
if saat  < 1:
    saat = -saat

print(f"{saat} saat, {deq} deqiqe, {san} saniye")