# Operaciones sobre conjuntos (personas)

import os; os.system("cls")

A = {"Juan","Maria","Pedro","Jose","Rocio"}
B = {"Pedro","Juan","Pablo","Mateo","Esther"}

print("Operaciones entre conjuntos : \n")
print(f"Conjunto A : {A} -- {len(A)} -- {type(A)}")
print(f"Conjunto B : {B} -- {len(B)} -- {type(B)}")

print(f"\nUnion (A | B)                : {A | B}")
print(f"Interseccion (A & B)         : {A & B}")
print(f"Diferencia (A - B)           : {A - B}")
print(f"Diferencia simetrica (A ^ B) : {A ^ B}")

C = {"Pablo","Mateo"}
D = {"Reynaldo","Angelica"}

print(f"\nEl conjunto {C} es subconjunto de B       ? --- {C.issubset(B)}")
print(f"A es superconjunto del conjunto {D} ? --- {A.issuperset(D)}")

print(f"\nEl elemento 'Pedro' esta en A    ? --- {"Pedro" in A}")
print(f"El elemento 'Lilia' no esta en B ? --- {"Lilia" not in B}\n")