# Operaciones sobre conjuntos (Numeros)

import os; os.system("cls")

A = {50,60,70,80,90,100,200}
B = {60,90,100,300,400,500}
C = {10,20,60,90,70,100,600,700}

print("Operaciones con conjuntos : \n")
print(f"Conjunto A : {A} - {len(A)} - {type(A)}")
print(f"Conjunto B : {B} - {len(B)} - {type(B)}")
print(f"Conjunto C : {C} - {len(C)} - {type(C)}")

print(f"\nUnion (A | B)                : {A.union(B)}")
print(f"Union (B | C)                : {B.union(C)}")
print(f"Diferencia (A - C)           : {A.difference(C)}")
print(f"Diferencia simetrica (B ^ C) : {B.symmetric_difference(C)}")
print(f"Interseccion (B & C)         : {B.intersection(C)}")

print(f"\nA es subconjunto de B ? --- {A.issubset(B)}")
print(f"C es subconjunto de A ? --- {C.issubset(A)}")

print(f"\n100 esta en A              ? --- {100 in A}")
print(f"60 esta en A y en B y en C ? --- {60 in A and 60 in B and 60 in C }")
print(f"900 no esta en C           ? --- {900 not in C }\n")