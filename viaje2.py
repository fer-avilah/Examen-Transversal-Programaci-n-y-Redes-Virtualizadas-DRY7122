distancias = {
    ("Santiago", "Mendoza"): 370
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

    if (origen, destino) in distancias:
        km = distancias[(origen, destino)]
        millas = round(km * 0.621371, 2)

        print("\n narrativa del viaje")
        print(f"Desde {origen} hasta {destino} utilizando un {medio}.")
        print(f"Distancia total: {km} km ({millas} millas).\n")
    else:
        print("Datos no válidos. Intenta nuevamente.\n")

