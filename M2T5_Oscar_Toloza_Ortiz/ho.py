def ends_with_ing_or_ion(s):
    s = s.lower()  # Ignorar mayúsculas
    return s.endswith('ing') or s.endswith('ion')

# Ejemplos de prueba
print(ends_with_ing_or_ion('action'))  # True
print(ends_with_ing_or_ion('Running')) # True
print(ends_with_ing_or_ion('hello'))   # False
