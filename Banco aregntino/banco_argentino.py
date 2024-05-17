from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Cargar los datos
datos = pd.read_excel('Libro1.xlsx') #Carga de los datos de excel
X = datos.iloc[:, 0:4].values

# Definir las reglas de asociación
def fiabilidad(edad, ingresos):
    if edad < 25 or ingresos < 29000:
        return 0
    else:
        return 1

# Aplicar las reglas de asociación para etiquetar los datos
datosbuenos = [fiabilidad(edad, ingresos) for estado_civil, genero, edad, ingresos in X]

# Convertir etiquetas a matriz numpy
Y = np.array(datosbuenos)

# Imprimir Y
print(Y)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_datos, Y_entrenamiento, Y_datos = train_test_split(X, Y, test_size=0.5, random_state=42)  # 50% de los datos para entrenamiento

# Crea el modelo+
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_entrenamiento, Y_entrenamiento, epochs=150, batch_size=32, validation_data=(X_datos, Y_datos))

# Evaluar el modelo
test_loss, test_acc = model.evaluate(X_datos, Y_datos)
print('Precisión en el conjunto de prueba: %.2f%%' % (test_acc*100))