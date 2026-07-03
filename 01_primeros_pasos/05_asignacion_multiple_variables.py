"""
Tema: Asignación múltiple de variables
Conceptos clave: asignación por posición, asignación en cadena,
desempaquetado, intercambio de valores (swap).
Error común de estudiantes: que la cantidad de variables no
coincida con la cantidad de valores (ValueError).
"""

# ============ VARIAS VARIABLES, VARIOS VALORES ============
# La asignación es por posición: primera con primera, etc.
fruta1, fruta2, fruta3 = "manzana", "naranja", "banana"
print(fruta1, fruta2, fruta3)

# ⚠️ Las cantidades deben coincidir:
# a, b = "manzana", "naranja", "banana"
# ValueError: too many values to unpack (expected 2)

# ============ VARIAS VARIABLES, UN MISMO VALOR ============
# Asignación en cadena: las tres apuntan al mismo valor
color_fondo = color_borde = color_texto = "mandarina"
print(color_fondo, color_borde, color_texto)

# ============ INTERCAMBIO DE VALORES (swap) ============
# El truco clásico de Python: sin variable temporal
a = "primero"
b = "segundo"
a, b = b, a
print(a, b)  # segundo primero

# ============ DESEMPAQUETAR UNA LISTA ============
frutas = ["manzana", "naranja", "banana"]
f1, f2, f3 = frutas
print(f1, f2, f3)