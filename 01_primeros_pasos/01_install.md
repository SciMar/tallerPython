# 01 — Instalación y configuración del entorno

## Herramientas necesarias

- **VS Code** — editor de código
- **Git** — control de versiones
- **Python** — descargar desde python.org (marcar "Add Python to PATH" ⚠️)

## Extensiones de VS Code

- **Python** (Microsoft) — soporte del lenguaje
- **Pylance** — autocompletado e IntelliSense
- **Jupyter** — notebooks interactivos

## Configuración

- Crear un *profile* en VS Code para el entorno de Python
- Verificar la instalación en la terminal:

```bash
python --version
git --version
```

## Variables de entorno

- Confirmar que Python está en el PATH del sistema
- Si `python --version` falla en la terminal, revisar PATH en
  Configuración → Variables de entorno

## 🎓 Nota para clases

**Error común de estudiantes:** instalar Python sin marcar
"Add Python to PATH" — la terminal no reconoce el comando `python`.
Solución rápida: reinstalar marcando la casilla.