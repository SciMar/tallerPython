"""
Tema: Variables y convenciones de nombres
Conceptos clave: reglas de nombres válidos, snake_case, camelCase,
PascalCase, constantes en MAYÚSCULAS, _prefijo_privado.
Error común de estudiantes: empezar nombres con número o usar
guion medio (mi-variable), que Python interpreta como resta.
"""

# ============ NOMBRES VÁLIDOS ============
mivariable = 1        # solo minúsculas
mi_variable = 2       # snake_case (la convención oficial de Python)
_mi_variable = 3      # guion bajo inicial: uso "privado"
miVariable = 4        # camelCase (válido, pero no es el estilo Python)
MiVariable = 5        # PascalCase (se reserva para nombres de clases)
MIVARIABLE = 6        # MAYÚSCULAS: se reserva para constantes
mi_variable2 = 7      # números sí, pero nunca al inicio

# ============ NOMBRES INVÁLIDOS ============
# (descomentar en clase para ver cada error)

# 2variable = 1      # ❌ SyntaxError: no puede empezar con número
# mi-variable = 1    # ❌ Python lo lee como resta: mi - variable
# mi variable = 1    # ❌ SyntaxError: no se permiten espacios

# ============ CONVENCIONES EN LA PRÁCTICA ============

# snake_case → variables y funciones (el estándar en Python, PEP 8)
nombre_estudiante = "Marcela"

# MAYÚSCULAS → constantes (valores que no deben cambiar)
PI = 3.14159
IVA = 0.19

# PascalCase → clases (lo verán más adelante)
# class MiClase: ...

# _guion_bajo_inicial → "no tocar desde afuera" (privado por convención)
_contador_interno = 0

print(nombre_estudiante)
print(f"El IVA es {IVA}")