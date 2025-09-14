# Modelo de Predicción de Dígitos Escritos a Mano

Este repositorio contiene un modelo de aprendizaje automático para reconocer y predecir dígitos escritos a mano a partir de imágenes en escala de grises. El proyecto utiliza TensorFlow/Keras para el preprocesamiento, entrenamiento y evaluación del modelo.

## Datos: MNIST
- Conjunto de datos: MNIST (Modified National Institute of Standards and Technology), un conjunto clásico con 60,000 imágenes para entrenamiento y 10,000 para prueba de dígitos del 0 al 9.
- Formato: imágenes de 28x28 píxeles en escala de grises, con su etiqueta correspondiente.
- Cita recomendada:
  - LeCun, Y., Cortes, C., & Burges, C. J. C. (1998). The MNIST database of handwritten digits. Disponible en: http://yann.lecun.com/exdb/mnist/

## Tecnologías
- TensorFlow/Keras para el modelado y entrenamiento
- Python 3.10+ (recomendado)
- NumPy, Matplotlib y herramientas comunes del ecosistema científico de Python

## Estructura del proyecto
- `handwritting_digits/dataset/dataset.ipynb`: Cuaderno con el flujo de extracción de los datos.
- - `handwritting_digits/model/model.ipynb`: Cuaderno para generar el modelo, deacuerdo a las características de la base de datos.
- `handwritting_digits/train/train.ipynb`: Cuaderno principal con el flujo de entrenamiento, evaluación e inferencia.
- `requirements.txt`: Dependencias del proyecto.

## Cómo ejecutar
1. Crear y activar un entorno virtual (opcional pero recomendado).
2. Instalar dependencias: `pip install -r requirements.txt`.
3. Abrir y ejecutar el cuaderno `handwritting_digits/train/train.ipynb` en Jupyter (o VS Code/Jupyter Lab) para:
   - Descargar/cargar MNIST (vía `tensorflow.keras.datasets.mnist`).
   - Normalizar y preparar los datos.
   - Definir, compilar y entrenar el modelo en TensorFlow.
   - Evaluar el desempeño en el conjunto de prueba.
   - Realizar predicciones de ejemplo sobre imágenes nuevas o del set de prueba.

## Notas
- La precisión final depende de la arquitectura y los hiperparámetros elegidos (épocas, tamaño de lote, tasa de aprendizaje, etc.).
- El cuaderno incluye celdas comentadas para guiar el proceso de principio a fin.

## Agradecimientos
- A los autores y mantenedores del conjunto de datos MNIST: Y. LeCun, C. Cortes y C. J. C. Burges.
- A la comunidad de TensorFlow por la infraestructura de código abierto que facilita el desarrollo de modelos de aprendizaje profundo.
