def buscar(lista, elemento):
    """Retorna o indice de elemento se ele estiver na lista ou None, caso contrario"""
   
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

lista_estranha = [8, "5", 32, 0, "py", 11]
elem = input("qual valor vc que saber onde estar: ")

indice = buscar(lista_estranha, elem)
if indice is not None:
    print("o indice do elemento {} é {}".format(elem, indice))
else:
    print("O elemento {} nao se encontra na lista".format(elem))



# pra lista ORDENADA, é mais eficiente fazer uma busca binaria
