# Guía para Desarrolladores de la Calculadora Matemática

Esta guía está destinada a los desarrolladores interesados en contribuir al proyecto de la Calculadora Matemática en Python o aquellos que deseen comprender su estructura interna.

## Estructura del Proyecto

La estructura del proyecto se divide en varios componentes:

- `calculadora.py`: El módulo principal que maneja el menú y la lógica de la calculadora.
- `operaciones/`: Un paquete que contiene módulos para realizar diferentes operaciones matemáticas.
- `validaciones.py`: Un módulo para funciones de validación de entrada de usuario.
- `tests/`: Carpeta con pruebas unitarias para las operaciones y la calculadora.

## Cómo Ejecutar las Pruebas

Puedes ejecutar las pruebas unitarias utilizando la biblioteca `pytest`. Asegúrate de tener todas las dependencias instaladas:

```bash
pip install -r requirements.txt
