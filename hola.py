# Investigando excepciones
try:
    with open("archivo_inexistente.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError as e:
    print("Excepción original:", e)
    print("Error: No se pudo abrir el archivo. Asegúrate de que el archivo existe y la ruta es correcta.")
