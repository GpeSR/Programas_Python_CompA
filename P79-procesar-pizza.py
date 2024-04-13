# Procesa el pedido de una pizza en base a los ingredientes 

import os; os.system("cls")

ingr = {"T":1.50,"P":3.50,"C":3.74,"A":0.40,"Q":4}
base = 15
st = 0 # subtotal
tot = 0
des = 0

pedido = input("Ingredientes de tu pizza ? ").upper()
for i in pedido:
    if i in "PTCAQ":
        st = st + ingr[i]

st = st + base

if st >= 20:
    des = st * 0.05
    tot = st - des 

print(f"\nEl subtotal es : {st}, con un descuento de {des:.2f} (5%)")
print(f"El total es    : {tot}")
