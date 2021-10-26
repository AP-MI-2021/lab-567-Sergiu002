from Logic.CRUD import Adauga_Rezervare
from Tests.test_All import Run_All
from UI.console import Run_Menu, UI_Lista_de_rezervari


def main():
    lista = UI_Lista_de_rezervari()
    Run_All()
    Run_Menu(lista)
if __name__ == '__main__':
    main()