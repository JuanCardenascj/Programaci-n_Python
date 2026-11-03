"""Crea estas variables:
vida_garen = 5000vida_ahri = 4500dano_garen = 1200dano_ahri = 1000



Simula esta secuencia:
1. Ahri ataca a Garen.
2. Garen ataca a Ahri.
3. Ahri vuelve a atacar a Garen.
4. Garen vuelve a atacar a Ahri.
Muestra la vida restante de ambos al finalizar.

Condición: utiliza variables para actualizar la vida. No escribas directamente los resultados de las operaciones."""

vida_garen = 5000
vida_ahri = 4500
daño_garen = 1200
daño_ahri = 1000

#1. Ahri ataca a garen
vida_garen -= daño_ahri
#2. Garen ataca a Ahri
vida_ahri -= daño_garen
#3. Ahri vuelve a atacar a Garen
vida_garen -= daño_ahri
#4. Garen vuelve a atacar a Ahri
vida_ahri -= daño_garen

print(f"Vida restante de Garen: {vida_garen}")
print(f"Vida restante de Ahri: {vida_ahri}")