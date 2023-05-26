from ManejadorFederados import ManejaFederados
from ManjadorEvaluaciones import ManejaEvaluaciones
from Menu import menu
if __name__ == '__main__':
    ManejadorF = ManejaFederados()
    ManejadorF.initmf()
    ManejadorF.test()

    print('\n')

    ManejadorE = ManejaEvaluaciones()
    ManejadorE.initme()
    ManejadorE.test()

    print('\n')

    menu(ManejadorE,ManejadorF)
    # ManejadorE.Aa(ManejadorF)
    # print('\n')
    # valor = input('valor:')
    # print('\n')
    # ManejadorE.Ab(ManejadorF)
    # print('\n')
    # valor = input('valor:')
    # print('\n')
    # ManejadorE.Ac(ManejadorF)
    # print('\n')
    # valor = input('valor:')
    # print('\n')
    # ManejadorE.Ad()
