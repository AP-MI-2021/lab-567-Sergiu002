from Logic.CRUD import Adauga_Rezervare
from Tests.test_All import Run_All
from UI.console import Run_Menu


def main():
    lista = []
    lista = Adauga_Rezervare("1", "Anglia", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Anglia", "economy", 20.0, "Da", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = Adauga_Rezervare("6", "China", "economy", 50.0, "Da", lista)
    lista = Adauga_Rezervare("7", "Germania", "business", 200.0, "Nu", lista)
    Run_All()
    Run_Menu(lista)
if __name__ == '__main__':
    main()