from Domain.rezervare import to_string
from Logic.CRUD import Adauga_Rezervare, Sterge_Rezervare, Modifica_Rezervare, get_by_ID, get_by_Nume
from Logic.functionalitati import Trecerea_Rezervarilor_La_Clasa_Superioara, Ieftinirea_Rezervarilor_Cu_Un_Procentaj, \
    Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa, Ordonare_Descrescator_Pret, Sume_Preturi_Pentru_Fiecare_Nume, \
    Adaugare_In_Lista_Nume, Lista_de_lista, Functia_Undo, Reducere_Len_Lista_de_Lista


def Print_Menu():
    print("\033[36m1. Adaugare Rezervare")
    print("2. Stergere Rezervare")
    print("3. Modificare Rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit")
    print("6. Determinarea prețului maxim pentru fiecare clasă")
    print("7. Ordonarea rezervărilor descrescător după preț")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume")
    print("9. Undo")
    print("\033[32ma. Afisare rezervari facute")
    print("\033[35mx. Iesire")

def UI_Sterge_Rezervare(lista):
    try:
        ID = input("\033[36mDati ID-ul rezervarii pe care doriti sa o stergeti: ")
        if get_by_ID(ID, lista) is None:
            raise ValueError("\033[31mId-ul nu exista!")
        else:
            return Sterge_Rezervare(ID, lista)
    except ValueError as ve:
        print("\033[31mEroare: {}".format(ve))
        return lista


def UI_Modifica_Rezervare(lista):
    try:
        ID = input("\033[36mDati ID-ul rezervarii pe care doriti sa o modificati: ")
        nume = input("\033[36mDati un nume nou: ")
        while True:
            clasa = input("\033[36mDati o clasa noua(economy, economy plus, business): ")
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("\033[31mNu ati introdus o clasa existenta!!!")
            else:
                break
        while True:
            try:
                pret = float(input("\033[36mDati un pret nou: "))
            except ValueError as ve:
                print("\033[31mEroare: {}".format(ve))
            else:
                print("\033[32mSucces")
                break
        while True:
            checkin = input("\033[36mDati checkin nou(Da sau Nu): ")
            if checkin != "Da" and checkin != "Nu":
                print("\033[31mIntroduceti Da sau Nu")
            else:
                break
        return Modifica_Rezervare(ID, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("\033[31mEroare: {}".format(ve))
        return lista

def UI_Adauga_Rezervare(lista):
    try:
        ID = input("\033[36mDati un ID: ")
        nume = input("\033[36mDati un nume: ")
        while True:
            clasa = input("\033[36mDati o clasa (economy, economy plus, business): ")
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("\033[31mNu ati introdus o clasa existenta!!!")
            else:
                break
        while True:
            try:
                pret = float(input("\033[36mDati un pret: "))
            except ValueError as ve:
                print("\033[31mEroare : {}".format(ve))
            else:
                print("\033[32mSucces")
                break
        while True:
            checkin = input("\033[36mDati checkin (Da sau Nu): ")
            if checkin != "Da" and checkin != "Nu":
                print("\033[31mIntroduceti Da sau Nu")
            else:
                break
        return Adauga_Rezervare(ID, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("\033[31mEroare: {}".format(ve))
        return lista

def Show_All(lista):
    for rezervare in lista:
        print(to_string(rezervare))

def UI_Trecerea_Rezervarilor_La_Clasa_Superioara(lista):
    try:
        nume = input("\033[36mDati un nume: ")
        if get_by_Nume(nume, lista) is None:
            raise ValueError("\033[31mNumele dat nu exista in lista!")
        else:
            return Trecerea_Rezervarilor_La_Clasa_Superioara(nume, lista)
    except ValueError as ve:
        print("\033[31mEroare: {}".format(ve))
        return lista

def UI_Ieftinirea_Rezervarilor_Cu_Un_Procentaj(lista):
    procent = input("\033[36mDati un procent de forma \033[32m'ab%': ")
    ok = True
    if procent[len(procent) - 1] != "%":
        print("\033[31mNu ati introdus un procentaj corect")
        while procent[len(procent) - 1] != "%":
            procent = input("\033[36mDati un procent de forma \033[32m'ab%': ")
            if procent[len(procent) - 1] != "%":
                print("\033[31mNu ati introdus un procentaj corect")
    return Ieftinirea_Rezervarilor_Cu_Un_Procentaj(procent, lista)

def UI_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista):
    print(Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista))

def UI_Ordonare_Descrescator_Pret(lista):
    return Ordonare_Descrescator_Pret(lista)

def UI_Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista):
    lista_sume = Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista)
    for nume in range(len(lista_nume)):
        print("\033[32mSuma preturilor pentru numele " + "\033[35m" + lista_nume[nume] + " \033[32meste " + "\033[35m" + str(lista_sume[nume]))

def UI_Lista_de_rezervari():
    lista = []
    lista = Adauga_Rezervare("1", "Anglia", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Anglia", "economy", 20.0, "Da", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = Adauga_Rezervare("6", "China", "economy", 50.0, "Da", lista)
    lista = Adauga_Rezervare("7", "Germania", "business", 200.0, "Da", lista)
    lista = Adauga_Rezervare("8", "Germania", "economy", 57.0, "Nu", lista)
    lista = Adauga_Rezervare("9", "Germania", "economy", 57.0, "Da", lista)
    lista = Adauga_Rezervare("10", "Austria", "business", 120.0, "Nu", lista)
    lista = Adauga_Rezervare("11", "Romania", "economy plus", 76.0, "Nu", lista)
    lista = Adauga_Rezervare("12", "Franta", "economy plus", 123.7, "Nu", lista)
    lista = Adauga_Rezervare("13", "Franta", "business", 199.9, "Da", lista)
    lista = Adauga_Rezervare("14", "Franta", "economy", 83.0, "Nu", lista)
    lista = Adauga_Rezervare("15", "Cehia", "economy", 50.0, "Nu", lista)
    lista = Adauga_Rezervare("16", "Belgia", "economy", 150.7, "Da", lista)
    lista = Adauga_Rezervare("17", "Romania", "economy plus", 76.0, "Da", lista)
    lista = Adauga_Rezervare("18", "Bulgaria", "business", 91.23, "Nu", lista)
    lista = Adauga_Rezervare("19", "Ungaria", "economy plus", 91.35, "Nu", lista)
    lista = Adauga_Rezervare("20", "Austria", "business", 120.0, "Da", lista)
    return lista

def Run_Menu(lista):
    Lista_lista = []
    Lista_lista = Lista_de_lista(Lista_lista, lista)
    while True:
        Print_Menu()
        lista_nume = []
        lista_nume = Adaugare_In_Lista_Nume(lista_nume, lista)
        Optiune = input("\033[36mDati optiunea: ")
        if Optiune == "1":
            lista = UI_Adauga_Rezervare(lista)
            Lista_lista.append(lista)
        elif Optiune == "2":
            lista = UI_Sterge_Rezervare(lista)
            Lista_lista.append(lista)
        elif Optiune == "3":
            lista = UI_Modifica_Rezervare(lista)
            Lista_lista.append(lista)
        elif Optiune == "4":
            lista = UI_Trecerea_Rezervarilor_La_Clasa_Superioara(lista)
            Lista_lista.append(lista)
        elif Optiune == "5":
            lista = UI_Ieftinirea_Rezervarilor_Cu_Un_Procentaj(lista)
            Lista_lista.append(lista)
        elif Optiune == "6":
            UI_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista)
        elif Optiune == "7":
            lista = UI_Ordonare_Descrescator_Pret(lista)
            Lista_lista.append(lista)
        elif Optiune == "8":
            UI_Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista)
        elif Optiune == "9":
            if len(Lista_lista) > 1:
                lista = Functia_Undo(Lista_lista)
                Lista_lista = Reducere_Len_Lista_de_Lista(Lista_lista)
            else:
                print("\033[31mNu mai puteti face Undo")
        elif Optiune == "a":
            Show_All(lista)
        elif Optiune == "x":
            break
        else:
            print("\033[31mOptiunea dumneavoastra nu este corecta")
