# Sistema de Reservación de Hoteles - Actividad 6.2

Este proyecto consiste en un sistema básico de reservación de hoteles desarrollado en Python. La aplicación permite gestionar información de hoteles, clientes y reservaciones con persistencia de datos en archivos JSON.

**Estudiante:** Fernando Pérez Escalante  
**Matrícula:** A01796934  
**Materia:** Pruebas de Software y Aseguramiento de la Calidad

## Estructura del Proyecto

- `src/`: Contiene el código fuente de las clases (`Hotel`, `Customer`, `Reservation`).
- `tests/`: Contiene las pruebas unitarias desarrolladas con el módulo `unittest`.
- `data/`: Directorio donde se almacenan los archivos JSON de persistencia.

## Requisitos de Calidad Cumplidos

### 1. Estándar de Codificación (PEP8)
El código ha sido validado con **Flake8** y **Pylint**, obteniendo una calificación de **10/10** en todos los módulos principales.
- Sin errores de estilo.
- Sin espacios en blanco al final de las líneas.
- Complejidad ciclomática controlada.

### 2. Pruebas Unitarias y Cobertura
Se implementaron pruebas para todos los métodos, incluyendo **más de 5 casos negativos** (manejo de archivos corruptos, IDs inexistentes, errores de permisos).

**Cobertura de código alcanzada:** > 85% (según requerimiento).

### 3. Manejo de Errores
El sistema implementa bloques `try-except` para manejar datos inválidos en los archivos. En caso de error, se notifica en consola y la ejecución continúa sin interrumpirse.

## Instrucciones de Ejecución

1. **Instalar dependencias de desarrollo:**
   ```bash
   pip install flake8 pylint coverage
