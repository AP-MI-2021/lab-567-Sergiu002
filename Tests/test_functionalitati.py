from Domain.rezervare import get_clasa, get_pret
from Logic.CRUD import Adauga_Rezervare, get_by_ID, Sterge_Rezervare
from Logic.functionalitati import Trecerea_Rezervarilor_La_Clasa_Superioara, Ieftinirea_Rezervarilor_Cu_Un_Procentaj, \
    Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa, Ordonare_Descrescator_Pret, Sume_Preturi_Pentru_Fiecare_Nume, \
    Undo, Redo


def Test_Trecerea_Rezervarilor_La_Clasa_Superioara():
    lista = Adauga_Rezervare("1", "Franta", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = Trecerea_Rezervarilor_La_Clasa_Superioara("Franta", lista)

    assert get_clasa(get_by_ID("2", lista)) == "economy plus"
    assert get_clasa(get_by_ID("1", lista)) == "business"

def Test_Trecerea_Rezervarilor_La_Clasa_Superioara_Undo_Redo():
    undo_operations = []
    redo_operations = []
    lista = Adauga_Rezervare("1", "Franta", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista_noua = Trecerea_Rezervarilor_La_Clasa_Superioara("Franta", lista)
    assert get_clasa(get_by_ID("2", lista_noua)) == "economy plus"
    assert get_clasa(get_by_ID("1", lista_noua)) == "business"
    undo_operations.append([lambda: lista, lambda: lista_noua])
    redo_operations.clear()
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert get_clasa(get_by_ID("2", lista)) == "economy"
    assert get_clasa(get_by_ID("1", lista)) == "economy plus"
    if len(redo_operations) > 0:
        lista = Redo(lista, undo_operations, redo_operations)
    assert get_clasa(get_by_ID("2", lista)) == "economy plus"
    assert get_clasa(get_by_ID("1", lista)) == "business"

def Test_Ieftinirea_Rezervarilor_Cu_Un_Procentaj():
    lista = Adauga_Rezervare("1", "Franta", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = Ieftinirea_Rezervarilor_Cu_Un_Procentaj("10%", lista)

    assert get_pret(get_by_ID("1",lista)) == 90

def Test_Ieftinirea_Rezervarilor_Cu_Un_Procentaj_Undo_Redo():
    undo_operations = []
    redo_operations = []
    lista = Adauga_Rezervare("1", "Franta", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista_noua = Ieftinirea_Rezervarilor_Cu_Un_Procentaj("10%", lista)
    assert get_pret(get_by_ID("2", lista_noua)) == 20
    assert get_pret(get_by_ID("1", lista_noua)) == 90
    undo_operations.append([lambda: lista, lambda: lista_noua])
    redo_operations.clear()
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert get_pret(get_by_ID("2", lista)) == 20
    assert get_pret(get_by_ID("1", lista)) == 100
    if len(redo_operations) > 0:
        lista = Redo(lista, undo_operations, redo_operations)
    assert get_pret(get_by_ID("2", lista)) == 20
    assert get_pret(get_by_ID("1", lista)) == 90

def Test_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa():
    lista = Adauga_Rezervare("1", "Rusia", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Rusia", "economy", 20.0, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)

    assert Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista) == "maxim_economy: 30.0, maxim_economy_plus: 100.0, maxim_business: 240.0"

def Test_Ordonare_Descrescator_Pret():
    lista = Adauga_Rezervare("1", "Germaina", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = Adauga_Rezervare("3", "Romania", "economy plus", 80.0, "Da", lista)
    lista = Adauga_Rezervare("4", "Belgia", "economy", 10.0, "Nu", lista)
    lista = [rezervare[3] for rezervare in Ordonare_Descrescator_Pret(lista)]

    assert lista == [100.0, 80.0, 20.0, 10.0]

def Test_Ordonare_Descrescator_Pret_Undo_Redo():
    undo_operations = []
    redo_operations = []
    lista = Adauga_Rezervare("1", "Germaina", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = Adauga_Rezervare("3", "Romania", "economy plus", 80.0, "Da", lista)
    lista = Adauga_Rezervare("4", "Belgia", "economy", 10.0, "Nu", lista)
    lista_noua = [rezervare for rezervare in Ordonare_Descrescator_Pret(lista)]
    lista_preturi = [rezervare[3] for rezervare in lista_noua]
    assert lista_preturi == [100.0, 80.0, 20.0, 10.0]
    undo_operations.append([lambda: lista, lambda: lista_noua])
    redo_operations.clear()
    if len(undo_operations) > 0:
        lista = Undo(lista,undo_operations, redo_operations)
    lista_preturi = [rezervare[3] for rezervare in lista]
    assert lista_preturi == [100.0, 20.0, 80.0, 10.0]
    if len(redo_operations) > 0:
        lista = Redo(lista, undo_operations, redo_operations)
    lista_preturi = [rezervare[3] for rezervare in lista]
    assert lista_preturi == [100.0, 80.0, 20.0, 10.0]

def Test_Sume_Preturi_Pentru_Fiecare_Nume():
    lista = Adauga_Rezervare("1", "Ucraina", "economy plus", 100.0, "Da", [])
    lista = Adauga_Rezervare("2", "Ucraina", "economy", 20.0, "Nu", lista)
    lista = Adauga_Rezervare("3", "Austria", "economy plus", 80.0, "Da", lista)
    lista = Adauga_Rezervare("4", "Ucraina", "economy", 10.0, "Nu", lista)
    lista_sume = Sume_Preturi_Pentru_Fiecare_Nume(['Ucraina', 'Austria'], lista)

    assert lista_sume == [130.0, 80.0]

def Test_Functia_Undo_Si_Redo():
    undo_operations = []
    redo_operations = []
    lista = []
    lista = Adauga_Rezervare("1", "Ucraina", "economy plus", 100.0, "Da", lista)
    undo_operations.append([lambda: Sterge_Rezervare('1', lista), lambda: Adauga_Rezervare("1", "Ucraina", "economy plus", 100.0, "Da", lista)])
    redo_operations.clear()
    lista = Adauga_Rezervare("2", "Ucraina", "economy", 20.0, "Nu", lista)
    undo_operations.append([lambda: Sterge_Rezervare('2', lista), lambda: Adauga_Rezervare("2", "Ucraina", "economy", 20.0, "Nu", lista)])
    redo_operations.clear()
    lista = Adauga_Rezervare("3", "Austria", "economy plus", 80.0, "Da", lista)
    undo_operations.append([lambda: Sterge_Rezervare('3', lista), lambda: Adauga_Rezervare("3", "Austria", "economy plus", 80.0, "Da", lista)])
    redo_operations.clear()
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert lista[1] == ("2", "Ucraina", "economy", 20.0, "Nu")
    assert get_by_ID("3", lista) is None
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_ID("2", lista) is None
    assert get_by_ID("3", lista) is None
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert get_by_ID("1", lista) is None
    assert get_by_ID("2", lista) is None
    assert get_by_ID("3", lista) is None
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert get_by_ID("1", lista) is None
    assert get_by_ID("2", lista) is None
    assert get_by_ID("3", lista) is None
    lista = Adauga_Rezervare("1", "Ucraina", "economy plus", 100.0, "Da", lista)
    undo_operations.append([lambda: Sterge_Rezervare('1', lista), lambda: Adauga_Rezervare("1", "Ucraina", "economy plus", 100.0, "Da", lista)])
    redo_operations.clear()
    lista = Adauga_Rezervare("2", "Ucraina", "economy", 20.0, "Nu", lista)
    undo_operations.append([lambda: Sterge_Rezervare('2', lista), lambda: Adauga_Rezervare("2", "Ucraina", "economy", 20.0, "Nu", lista)])
    redo_operations.clear()
    lista = Adauga_Rezervare("3", "Austria", "economy plus", 80.0, "Da", lista)
    undo_operations.append([lambda: Sterge_Rezervare('3', lista), lambda: Adauga_Rezervare("3", "Austria", "economy plus", 80.0, "Da", lista)])
    redo_operations.clear()
    if len(redo_operations) > 0:
        lista = Redo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert lista[1] == ("2", "Ucraina", "economy", 20.0, "Nu")
    assert lista[2] == ("3", "Austria", "economy plus", 80.0, "Da")
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert lista[1] == ("2", "Ucraina", "economy", 20.0, "Nu")
    assert get_by_ID("3", lista) is None
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_ID("2", lista) is None
    assert get_by_ID("3", lista) is None
    lista = Adauga_Rezervare("4", "Ucraina", "economy", 10.0, "Nu", lista)
    undo_operations.append([lambda: Sterge_Rezervare('4', lista), lambda: Adauga_Rezervare("4", "Ucraina", "economy", 10.0, "Nu", lista)])
    redo_operations.clear()
    if len(redo_operations) > 0:
        lista = Redo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert lista[1] == ("4", "Ucraina", "economy", 10.0, "Nu")
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_ID('4', lista) is None
    if len(undo_operations) > 0:
        lista = Undo(lista, undo_operations, redo_operations)
    assert get_by_ID('1', lista) is None
    assert get_by_ID('4', lista) is None
    if len(redo_operations) > 0:
        lista = Redo(lista, undo_operations, redo_operations)
    if len(redo_operations) > 0:
        lista = Redo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert lista[1] == ("4", "Ucraina", "economy", 10.0, "Nu")
    if len(redo_operations) > 0:
        lista = Redo(lista, undo_operations, redo_operations)
    assert lista[0] == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert lista[1] == ("4", "Ucraina", "economy", 10.0, "Nu")