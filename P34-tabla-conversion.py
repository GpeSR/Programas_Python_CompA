# Imprimir una tabla de conversion de peso a dolar usando while

while(True):
    import os; os.system("cls")
    tc = 17.00

    print("Tabla de conversion de peso a dolar : \n")
    pi = float(input("Valor inicial: "))
    pf = float(input("Valor final: "))

    c = pi

    print("\nPeso\tDolar")
    print("-"*15)

    while c <= pf:
        print(f"{c}\t{c/tc:.2f}")
        c = c + 1

    print("-"*15)

    res = input("Deseas continuar (S/N) ? ")
    if res.upper() == "N": break

print("\nProceso terminado :)")