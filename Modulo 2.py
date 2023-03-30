print("Bienvenidos a nuestro programa para las carreras de la temporada 2023 de la Fórmula 1")
print("             ¡Esperamos que sea una experiencia agradable para ti!                   ")

listaEntradas = []

def seleccionInput():
    seleccion = ''
    while seleccion != '1' and seleccion != '2' and seleccion != '3' and seleccion != '4':
        seleccion = input('')
        if seleccion != '1' and seleccion != '2' and seleccion != '3' and seleccion != '4':
            print('Opcion no valida, introduzca el numero asociado a su opcion')
    return seleccion

def respuestaInput():
    respuesta = ''
    while respuesta != 'S' and respuesta != 'N':
        respuesta = input('''Desea proseguir con la compra?
        Si (S)
        No (N)''')

        if respuesta != 'S' and respuesta != 'N':
            print('Opcion no valida, por favor, solo ingrese la letra S o N dependiendo de la opcion que quiera')
    return respuesta

def nameInput():
    name = ''
    while len(name) == 0:
        name = input("Por favor, introduzca su nombre: \n")
        if len(name) == 0:
            print('Error, nombre no introducido, por favor intente de nuevo')
    return name

def cedulaInput():
    cedula = ''
    while len(cedula) == 0 or not cedula.isdigit():
        cedula = input("Por favor, introduzca su cedula: \n")
        if len(cedula) == 0 or not cedula.isdigit():
            print('Error, cedula invalida, por favor intente de nuevo')    
    return cedula

def es_ondulante(cadena):
    last=""
    for i in cadena:
        if i==last:
            return False
        last=i
    return True
 
valores=["123456", "1223", "11223", "23344"]
for cedula in valores:
    if es_ondulante(cedula):
        print("{} es ondulante".format(cedula))
    else:
        print("{} NO es ondulante".format(cedula))

def edadInput():
    edad = ''
    while len(edad) == 0 or not edad.isdigit():
        edad = input("Por favor, introduzca su edad: \n")
        if len(edad) == 0 or not edad.isdigit():
            print('Error, edad invalida, por favor intente de nuevo')
    return edad

def correoInput():
    correo = ''
    correoConCaracteresBan = True
    while len(correo) == 0 or len(correo) > 50 or correo.count('@') != 1 or correoConCaracteresBan:
        correo = input("Por favor, introduzca su correo: \n")
        # Se asume que el correo es valido
        correoConCaracteresBan = False
        # se recorre todo el correo para verificar si lo asumido es correcto
        for letra in correo:
            if not letra.isalnum() and (letra != '@') and (letra != '.') and (letra != '_'):
                correoConCaracteresBan = True

        if len(correo) == 0 or len(correo) > 50 or correoConCaracteresBan:
            print('Error, correo invalida, por favor intente de nuevo')
    return correo

def entradaInput():
    entrada = ''
    while entrada != 'V' and entrada != 'N':
        entrada = input('''Seleccione el tipo de entrada, estas tienen un IVA de 16%
        Entrada Normal (N)
        Entrada VIP (V)
        ''')
        if entrada != 'V' and entrada != 'N':
            print('Opcion no valida, por favor, solo ingrese la letra V o N dependiendo de la opcion que quiera')
    return entrada

def personasInput():
    personas = ''
    while (not personas.isnumeric()) or int(personas) <= 0:
        personas = input('¿Cuantas entradas desea comprar?')
        if (not personas.isnumeric()) or int(personas) <= 0:
            print('Cantidad invalida, por favor introduzca un entero')
    return personas

def sacarTotal(entrada,personas):
    total = 0
    subtotal = 0
    descuento = False
    if entrada == 'N':
        total =  personas * 150 + 100 * 0.16
    else:
        total = personas * 340 + 100 * 0.16
        # El + 100 * 0.16 es el IVA incrementado de 16%

    subtotal = total
    if personas % 2 != 0:
        # la cantidad de personas es impar
        total = total - (total * 0.50)
        descuento = True
    return total,descuento,subtotal


def comprarEntrada():
    name = nameInput()
    cedula = cedulaInput()
    correo = correoInput()
    edad = edadInput()
    entrada = entradaInput()
    personas = int(personasInput())
    total,descuento,subTotal = sacarTotal(entrada,personas)
    textoDescuento = ''
    if entrada == "V":
        nroRon = personas * 2
        print('Con las entradas vip vienen ${} tragos de Ron'.format(nroRon))
    if descuento: 
        textoDescuento = 'Si (50%)'
    else: 
        textoDescuento = 'No'
        
    print("""
    ---------- RECIBO ----------
    Nombre: {}
    Cedula: {}
    Correo: {}
    Edad: {}
    Numero de Entradas: {}
    subTotal: {}
    Descuento: {}
    Total: {}
    """.format(name,cedula,correo,edad,personas,subTotal,textoDescuento,total))
    respuesta = respuestaInput()
    if respuesta == "N":
        print('Cancelando Compra')
    else:
        comprador = {
            'name': name,
            'cedula': cedula,
            'correo':correo,
            'edad' : edad,
            'total':total,
            'descuento':descuento,
            'NroDeEntradas':personas,
            'tipoDeEntrada': entrada,
        }
        listaEntradas.append(comprador)
        print(comprador)

def totalEntradasVendidas():
    cantGenerales = 0 
    cantVIP = 0
    for comprador in listaEntradas:
        if comprador["tipoDeEntrada"] == 'V':
            cantVIP += 1
        else:
            cantGenerales +=1
    print('''
    Compradores de Entradas VIP : {}
    Compradores de Entradas Generales: {}
    '''.format(cantVIP,cantGenerales))
    return

def clientesConDescuento():
    clientesConDescuento = 0
    for comprador in listaEntradas:
        if comprador['descuento']:
            clientesConDescuento += 1
    
    print('''
    Clientes con descuento: {}
    '''.format(clientesConDescuento))
    return


def main():
    running = True
    while running:
        print('''
        
        ¿Qué desea realizar?
        1. Comprar entradas (1)
        2. Ver cantida de compradores por entrada (2)
        3. Ver cantidad de clientes con descuento (3)
        4. Salir del sistema (4)
        ''')
        seleccion = seleccionInput()

        if seleccion == '1':
            comprarEntrada()
        elif seleccion == '2':
            totalEntradasVendidas()
        elif seleccion == '3':
            clientesConDescuento()
        else:
            print('Hasta Luego, disfrute las carreras!!')
            running = False



main()
