print()
monto_dolares = int(input("Porfavor ingresa un monto en dólares "))
print()

PESOS_COL = monto_dolares * 4030.36
PESOS_ARG = monto_dolares * 1350.99
EUROS = monto_dolares * 0.86

print(f'{monto_dolares} dólares en pesos colombianos son: {PESOS_COL}')
print()
print(f'{monto_dolares} dólares en pesoss argentinos son: {PESOS_ARG}')
print()
print(f'{monto_dolares} dólares en euros son: {EUROS}')