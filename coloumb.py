A = int(input("masukkan besar FA : "))
B = int(input("masukkan besar FB : "))
R = float(input("masukkan r : "))


k1 = 9
k2 = 0.0000000001
ktotal = k1*k2

q = A*B

F = ktotal*(q/R**2)
print(F)