import random
n = int(input("Masukkan nilai N :"))
for i in range(n):
    d = random.uniform(0.0, 0.5)
    print("Data ke :", i+1, "=> ",d)
print('tamat')