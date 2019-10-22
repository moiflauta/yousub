profundidad = 0


def imprime_cosas(cosa):

    def imprime_lista(lista):
        global profundidad

        profundidad = + 1
        #    print("_____________")
        for item in lista:
            imprime_cosas(item)

    def imprime_diccionario(diccionario):
        global profundidad
        profundidad = + 1

        print("___________________")

        for item in diccionario.keys():
            print("\t" * profundidad, item, ":")

            imprime_cosas(diccionario[item])

    if ("list" in str(type(cosa))) or ("set" in str(type(cosa))):
        print("_____________")

        imprime_lista(cosa)
    elif  "dict" in str(type(cosa)):
        imprime_diccionario(cosa)

    else: print("\t"*profundidad, cosa)




#imprime_cosas([{31:["23","12"]}, {45:[1,2,[3,4,5,[6,8]]]}])