import random

def elige_palabra():
     palabras = 'programación, algoritmo, variable, función, cadena, número, bucle, condición, entrada, salida, fácil, difícil, murciélago, pingüino, aéreo, camión, corazón, ratón, árbol, canción, fútbol, matemáticas, lógica, recursión, ahorcado, universidad, python, teclado, pantalla, profesor, estudiante'
     random(palabras)

elige_palabra()

def normalizar():
    elige_palabra().lower()
    elige_palabra().strip()
    elige_palabra().unidecode()

normalizar()


