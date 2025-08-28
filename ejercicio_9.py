m_solicitado = int(input("Ingrese el monto solicitado "))
mes_cuota = int(input("Ingrese el mes de cuota que quiere saber "))
print()

m_total = m_solicitado * (1+0.02)**12
valor_cuota = m_solicitado * (1+0.02)**mes_cuota
valor_real = m_solicitado * (1+0.02)**(mes_cuota-1)

print("Valor del monto total ")
print(m_total)
print()
print("Valor de la cuota número",mes_cuota)
print(valor_cuota-valor_real)
