import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower().strip()
    res = ""
    for c in cadena:
        if c == 'á' or c == 'ä':
            res += 'a'
        elif c == 'é' or c == 'ë':
            res += 'e'
        elif c == 'í' or c == 'ï':
            res += 'i'
        elif c in 'óö':
            res += 'o'
        elif c in 'úü':
            res += 'u'
        else:
            res += c
    return res


def ocultar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    res = ""
    for letra in palabra_secreta:
        if letra in letras_usadas:
            res += letra
        else:
            res += "_"
    return res


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    res = ""
    if not "_" in palabra_enmascarada:
        return True
    else:
        return False


def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes):
    print(f"Estado: {" ".join(palabra_enmascarada)}")
    print(f"Letras usadas: {letras_usadas}")
    print(f"Intentos restantes: {intentos_restantes}")


def pedir_letra(letras_usadas):
    '''La función pide una letra al jugador, comprueba si es válida.
            Si la se introduce un número, más de una letra u otra letra repetida, debe denegar esa letra.
        Letras usadas: letras que ya se han usado
        '''
    res = ""
    letra = str(input("Introduce una letra:"))
    if letra in letras_usadas:
        print("Esa letra ya la has usado anteriormente")
    elif letra.isdigit():
        print("Debes introducir una letra")
    elif len(letra) >= 2:
        print("Debes introducir una única letra")
    else:
        print(f"Letra introducida: {letra.lower()}")
        res = letra
    return res


def jugar(palabra_secreta):
    print('''Bienvenido al juego ahorcado!
          ''')

    palabra_secreta = normalizar(palabra_secreta)
    if palabra_secreta == "":
        return None
    palabra_enmascarada = ocultar(palabra_secreta)
    numero_intentos = 6
    letras_usadas = ""

    while numero_intentos > 0 and not ha_ganado(palabra_enmascarada):
        mostrar_estado(palabra_enmascarada, letras_usadas, numero_intentos)
        letra = pedir_letra(letras_usadas)
        letra = str(letra)
        letras_usadas += letra
        if letra in palabra_secreta:
            print("✅ ¡Bien!")
            palabra_enmascarada = ocultar(palabra_secreta, letras_usadas)
        else:
            print("❌ La letra no está en la palabra.")
            numero_intentos -= 1

    if ha_ganado(palabra_enmascarada):
        print(f"🎉 ¡Enhorabuena, has ganado!. La palabra era {palabra_secreta}")
    else:
        print(f"😞 Has perdido. La palabra, era: {palabra_secreta}")


