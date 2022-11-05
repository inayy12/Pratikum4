print("Paratikum2")

A = int (input("Masukan bilangan pertaman: "))
B = int (input("Masukan bilangan kedua: "))
C = int (input("Masukan bilangan ketiga: "))

if A > B > C :
    print("\nBilangan pertama adalah bilangan terbesar = %s" % A)
elif B > C :
    print("\nBilangan kedua adalah bilangan terbesar = %s" % B)
else :
    print("\nBilangan ketiga adalah bilangan terbesar = %s" %C)