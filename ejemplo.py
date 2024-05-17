from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Cargar los datos
dataset = pd.read_excel('Libro1.xlsx') 
datosX = dataset.iloc[:, 0:4].values

# Definir las reglas de asociación
def es_fiable(estado_civil, genero, edad, ingresos):
    if edad < 25 or ingresos < 29000:
        return 0
    else:
        return 1

# Aplicar las reglas de asociación para etiquetar los datos
datosbuenos = [es_fiable(estado_civil, genero, edad, ingresos) for estado_civil, genero, edad, ingresos in datosX]

# Convertir etiquetas a matriz numpy
y = np.array(datosbuenos)

# Imprimir Y
print(y)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_datos, y_entrenamiento, y_datos = train_test_split(datosX, y, test_size=0.3, random_state=42)

# Crea el modelo
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_entrenamiento, y_entrenamiento, epochs=150, batch_size=32, validation_data=(X_datos, y_datos))

# Evaluar el modelo
test_loss, test_acc = model.evaluate(X_datos, y_datos)
print('Precisión en el conjunto de prueba: %.2f%%' % (test_acc*100))