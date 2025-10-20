print("Hola, todo funciona")
print("___")

print("Bienvenidos a mi tienda")

def colores ():
    color=input("Selecciones el color entre Rojo, azul, verde o negro : ").lower()
    colores=["azul","rojo","verde", "negro"]
    while color not in colores:
        print("Color no disponible")
        color=input("Selecciones el color entre Rojo, azul o verde : ").lower()
    print("Siguiente paso: ")
    return color

def tallas():
    talla=input("Seleccione la talla  entre S, M , L, XL : ").lower()
    tallas=["s","m","l","xl"]
    while talla not in tallas:
        print("Talla no disponible")
        talla=input("Seleccione la talla  entre S, M , L, XL : ").lower()
    return talla
    print("Siguiente paso: ")

def telas ():
    tela=input("Seleccione la tela entre algodon, seda, lana o poliester : ").lower()
    telas=["algodon", "seda","lana", "poliester"]
    while tela not in telas:
        if tela == "algodón" or tela =="poliéster":
            break
        print("Tela no disponible")
        tela=input("Seleccione la tela entre algodon, seda, lana o poliester : ").lower()
    return tela

print(" Resumen de compra: Polo color", colores(), "talla", tallas(), "tela de", telas())
print("Gracias por su compra")

