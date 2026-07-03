"""
Tema: Manipulación y conversión de tipos (casting)
Conceptos clave: type(), int(), float(), complex(), str(), abs(), random.
Error común de estudiantes: creer que int(2.9) redondea (da 2, trunca)
y olvidar que input() siempre devuelve string.
"""

import random  # los imports SIEMPRE van al inicio del archivo

# ============ type(): conocer el tipo de dato ============
x = 1       # int (del inglés "integer": entero)
y = 2.5     # float (punto flotante)
z = 1j      # complex (complejo)

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# ============ CASTEO: int ↔ float ============
xf = float(x)
print(xf, type(xf))  # 1.0 <class 'float'>

ye = int(y)
print(ye, type(ye))  # 2 <class 'int'>

# ⚠️ int() TRUNCA, no redondea: corta los decimales hacia cero.
print(int(2.9))    # 2  (no 3)
print(int(-2.9))   # -2 (no -3): trunca hacia cero
print(round(2.9))  # 3  ← para redondear de verdad existe round()

# ============ CASTEO: strings ↔ números ============
# Fundamental: input() SIEMPRE devuelve string
edad_texto = "25"
edad = int(edad_texto)
print(edad + 1, type(edad))  # 26 <class 'int'>

numero = 3.14
texto = str(numero)
print(texto, type(texto))  # 3.14 <class 'str'>

# int("hola")  # ❌ ValueError: solo se convierten strings numéricos

# ============ NÚMEROS COMPLEJOS ============
imaginario = 5 + 1j

# No se puede convertir complejo → int directamente,
# pero abs() devuelve su magnitud: sqrt(real² + imag²)
magnitud = abs(imaginario)
print(magnitud)  # 5.0990195135927845

# Casteo a complejo: se agrega la parte imaginaria 0j
print(complex(5))     # (5+0j)
print(complex(5.5))   # (5.5+0j)

# ============ NÚMEROS ALEATORIOS ============
# El módulo random genera valores impredecibles
print(random.randrange(1, 10))  # entre 1 y 9 (el 10 NO se incluye)
print(random.randint(1, 10))    # entre 1 y 10 (ambos incluidos)