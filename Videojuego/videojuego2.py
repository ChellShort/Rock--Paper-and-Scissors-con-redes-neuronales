from keras.models import Sequential
from keras.layers import Dense
import numpy

# Fija las semillas aleatorias para la reproducibilidad
numpy.random.seed(7)

# Carga los datos
dataset = numpy.loadtxt("Videojuego/videojuego.csv", delimiter=",")

# Dividir en variables de entrada (X) y salida (Y)
X = dataset[:,0:4]
Y = dataset[:,4]

# Dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Crea el modelo
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='softmax'))

# Compila el modelo
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrena el modelo
model.fit(X_train, y_train, epochs=120, batch_size=10, validation_data=(X_test, y_test))

# Evalúa el modelo en el conjunto de prueba
scores = model.evaluate(X_test, y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

#--------------------------------------------------------------------------------------------------------------------------------------------

print("Hagamos una predicción!")
resultado = model.predict(numpy.array([[0,1,1,3]]))  # Convertir lista a arreglo numpy
print("El resultado es " + str(resultado[0][0]))
print("El resultado es " + str(resultado[0][1]))
print("El resultado es " + str(resultado[0][2]))
print("El resultado es " + str(resultado[0][3]))

# Encuentra el índice del valor más grande en las predicciones
indice_maximo = numpy.argmax(resultado)


# Imprime el valor más grande
print("El resultado más grande es:", resultado[0][indice_maximo])

# Imprime el array correspondiente al valor más grande
print("El array donde se encontró el valor más grande es:", numpy.argmax(resultado))

#--------------------------------------------------------------------------------------------------------------------------------------------

print("Hagamos una predicción!")
resultado = model.predict(numpy.array([[1,1,1,2]]))  # Convertir lista a arreglo numpy
print("El resultado es " + str(resultado[0][0]))
print("El resultado es " + str(resultado[0][1]))
print("El resultado es " + str(resultado[0][2]))
print("El resultado es " + str(resultado[0][3]))

# Encuentra el índice del valor más grande en las predicciones
indice_maximo = numpy.argmax(resultado)

# Imprime el valor más grande
print("El resultado más grande es:", resultado[0][indice_maximo])

# Imprime el array correspondiente al valor más grande
print("El array donde se encontró el valor más grande es:", numpy.argmax(resultado))

#--------------------------------------------------------------------------------------------------------------------------------------------

print("Hagamos una predicción!")
resultado = model.predict(numpy.array([[1,0,1,2]]))  # Convertir lista a arreglo numpy
print("El resultado es " + str(resultado[0][0]))
print("El resultado es " + str(resultado[0][1]))
print("El resultado es " + str(resultado[0][2]))
print("El resultado es " + str(resultado[0][3]))

# Encuentra el índice del valor más grande en las predicciones
indice_maximo = numpy.argmax(resultado)

# Imprime el valor más grande
print("El resultado más grande es:", resultado[0][indice_maximo])

# Imprime el array correspondiente al valor más grande
print("El array donde se encontró el valor más grande es:", numpy.argmax(resultado))

#--------------------------------------------------------------------------------------------------------------------------------------------

print("Hagamos una predicción!")
resultado = model.predict(numpy.array([[0,0,1,1]]))  # Convertir lista a arreglo numpy
print("El resultado es " + str(resultado[0][0]))
print("El resultado es " + str(resultado[0][1]))
print("El resultado es " + str(resultado[0][2]))
print("El resultado es " + str(resultado[0][3]))

# Encuentra el índice del valor más grande en las predicciones
indice_maximo = numpy.argmax(resultado)

# Imprime el valor más grande
print("El resultado más grande es:", resultado[0][indice_maximo])

# Imprime el array correspondiente al valor más grande
print("El array donde se encontró el valor más grande es:", numpy.argmax(resultado))