
# -------------------------
# Ejercicio 1: Sumatoria de no negativos
# -------------------------
def sumatoria_positivos(nums):
    """
    Devuelve la suma de los valores mayores o iguales a 0 de una lista de enteros.
    """
    total = 0
    for n in nums:
        if n >= 0:
            total += n
    return total

# -------------------------
# Ejercicio 2: Palíndromo básico
# -------------------------
def es_palindromo(s: str) -> bool:
    """
    Devuelve True si la cadena es un palíndromo, ignorando mayúsculas y espacios.
    """
    s = s.lower().replace(' ', '')
    return s == s[::-1]

# -------------------------
# Ejercicio 3: Máximo con control de errores
# -------------------------
def maximo_seguro(nums):
    """
    Devuelve el máximo de la lista. Lanza ValueError si la lista está vacía.
    """
    if not nums:
        raise ValueError('lista vacía')
    maximo = nums[0]
    for n in nums[1:]:
        if n > maximo:
            maximo = n
    return maximo

# -------------------------
# Ejercicio 4: Contador simple de palabras
# -------------------------
def contar_palabras(texto: str) -> dict:
    """
    Devuelve un diccionario con el conteo de cada palabra en el texto,
    ignorando mayúsculas/minúsculas.
    """
    conteo = {}
    for palabra in texto.lower().split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

# -------------------------
# Ejercicio 5: Filtrar aprobados
# -------------------------
def filtrar_aprobados(pares):
    """
    Recibe una lista de tuplas (nombre, nota) y devuelve una lista con
    los nombres de quienes tienen nota >= 5, conservando el orden.
    """
    resultado = []
    for nombre, nota in pares:
        if nota >= 5:
            resultado.append(nombre)
    return resultado

# -------------------------
# Ejercicio 6: Normalizar email
# -------------------------
def normalizar_email(email: str):
    """
    Devuelve (usuario, dominio) en minúsculas. Lanza ValueError si el formato es incorrecto.
    """
    if email.count('@') != 1:
        raise ValueError('email inválido')
    usuario, dominio = email.split('@')
    return usuario.lower(), dominio.lower()

# -------------------------
# Ejercicio 7: Factorial iterativo con control de errores
# -------------------------
def factorial(n: int) -> int:
    """
    Calcula el factorial de n (n!). Lanza ValueError si n es negativo.
    """
    if n < 0:
        raise ValueError('n negativo')
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

# -------------------------
# Ejercicio 8: Media aritmética
# -------------------------
def media(nums):
    """
    Calcula la media de una lista no vacía de números.
    Lanza ValueError si la lista está vacía.
    """
    if not nums:
        raise ValueError('lista vacía')
    return sum(nums) / len(nums)
