# 01. Digit Recognizer

Este modelo se entreno con la base de datos MNIST encontrada en keras

## Pasos:

- Se carga el MNIST dataset
- Se crean varios modelos de redes neuronales para ver cual tiene mayor precision

Resulta el modelo 6 el mejor

- Guardado del modelo CNN (convolutional neural network)

En el archivo MNIST_CNN_final.ipynb:

- Se carga el modelo
- Descargar el test_set de kaggle correspondiente a este trabajo
- Se transforman los 784 valores correspondientes a cada ejemplo en matrices de 28x28 (hacemos el test_set compatible con el modelo anteriormente creado)
- Se reduce la escala de todos los valores dividiendo por el valor maximo encontrado (255)
- Se realizan las predicciones
- Se almacenan los resultados en un .txt que luego se debe transformar a .cvs para subir a Kaggle.

### Los resultados mostraron 0.997 de presición, posicionando al modelo dentro de los 100 mejores de la competencia.