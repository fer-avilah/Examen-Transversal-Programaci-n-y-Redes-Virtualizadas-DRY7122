distancias = {
    ("Santiago", "Mendoza"): 370
}

# Velocidades promedio en km/h
velocidades = {
    "auto": 80,
    "bus": 60,
    "avión": 700
}

print("Calculadora de Viajes (escribe 's' para salir)\n")

while True:
    origen = input("Ciudad de Origen: ").title()
    if origen.lower() == 's':
        break

    destino = input("Ciudad de Destino: ").title()
    if destino.lower() == 's':
        break

    medio = input("Medio de transporte (auto, bus, avión): ").lower()
    if medio == 's':
        break

    if (origen, destino) in distancias and medio in velocidades:
        km = distancias[(origen, destino)]
        millas = round(km * 0.621371, 2)
        velocidad = velocidades[medio]
        tiempo_horas = round(km / velocidad, 2)

        print("\nNarrativa del viaje")
        print(f"Desde {origen} hasta {destino} utilizando un {medio}.")
        print(f"Distancia total: {km} km ({millas} millas).")
        print(f"Duración aproximada: {tiempo_horas} horas.\n")
    else:
        print("Datos no válidos. Intenta nuevamente.\n")