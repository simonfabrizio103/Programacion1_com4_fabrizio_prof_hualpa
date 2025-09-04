auto_consume = 8

print()
distancia = int(input("Por favor, ingresa la distancia en KM "))
precio = float(input("Por favor, ingresa el precio de gasolina por litro "))
print()

litros_consumidos = distancia/100*8

costo_viaje = litros_consumidos*precio

horas = distancia/90

print(f'Se necesitan {litros_consumidos} litros para realizar el viaje')
print()
print(f'El viaje costará {costo_viaje}$')
print()
print(f'Tardará {horas} horas si la velocidad promedio es de 90km/h')