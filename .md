# 🚀 Guía de Configuración del Entorno de Desarrollo

Antes de empezar a construir el compilador basado en reglas, debemos unificar el entorno de trabajo y seguir una estructura clara para evitar errores.

## 1. Requisitos previos: instalar Python
Utilizaremos Python para el Lexer, Parser, AST e Intérprete. Instala una versión reciente: **Python 3.10 o superior**.

- **Windows / macOS**
  - Descarga el instalador en [python.org](https://www.python.org/downloads/).
  - En Windows, marca `Add Python to PATH` durante la instalación.
- **Linux**
  - Verifica la instalación con:

    ```bash
    python3 --version
    ```

## 2. Clonar el repositorio
Abre tu terminal favorita y clona el repositorio:

```bash
git clone https://github.com/JoanP-B/practica_3_lenguajes_formales.git

cd practica_3_lenguajes_formales
```


## 3. Crear y activar un entorno virtual
Siempre trabaja dentro de un entorno virtual para evitar conflictos entre dependencias.

### En Windows

Ejecutar esto en una terminal dentro del proyecto

```bash
python -m venv venv
venv\Scripts\activate
```

### En macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Cuando el entorno está activado, verás un prefijo similar a `(venv)` al inicio de la línea de comandos.

## 4. Instalar dependencias

Con el entorno virtual activado, instala los paquetes listados en `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 5. Flujo de trabajo con Git

Para trabajar en equipo, usa ramas independientes. No trabajes directamente en `main`.

### Actualizar el repositorio local

```bash
git pull origin main
```

### Crear tu rama de trabajo

- Para P1: `git checkout -b feat/p1-lexer-parser`
- Para P2: `git checkout -b feat/p2-ast-interpreter`
- Para P3: `git checkout -b feat/p3-static-analysis`

### Confirmar y subir cambios

```bash
git add .
git commit -m "Descripción clara de lo que hiciste. Ej: Añade el lexer base"
git push origin <nombre-de-tu-rama>
```
