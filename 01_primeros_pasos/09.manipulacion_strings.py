"""
Tema: Manipulación de strings — slicing, replace, split
Conceptos clave: texto[inicio:fin:paso], el fin NUNCA se incluye,
índices negativos, replace(), split().
Error común de estudiantes: esperar que texto[0:4] incluya el
índice 4 — el límite superior siempre queda afuera.
"""

# Regla de oro del slicing:  texto[inicio:fin:paso]
# - inicio: se INCLUYE (default: 0)
# - fin:    se EXCLUYE (default: final del texto)
# - paso:   de a cuántos avanza (default: 1; negativo = al revés)

#          índices:  0123456789...
texto = "Este es un texto"
#        E=0, s=1, t=2, e=3, (espacio)=4, e=5 ...

# ============ ACCESO E ÍNDICES ============
print(texto[0])    # E  (primer carácter)
print(texto[-1])   # o  (índices negativos cuentan desde el final)

# ============ RANGOS ============
print(texto[0:4])   # Este  (índices 0,1,2,3 — el 4 queda AFUERA)
print(texto[:4])    # Este  (sin inicio = desde 0)
print(texto[5:])    # es un texto  (desde el índice 5 hasta el FINAL)
print(texto[:-2])   # Este es un tex  (todo menos los 2 últimos)

# ============ PASO ============
print(texto[::2])    # Et su et  (cada 2 caracteres)
print(texto[1::2])   # see ntxo  (cada 2, arrancando en el índice 1)
print(texto[::3])    # Ee ntt  (cada 3)
print(texto[1:10:2]) # seé n  (del 1 al 9, de a 2)

# ============ PASO NEGATIVO: recorrer al revés ============
print(texto[::-1])    # otxet nu se etsE  (¡texto invertido!)
print(texto[10:1:-2]) # nues  (del 10 hacia el 2, de a 2, al revés)

# ============ replace(): reemplazar texto ============
curso = "Este curso es de Javascript"
print(curso.replace("Javascript", "Python"))
# Ojo: replace NO modifica 'curso', devuelve un string NUEVO
print(curso)  # sigue diciendo Javascript

# ============ split(): dividir en una LISTA ============
texto_dividido = texto.split(" ")
print(texto_dividido)  # ['Este', 'es', 'un', 'texto']

# ============ BÚSQUEDA SIN DISTINGUIR MAYÚSCULAS ============
texto2 = "Este texto tiene MAYUSCULAS y minusculas"
print("mayusculas".lower() in texto2.lower())  # True