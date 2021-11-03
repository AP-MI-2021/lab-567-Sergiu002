from Logic.CRUD import Adauga_Rezervare
from Tests.test_All import Run_All
from UI.command_line_console import Run_MENU
from UI.console import Run_Menu, UI_Lista_de_rezervari

def Meniu():
    print("\033[36m1. Interfata veche")
    print("\033[36m2. Interfata noua")
    print("\033[35mx. Iesire")

def main():
    lista = UI_Lista_de_rezervari()
    Run_All()
    while True:
        Meniu()
        optiune = input("\033[36mAlegeti interfata: ")
        if optiune == '1':
            Run_Menu(lista)
        elif optiune == '2':
            Run_MENU(lista)
        elif optiune == 'x':
            break
        else:
            print("\033[31mAti introdus o optiune inexistenta!!!")
if __name__ == '__main__':
    main()