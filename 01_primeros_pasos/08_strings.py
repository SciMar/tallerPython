"""
Tema: Strings y sus métodos básicos
Conceptos clave: comillas anidadas, len(), in / not in,
upper(), lower(), strip(), concatenación vs suma.
Error común de estudiantes: "5" + "6" da "56" (concatena),
no 11 — los strings con números siguen siendo texto.
"""

# ============ COMILLAS ANIDADAS ============
# Comillas dobles afuera → simples adentro, y viceversa
print('Hola "Mundo"')
saludo_ingles = "I'm Ari"  # la doble protege el apóstrofo
print(saludo_ingles)

# ============ SALTOS DE LÍNEA ============
multilinea = """Hola
Mundo
desde
comillas
triples"""
print(multilinea)
print()  # print() vacío = línea en blanco (separador)

# ============ len(): cantidad de caracteres ============
palabra = "Murciélago"
print(len(palabra))  # 10 — cuenta letras, espacios, símbolos

# ============ BUSCAR DENTRO DE UN TEXTO (case sensitive) ============
texto_curso = "Este curso es de fundamentos de Python"

esta_incluida = "Python" in texto_curso
print(esta_incluida)   # True

no_esta_incluida = "Python" not in texto_curso
print(no_esta_incluida)  # False

print("python" in texto_curso)  # False ⚠️ ¡mayúsculas importan!

# ============ MAYÚSCULAS / MINÚSCULAS ============
print(texto_curso.upper())

fecha = "HOY ES 4 DE NOVIEMBRE"
print(fecha.lower())

# Truco de clase: comparar sin importar mayúsculas
print("PYTHON".lower() in texto_curso.lower())  # True

# ============ strip(): limpiar espacios en los extremos ============
con_espacios = "     Este es el texto       "
print(con_espacios.strip())
# Muy usado al limpiar lo que escribe un usuario en input()

# ============ CONCATENAR vs SUMAR ============
print("5" + "6")   # "56" → con strings, + concatena
print(5 + 6)       # 11  → con números, + suma
# print("5" + 6)   # ❌ TypeError: no se mezclan tipos
