# Notas de Diseño de la Calculadora Matemática

Este documento contiene notas de diseño que explican las decisiones y consideraciones clave relacionadas con la estructura y el diseño de la Calculadora Matemática en Python.

## Estructura de Directorios

El proyecto sigue una estructura de directorios organizada para facilitar el mantenimiento y la expansión. Aquí está una descripción general de la estructura:

- `calculadora.py`: El módulo principal que controla el flujo de la aplicación.
- `operaciones/`: Un paquete que contiene módulos para operaciones matemáticas individuales.
- `validaciones.py`: Un módulo para funciones de validación de entrada de usuario.
- `tests/`: Carpeta que alberga pruebas unitarias para todas las operaciones.

## Modularidad

La calculadora se implementa de manera modular. Cada operación matemática tiene su propio módulo en el paquete `operaciones`, lo que facilita la adición y modificación de operaciones en el futuro.

## Pruebas Unitarias

Se han creado pruebas unitarias para cada operación matemática utilizando la biblioteca `pytest`. Esto garantiza que las operaciones funcionen correctamente y ayuda a mantener la calidad del código.

## Extensibilidad

El diseño de la calculadora está orientado a la extensibilidad. Los nuevos módulos de operaciones se pueden agregar fácilmente al paquete `operaciones` sin afectar la lógica principal de la calculadora.

## Control de Errores

Se implementa un manejo de errores sólido para garantizar que la calculadora maneje situaciones inesperadas, como la división por cero o la entrada incorrecta del usuario, de manera adecuada.

## Documentación

La documentación se mantiene actualizada en los archivos README.md y en las guías de usuario y desarrollador para garantizar que los usuarios y colaboradores puedan comprender y utilizar el proyecto de manera efectiva.

## Contribuciones

Se alientan las contribuciones de otros desarrolladores. Los contribuyentes pueden enviar solicitudes de extracción (pull requests) en el repositorio de GitHub para mejorar la calculadora.

## Futuras Mejoras

Se planean futuras mejoras, como la adición de nuevas operaciones matemáticas y la creación de una interfaz de usuario gráfica (GUI) para la calculadora.