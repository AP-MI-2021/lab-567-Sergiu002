from Domain.rezervare import to_string
from Logic.CRUD import Adauga_Rezervare, Sterge_Rezervare, Modifica_Rezervare
from Logic.functionalitati import Trecerea_Rezervarilor_La_Clasa_Superioara, Ieftinirea_Rezervarilor_Cu_Un_Procentaj, \
    Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa, Ordonare_Descrescator_Pret, Sume_Preturi_Pentru_Fiecare_Nume, \
    Adaugare_In_Lista_Nume


def Print_Menu():
    print("1. Adaugare Rezervare")
    print("2. Stergere Rezervare")
    print("3. Modificare Rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit")
    print("6. Determinarea prețului maxim pentru fiecare clasă")
    print("7. Ordonarea rezervărilor descrescător după preț")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume")
    print("a. Afisare rezervari facute")
    print("x. Iesire")
def UI_Sterge_Rezervare(lista):
    ID = input("Dati ID-ul rezervarii pe care doriti sa o stergeti: ")
    return Sterge_Rezervare(ID, lista)
def UI_Modifica_Rezervare(lista):
    ID = input("Dati ID-ul rezervarii pe care doriti sa o modificati: ")
    nume = input("Dati un nume nou: ")
    while True:
        clasa = input("Dati o clasa noua(economy, economy plus, business): ")
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Nu ati introdus o clasa existenta!!!")
        else:
            break
    while True:
        try:
            pret = float(input("Dati un pret nou: "))
        except ValueError:
            print("Eroare")
        else:
            print("Succes")
            break
    while True:
        checkin = input("Dati checkin nou(Da sau Nu): ")
        if checkin != "Da" and checkin != "Nu":
            print("Introduceti Da sau Nu")
        else:
            break
    return Modifica_Rezervare(ID, nume, clasa, pret, checkin, lista)
def UI_Adauga_Rezervare(lista):
    ID = input("Dati un ID: ")
    nume = input("Dati un nume: ")

    while True:
        clasa = input("Dati o clasa (economy, economy plus, business): ")
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Nu ati introdus o clasa existenta!!!")
        else:
            break
    while True:
        try:
            pret = float(input("Dati un pret: "))
        except ValueError:
            print("Eroare")
        else:
            print("Succes")
            break
    while True:
        checkin = input("Dati checkin (Da sau Nu): ")
        if checkin != "Da" and checkin != "Nu":
            print("Introduceti Da sau Nu")
        else:
            break
    return Adauga_Rezervare(ID, nume, clasa, pret, checkin, lista)
def Show_All(lista):
    for rezervare in lista:
        print(to_string(rezervare))
def UI_Trecerea_Rezervarilor_La_Clasa_Superioara(lista):
    nume = input("Dati un nume: ")
    return Trecerea_Rezervarilor_La_Clasa_Superioara(nume, lista)
def UI_Ieftinirea_Rezervarilor_Cu_Un_Procentaj(lista):
    procent = input("Dati un procent de forma 'ab%': ")
    ok = True
    if procent[len(procent) - 1] != "%":
        print("Nu ati introdus un procentaj corect")
        while procent[len(procent) - 1] != "%":
            procent = input("Dati un procent de forma 'ab%': ")
            if procent[len(procent) - 1] != "%":
                print("Nu ati introdus un procentaj corect")
    return Ieftinirea_Rezervarilor_Cu_Un_Procentaj(procent, lista)
def UI_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista):
    print(Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista))
def UI_Ordonare_Descrescator_Pret(lista):
    return Ordonare_Descrescator_Pret(lista)
def UI_Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista):
    lista_sume = Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista)
    for nume in range(len(lista_nume)):
        print(lista_nume[nume] + ' ' + str(lista_sume[nume]))
def Run_Menu(lista):
    while True:
        Print_Menu()
        lista_nume = []
        lista_nume = Adaugare_In_Lista_Nume(lista_nume, lista)
        Optiune = input("Dati optiunea: ")
        if Optiune == "1":
            lista = UI_Adauga_Rezervare(lista)
        elif Optiune == "2":
            lista = UI_Sterge_Rezervare(lista)
        elif Optiune == "3":
            lista = UI_Modifica_Rezervare(lista)
        elif Optiune == "4":
            lista = UI_Trecerea_Rezervarilor_La_Clasa_Superioara(lista)
        elif Optiune == "5":
            lista = UI_Ieftinirea_Rezervarilor_Cu_Un_Procentaj(lista)
        elif Optiune == "6":
            UI_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista)
        elif Optiune == "7":
            lista = UI_Ordonare_Descrescator_Pret(lista)
        elif Optiune == "8":
            UI_Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista)
        elif Optiune == "a":
            Show_All(lista)
        elif Optiune == "x":
            break
        else:
            print("Optiunea dumneavoastra nu este corecta")
