juegos={
    "G001" : ["eclipse runner", "PC", "accion", "T", True, "NovaStudio"],
    "G002" : ["Puzzle Atlas", "Switch", "Puzzle", "E", False,"BrightWorks"],
    "G003" : ["Sky Legends","PS5", "Aventura", "T", True, "OrionGames"],
    "G004" : ["Racing Pulse", "PC", "carreras", "E", True, "VelocityLab"],
    "G005" : ["Mystic Farm", "Switch", "simulacion", "E", False, "GreenSeed"],
    "G006" : ["Shadow Tactics", "Xbox", "Estrategia", "M", False, "IronGate"],
    
}

inventario={
    "G001" : [9990, 7],
    "G002" : [19990, 0],
    "G003" : [42990, 3],
    "G004" : [14990, 5],
    "G005" : [17990, 9],
    "G006" : [39990, 2],
    
}

def stock_plataforma(plataforma:str, juegos: dict , inventario: dict ):
    codigo_plataforma=plataforma.strip().upper()
    if codigo_plataforma =="":
        return False
    if codigo_plataforma not in inventario:
        return False
    

def busqueda_precio(p_min: int, p_max: int, juegos: dict, inventario: dict):
    for codigo in inventario:
        pass
        
        
def buscar_codigo(codigo: str, inventario: dict):
    for codigo_precio in inventario:
        pass    
        
# return True
def actualizar_precio(codigo: str, nuevo_precio: int, inventario: dict):
    
    
    return True
def agregar_juego(codigo: str, titulo:str , plataforma: str, genero:str , clasificacion: str, multiplayer: str, editor: str, precio: int, stock: int , juegos:dict , inventario:dict):
    validar_codigo=codigo.strip()
    if validar_codigo =="":
        return False
    
    if validar_codigo in inventario:
        return False
    
    
    validar_titulo=titulo.strip()
    if validar_titulo =="":
        return False
    
    validar_plataforma=plataforma.strip()
    if validar_plataforma =="":
        return False
    
    validar_genero=genero.strip()
    if validar_genero =="":
        return False
    
    
    validar_clasificacion=clasificacion
    if validar_clasificacion!= "E, M, T":
        return False
    
    validar_multiplayer=multiplayer.strip()
    s=True
    n=False
    if validar_multiplayer != "s" or "n":
        return False
    
    validar_editor=editor.strip()
    if validar_editor=="":
        return False
    
    validar_precio=precio
    if validar_precio <=0:
        return False
    
    validar_stock=stock
    if validar_stock <0:
        return False
    
    return True


def eliminar_juego(codigo: str, juegos: dict, inventario: dict):
    del codigo[juegos]
    del codigo[inventario]


def mostrar_menu():
    print("----MENÚ PRINCIPAL----")
    print("1. stock por plataforma")
    print("2. busqueda de juegos por rango de precio")
    print("3. actualizar precio de juego")
    print("4. agregar juego")
    print("5. eliminar juego")
    print("6. salir")

opcion=0
while opcion!=6:
    mostrar_menu()
    try:
        opcion=int(input("opcion: "))
    except ValueError:
        opcion=0
        
    if opcion==1:
        plataforma=input("nombre de una plataforma: ")
        if plataforma!=[juegos][1]:
            print("esta plataforma no es parte del sistema.")
        else:
            continue
            
        stock_plataforma(plataforma, juegos, inventario)
        
        
    elif opcion==2:
        try:
            p_min=int(input("ingrese precio minimo: "))
        except ValueError:
            p_min=0
        try:
            p_max=int(input("ingrese preceio maximo:"))
        except ValueError:
            p_max=0
        busqueda_precio(p_min, p_max, juegos, inventario)
        
    elif opcion==3:
        buscar_codigo(codigo, inventario)
    elif opcion==4:
        titulo=input("titulo: ")
        plataforma=input("plataforma: ")
        genero=input("genero: ")
        clasificacion=input("clasificacion: ")
        multiplayer=input("multiplayer: ")
        editor=input("editor: ")
        try:
            precio=int(input("precio: "))
        except ValueError:
            precio=0
            
        try:
            stock=int(input("stock"))
        except ValueError:
            stock=0
        
        
        agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario)
    
    elif opcion==5:
        codigo=input("codigo del juego a eliminar: ")
        eliminar_juego(codigo,juegos,inventario)
        if eliminar_juego:
            print("juego eliminado")
        else:
            print("El codigo no existe")
    elif opcion==6:
        print("Programa Finalizado")
    else:
        print("error en opcion.")