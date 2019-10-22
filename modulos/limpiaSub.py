import re


def sacador(lineaSacar):
    patron = r"(.*begin=\")(.+)(\"\send=\")([^\"]+)(.*>)(.+)(<.+)"
    try:
        salida = re.compile(patron).search(lineaSacar)
        captura = [salida.group(2), salida.group(4), salida.group(6)]
    except:
        captura = None

    return captura


def limpiaSub(archivo):
    capturaLimpia = []

    with open(archivo, 'r') as captura:
        for linea in captura:
            lineaprueba = sacador(linea)
            if lineaprueba:
                capturaLimpia.append([lineaprueba[0], lineaprueba[2]])

    for item in capturaLimpia:
        print(item)

limpiaSub("../temp/cap.cosa")
