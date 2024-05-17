from keras.models import Sequential
from keras.layers import Dense
import numpy

# Fija las semillas aleatorias para la reproducibilidad
numpy.random.seed(7)

# Carga los datos
dataset = numpy.loadtxt("Videojuego/videojuego.csv", delimiter=",")
# Divididos en variables de entrada (X) y salida (Y)
X = dataset[:,0:4]
Y = dataset[:,4]

# Imprime las entradas y salidas para verificar
print("Entradas:")
print(X)
print("Salidas:")
print(Y)

# Crea el modelo
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='softmax'))

# Compila el modelo
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Hasta aquí solo estamos generando el modelo para que aprenda
model.fit(X, Y, epochs=120, batch_size=10)

# Evalúa el modelo
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

def prediccion(model, entrada, salida_real):
    resultado = model.predict(numpy.array([entrada]))  # Convertir lista a arreglo numpy

    # Imprime el array correspondiente al valor más grande
    print("La predicción es:", numpy.argmax(resultado))

    # Actualiza el modelo con la nueva entrada y salida
    model.fit(numpy.array([entrada]), numpy.array([salida_real]), epochs=1, verbose=0)

array1 = [4, 0, 1, 2]
array2 = [0, 1, 1, 3]
array3 = [1, 1, 1, 2]
array4 = [1, 0, 1, 2]
array5 = [0, 0, 1, 1]

# Realiza las predicciones y actualiza el modelo después de cada una
prediccion(model, array1, 0)  # Aquí asumí que el valor de salida real es 1, cámbialo según tus datos
prediccion(model, array2, 1)
prediccion(model, array3, 2)
prediccion(model, array4, 3)
prediccion(model, array5, 1)
