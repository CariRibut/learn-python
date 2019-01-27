n=str(input("Masukkan kata:"))
balik = reversed(n)
if (list(n) == list(balik)):
    print("Pallindrom")
else:
    print("Asu")
