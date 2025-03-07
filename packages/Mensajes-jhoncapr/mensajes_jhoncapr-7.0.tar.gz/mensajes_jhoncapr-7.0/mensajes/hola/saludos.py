import numpy as np

def saludar():
    print("Hola te saludo desde SALUDOS")
    
def prueba():
    print("Esto es una prueba de la nueva versión.")

def generar_array(numeros): #generara un array llamando a numpy
    return np.arange(numeros)

class Saludo:
    
    def __init__(self):
        print("Hola te saludo desde SALUDOS INIT CLASS")
        
if __name__ == '__main__':
    #saludar()
    print(generar_array(10))