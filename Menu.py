def menu(ManejadorE,ManejadorF):
    print('1 - Leer un estilo y una edad y listar apellido, nombre y DNI de cada patinador que participó en el estilo dado.')
    print('2 - Mostrar apellido y nombre del patinador, estilo y club al que representa el patinador que obtuvo el mayor puntaje en la evaluación.')
    print('3 - Listar los datos de los patinadores que participaron en estilo libre y en escuela.')
    print('4 - Dado el DNI de un inscripto y un estilo, mostrar las 3 valoraciones dadas por los jueces.')
    print('0 - Salir')
    op = int(input('Ingrese la opcion a buscar:'))
    while op != 0:
        if op == 1:
            ManejadorE.Aa(ManejadorF)
            print('\n')
        elif op == 2:
            ManejadorE.Ab(ManejadorF)
            print('\n')
        elif op == 3:
            ManejadorE.Ac(ManejadorF)
            print('\n')
        elif op == 4:
            ManejadorE.Ad()
        else:
            print('Opcion incorrecta')
            op = int(input('Ingrese la opcion a buscar:'))
        print('1 - Leer un estilo y una edad y listar apellido, nombre y DNI de cada patinador que participó en el estilo dado.')
        print('2 - Mostrar apellido y nombre del patinador, estilo y club al que representa el patinador que obtuvo el mayor puntaje en la evaluación.')
        print('3 - Listar los datos de los patinadores que participaron en estilo libre y en escuela.')
        print('4 - Dado el DNI de un inscripto y un estilo, mostrar las 3 valoraciones dadas por los jueces.')
        print('0 - Salir')
        op = int(input('Ingrese la opcion a buscar:'))
    print('Fin del programa')