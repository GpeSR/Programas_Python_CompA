# Calcular el pago total de un trabajador 

print('Calculando el pago de un trabajador \n')


nombre = input('Nombre del trabajador: ')
horas  = int(input('Ingrese la cantidad de horas trabajadas: '))
pago   = float(input('Ingrese el pago por hora: '))

tasa = 0.3

pagabruta = horas * pago
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print('\n\nResumen de pagos:\n')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una paga de {pago} pesos por hora, con un impuesto del {tasa}%')
print(f'Paga bruta {pagabruta:.2f}')
print(f'Impuesto   {impuesto:.2f}')
print(f'Paga neta  {paganeta:.2f}')