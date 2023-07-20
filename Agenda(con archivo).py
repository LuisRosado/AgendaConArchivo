import os
import pathlib

SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3

def MostrarMenu():
    os.system('cls')
    print(f'''               Agenda\n
{AGREGAR})Agregar Contactos
{MOSTRAR})Mostrar todos los Contactos
{BUSCAR})Buscar un Contacto
{SALIR})Salir\n''')

def CargarArchivo(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contacto, telefono, email ,categoria = linea.strip().split(',')
                agenda.setdefault(contacto, (telefono, email, categoria))
    else:
        with open(nombre_archivo,'w') as archivo:
            pass

def AgregarContacto(agenda, nombre_archivo):
    os.system('cls')
    print('                        Agregar Contacto')
    nombre = input('Nombre: ')
    if agenda.get(nombre):
        print('\nEse Contacto Ya Existe')
    else:
        telefono = input('Telefono: ')
        email = input('Email: ')
        categoria = input('Categoria: ')
        agenda.setdefault(nombre, (telefono, email, categoria))
        with open(nombre_archivo,'a') as archivo:
            archivo.write(f'{nombre},{telefono},{email},{categoria}\n')
        print('\nSe ha agregado a tu lista de contactos con exito.')

def MostrarContactos(agenda):
    os.system('cls')
    print('                        Mostar Contactos')
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print(f'Categoria: {datos[2]}')
            print('-'*50)
    else:
        print('\nNo tienes ningun Contacto.')

def BuscarContacto(agenda):
    os.system('cls')
    print('                        Buscar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'\nNombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'Email: {datos[1]}')
                print(f'Categoria: {datos[2]}')
                print('-'*50)
                encontrados += 1
        if encontrados == 0:
            print('\nContacto No Encontrado.')
        else:
            print(f'\nSe encontraron {encontrados} contactos')
    else:
        print('\nNo hay Contactos Registrados.')

def main():
    continuar = True
    Agenda = dict()
    nombre_archivo = 'agenda.txt'
    CargarArchivo(Agenda, nombre_archivo)
    while continuar:
        MostrarMenu()
        opc = int(input('Seleccione una opcion: '))

        if opc == AGREGAR:
            AgregarContacto(Agenda, nombre_archivo)
        elif opc ==MOSTRAR:
            MostrarContactos(Agenda)
        elif opc == BUSCAR:
            BuscarContacto(Agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion no valida...')
        input('Presiona enter para continuar')

if __name__ == '__main__':
    main()
