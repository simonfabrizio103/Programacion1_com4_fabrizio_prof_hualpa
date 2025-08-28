print()
parcial_1 = float(input("Porfavor ingresa la calificación de tu primer parcial "))
print()
parcial_2 = float(input("Porfavor ingresa la calificación de tu segundo parcial "))
print()
parcial_3 = float(input("Porfavor ingresa la calificación de tu tercer parcial "))
print()

promedio = (parcial_1 + parcial_2 + parcial_3) / 3

examen_final = float(input("Porfavor ingresa la calificación de tu examen final "))
print()
trabajo_final = float(input("Porfavor ingresa la calificación de tu trabajo final "))
print()
nota_final = 0.55*promedio + 0.30*examen_final + 0.15*trabajo_final

print("Tu nota final es: ",nota_final)