from Logic.CRUD import Adauga_Rezervare
from Tests.test_All import Run_All
from UI.console import Run_Menu


def main():
    lista = []
    lista = Adauga_Rezervare("1", "Suciu", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Suciu", "economy", 20.0, "Da", lista)
    lista = Adauga_Rezervare("3", "Sergiu", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Sergiu", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "Andrei", "economy plus", 100.0, "Nu", lista)
    lista = Adauga_Rezervare("6", "Andrei", "economy", 50.0, "Da", lista)
    lista = Adauga_Rezervare("7", "Eduard", "business", 200.0, "Nu", lista)
    Run_All()
    Run_Menu(lista)
if __name__ == '__main__':
    main()