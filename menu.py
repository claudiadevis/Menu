menu_T = {
    "Aperitivo: Guacamole": ["cilantro", "cebolla","chile","ajo","tomate","aguacate","zumo de limón","sal"],
    "Primer plato: Pimientos del piquillo rellenos" : ["huevo","palitos de cangrejo","atún en aceite de oliva","mayonesa","pimientos del piquillo","pimiento verde","pimiento rojo","cebolla","vinagre de vino","sal","aceite de oliva"],
    "Segundo plato: Solomillo de cerdo agridulce" : ["aceite de oliva","ajo","solomillo de cerdo","cebolla","manzana","tomate concentrado","calabacines","brandy","vino de Oporto","ciruelas pasas sin hueso","orejones de albaricoque","mostaza","piñones tostados"],
    "Postre: Brownie de chocolate con helado de turrón": ["chocolate amargo","mantequilla sin sal","azúcar","huevos","sal","harina de trigo","nueces"],
}

def lista_de_compras(menu):
    """
    Devuelve la lista de compras de un menú que es un diccionario
    """
    lista = []
    for plato in menu:
        #print(plato)
        for ingredientes in menu[plato]:
            #print(ingredientes)
            if ingredientes not in lista:
                lista.append(ingredientes)
    return lista

print(lista_de_compras(menu_T))

