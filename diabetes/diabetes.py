from keras.models import Sequential
from keras.layers import Dense
import numpy

#Fija las semillas aleatorias para la reproducibilidad
numpy.random.seed(7)

#Carga los datos
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
#divididos en variables de entrada (X) y salida (Y)
X=dataset[:,0:8]
Y=dataset[:,8]

#crea el modelo
model=Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#Compila el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Hasta aqui solo estamos generando el modelo para que aprenda
model.fit(X, Y, epochs=150, batch_size=10) #Tamano del archivo 10 kva

#evalua el modelo
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
