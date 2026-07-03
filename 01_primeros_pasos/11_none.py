"""
Tema: None — la ausencia de valor
Conceptos clave: NoneType, is None, truthy/falsy de None,
diferencia entre None y valores vacíos.
Error común de estudiantes: comparar con == None en vez de is None,
y confundir None con 0 o con "".
Analogía útil: None es el NULL de SQL.
"""

# None representa la AUSENCIA de valor — no un valor vacío.
# Un string vacío "" ES un valor (un texto sin letras).
# None es "aquí no hay nada".

x = None
print(x)        # None
print(type(x))  # <class 'NoneType'>

# None es un singleton: existe UNA sola instancia en todo el programa.
# Por eso se compara con "is" (identidad) y no con "==" (PEP 8 lo exige):
if x is None:
    print("Es None")

# ============ None es falsy ============
if x:
    print("No se ejecuta")
else:
    print("Se ejecuta")  # ← None se evalúa como False

# ============ OPERADOR TERNARIO (primera aparición 👀) ============
# Sintaxis Python:  valor_si_verdadero if condición else valor_si_falso
# (en Java/JS sería: condición ? valorSi : valorNo)
print("Es None" if x is None else "No es None")

# ============ ¿DÓNDE APARECE None EN LA VIDA REAL? ============

# 1. Funciones que no retornan nada devuelven None:
resultado = print("hola")
print(resultado)  # None — print no retorna valor

# 2. Variables declaradas "para después":
ganador = None  # aún no sabemos quién ganó

# 3. Búsquedas sin resultado (lo verán con diccionarios):
persona = {"nombre": "Ari"}
print(persona.get("edad"))  # None — la clave no existe

# ============ None NO es lo mismo que "vacío" ============
print(type(""))     # <class 'str'>    — string vacío
print(type(0))      # <class 'int'>    — el número cero
print(type(False))  # <class 'bool'>   — falso
print(type([]))     # <class 'list'>   — lista vacía
print(type(()))     # <class 'tuple'>  — tupla vacía
print(type({}))     # <class 'dict'>   — diccionario vacío
print(type(set()))  # <class 'set'>    — conjunto vacío
print(type(None))   # <class 'NoneType'> — la nada 😄