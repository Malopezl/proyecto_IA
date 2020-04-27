import numpy as np
#from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

longitud, altura =100,100
modelo ='./modelo/modelo.h5'
pesos = './modelo/pesos.h5'

cnn=load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
    x=load_img(file, target_size=(longitud, altura))
    x=img_to_array(x)
    x=np.expand_dims(x, axis=0)
    arreglo=cnn.predict(x)  ## para las clases definidas, devolvera un arreglo como este [[1, 0, 0, 0, 0, 0]] 
    resultado = arreglo[0]
    #print(resultado)
    respuesta=np.argmax(resultado)

    if respuesta==0:
        print("-------------------------------------------------------------")
        print("FASE 1:")
        print("PROPAGACION DE PLANDULAS")
        print("Edad: 2-3 semanas de vida")
        print("Tiempo de cosecha: 13-14 semanas aprox.")
        print("INFO: la propagacion de plnadulas consiste en el desarrollo")
        print("inicial de la planta, desde la germinación hasta obtener las")
        print("primeras ramas principales.")
        print("-------------------------------------------------------------")
    elif respuesta==1:
         print("-------------------------------------------------------------")
         print("FASE 2:")
         print("DESARROLLO DE RAICES")
         print("Edad: 4-6 semanas de vida")
         print("Tiempo de cosecha: 10-12 semanas aprox.")
         print("INFO: Se recomienda transplantar a area mas grande para que")
         print("la planta pueda enraizar correctamente.")
         print("-------------------------------------------------------------")
    elif respuesta==2:
         print("-------------------------------------------------------------")
         print("FASE 6:")
         print("COSECHA")
         print("Edad: 16- semanas de vida")
         print("Tiempo de cosecha: AHORA")
         print("INFO: Coseche según sea su necesidad, Para obtener un sabor")
         print("unico espere hasta que este completamente rojo.")
         print("-------------------------------------------------------------")
    elif respuesta==3: 
         print("-------------------------------------------------------------")
         print("FASE 3:")
         print("MADURACION O DE CRECIMIENTO")
         print("Edad: 7-11 semanas de vida")
         print("Tiempo de cosecha: 5-11 semanas aprox.")
         print("INFO: Produre agregar un soporte para que la planta crezca ")
         print("correctamente. Se recomienda abonar a cada 10-15 dias para ")
         print("que la planta crezca correctamente.")
         print("-------------------------------------------------------------")
    elif respuesta==4:
         print("-------------------------------------------------------------")
         print("FASE 4:")
         print("FLORACION")
         print("Edad: 12-13 semanas de vida")
         print("Tiempo de cosecha: 3-4 semanas aprox.")
         print("INFO: Las flores amarillas son los puntos en donde creceran")
         print("los frutos. Los primeros brotarán en la parte baja de la planta.")
         print("-------------------------------------------------------------")
    elif respuesta==5:
         print("-------------------------------------------------------------")
         print("FASE 5:")
         print("PRODUCCION")
         print("Edad: 14-15 semanas de vida")
         print("Tiempo de cosecha: 1-2 semanas aprox.")
         print("INFO: La planta ha iniciado a desarrollar sus frutos.")
         print("Debe esperar a que crezcan y muestren un color rojizo-anaranjado.")
         print("-------------------------------------------------------------")
    return respuesta
