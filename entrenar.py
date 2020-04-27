import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator #para preprocesar las imagenes
from tensorflow.python.keras import optimizers                             #para entrenar algoritmo
from tensorflow.python.keras.models import Sequential                      #para hacer rn secuenciales
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation # 
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D     #capas para convoluciones y maxpoolin
from tensorflow.python.keras import backend as K                           #para eliminar otra sesion de keras corriendo y hacer un entremiento nuevo.

K.clear_session()

data_entrenamiento="./data/entrenamiento"
data_validacion="./data/validacion"

##Parametros
epocas = 20
altura, longitud = 100, 100     #cambiamos la longitud de las imagenes a 100*100 pixeles.
batch_size = 32                 #no. imagenes a procesar en cada paso
pasos = 1000                    #no. veces a procesar la info por epoca
pasos_validacion = 200          #luego de cada epoca. Se corren 200 pasos para validar y verificar el aprendizaje
filtrosConv1=32                 #no. filtro/kernel en cada convolucion
filtrosConv2=64                 #no. filtro/kernel en la segunda convolucion
tamano_filtro1=(3,3)    
tamano_filtro2=(2,2)
tamano_pool=(2,2)
clases=6                        #las carpetas
lr=0.0005                       #learning rate

##pre procesamiento de imagenes
entrenamiento_datagen= ImageDataGenerator(
    rescale=1. / 255,              #rescala a cada pixel con un rango de 1 a 255. a 0-1
    shear_range=0.3,             #genera imagenes inclinadas para aprender a reconocer que puede estar inclinado
    zoom_range=0.3,              #a algunas imagenes les hara zoom
    horizontal_flip=True         #invierte las imagenes
)

validacion_datagen=ImageDataGenerator(
    rescale=1. / 255
)

imagen_entrenamiento= entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,                     #entra al directorio 
    target_size=(altura, longitud),         #procesa las carpetas segun altura y longitu
    batch_size=batch_size,                  # indica el batch size
    class_mode='categorical'                #
)

imagen_validacion = validacion_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)

##Crear la red convolucional
cnn = Sequential()

cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding='same',  input_shape=(altura, longitud, 3), activation='relu'))
#la primer capa es de convolucion, según los filtro y su tamaño. padding que va a hacer
#el filtro en las esquinas. Las imagenes de entrada tienen cierta dimension, y la funcion de activacion es relu

cnn.add(MaxPooling2D(pool_size=tamano_pool))
#luego de la capa anterior, se agrega una capa de pooling, con el tamaño indicado

cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding ='same'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Flatten())
#la imagen con varias dimensiones se vuelve plana

cnn.add(Dense(256, activation='relu'))
#añade una capa normal, con 256 neurones y la misma funcion de activacion

cnn.add(Dropout(0.5))
#a la capa normal, durante el entrenamiento se le desconectan aleatoriamente un 50%
#de las neuronas para que aprenda varios caminos para clasificar la data

cnn.add(Dense(clases, activation='softmax'))
#agrega las salidas que buscamos. Softmax nos devuelve los porcentajes del entrenamiento

cnn.compile(loss='categorical_crossentropy', optimizer=optimizers.Adam(lr=lr), metrics=['accuracy'])
#el optimizador se llama Adam
#la metrica es accuracy

cnn.fit_generator(imagen_entrenamiento, steps_per_epoch=pasos, epochs=epocas, validation_data=imagen_validacion, validation_steps=pasos_validacion)
# se entra la red con las imagenes preprocesadas
#cada epoca tendra pasos
#tendremos el numero de epocas
#se envian las imagenes de validacion
#luego de cada epoca se define cuantas validaciones dara

dir='./modelo/'

if not os.path.exists(dir):
    os.mkdir(dir)
cnn.save('./modelo/modelo.h5')
cnn.save_weights('./modelo/pesos.h5')

