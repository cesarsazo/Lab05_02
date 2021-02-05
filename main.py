from animal import perro, vaca, gato

opcion = 0
animalesList = []

def ver():
    for animal in animalesList:        
        if isinstance(animal, vaca):
            print('Soy una vaca y mi nombre es: ', animal.nombre,' y mi edad es: ', animal.edad)
        elif isinstance(animal, perro):
            print('Soy un perro y mi nombre es: ', animal.nombre,' y mi edad es: ', animal.edad)
        elif isinstance(animal, gato):
            print('Soy un gato y mi nombre es: ', animal.nombre,' y mi edad es: ', animal.edad)

def crear():
    nuevo = None
    nombre = input('Ingrese el nombre del nuevo animal.')
    edad = int(input('Ingrese la edad del nuevo animal.'))
    tipo = int(input('De que tipo desea crear el animal [Perro(1), Vaca(2), Gato(3)]'))
    if tipo == 1:
        nuevo = perro(nombre, edad)
    elif tipo == 2:
        nuevo = vaca(nombre, edad)
    elif tipo == 3:
        nuevo = gato(nombre, edad)
    animalesList.append(nuevo)

while True:
    if opcion == 3:
        break
    elif opcion == 2:
        ver()
    elif opcion == 1:
        crear()
    print('_____________________________')
    print('| 1. Crear animal            |')
    print('| 2. Ver                     |')
    print('| 3. Salir                   |')
    print('_____________________________')
    opcion = int(input('Ingrese alguna opcion [1-3]\n'))