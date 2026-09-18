# 🛒 Sistema de Reabastecimiento para Supermercado

Script en Python diseñado para simular la gestión de stock en góndolas, identificando productos críticos y reorganizando el inventario de forma automática.

## 🚀 Funcionalidades
- **Gestión de Stock:** Representación de productos mediante tuplas `(Nombre, Stock, Categoría)`.
- **Detección de Stock Crítico:** Ordenamiento dinámico utilizando la función `lambda` para priorizar el producto con menor cantidad disponible.
- **Extracción e Informe:** Uso de `.pop()` para retirar el producto urgente a reponer y notificar la alerta en consola.
- **Reordenamiento:** Clasificación alfabética del inventario restante.

## 🛠️ Tecnologías utilizadas
- **Lenguaje:** Python 3.x
- **Métodos y funciones clave:** `.sort()`, `lambda`, `.pop()`, f-strings para formateo de tablas en consola.

## 📋 Cómo ejecutarlo
1. Clona el repositorio o descarga el archivo `supermercado.py`.
2. Ejecuta el script desde la consola:
   ```bash
   python supermercado.py