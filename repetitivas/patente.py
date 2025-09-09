import sys

lista_abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
patente = ["A","A","A",0,0,0]
num_patente = 0
patente_usuario = int(input("Por favor, ingresa el número de patente (desde 1 hasta 175760000) "))

for i in range(len(lista_abc)):
    for j in range(len(lista_abc)):
        for k in range(len(lista_abc)):
            for x in range(10):
                for y in range(10):
                    for z in range(10):
                        patente = [lista_abc[i], lista_abc[j], lista_abc[k], x, y, z]
                        if num_patente == patente_usuario:
                            print(f'Tu patente número {patente_usuario} es: {patente}')
                            sys.exit()
                        num_patente += 1