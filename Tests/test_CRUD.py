from Domain.rezervare import get_ID, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import Adauga_Rezervare, get_by_ID, Sterge_Rezervare, Modifica_Rezervare, get_by_Nume


def Test_get_by_ID():
    lista = Adauga_Rezervare("1", "Anglia", "business", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Germania", "economy", 20, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    
    assert get_by_ID('1', lista) == lista[0]
    assert get_by_ID('6', lista) is None


def Test_get_by_Nume():
    lista = Adauga_Rezervare("1", "Anglia", "business", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Germania", "economy", 20, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)

    assert get_by_Nume('Anglia', lista) == lista[0]
    assert get_by_Nume('6', lista) is None

def Test_Adauga_Rezervare():
    lista = Adauga_Rezervare("1", "Anglia", "business", 100, "Da", [])

    assert len(lista) == 1
    assert get_ID(get_by_ID("1", lista)) == "1"
    assert get_nume(get_by_ID("1", lista)) == "Anglia"
    assert get_clasa(get_by_ID("1", lista)) == "business"
    assert get_pret(get_by_ID("1", lista)) == 100
    assert get_checkin(get_by_ID("1", lista)) == "Da"

def Test_Sterge_Rezervare():
    lista = Adauga_Rezervare("1", "Anglia", "business", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Germania", "economy", 20, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = Sterge_Rezervare("1", lista)

    assert len(lista) == 4
    assert get_by_ID('1', lista) is None
    assert get_by_ID('2', lista) is not None

def Test_Modifica_Rezervare():
    lista = Adauga_Rezervare("1", "Anglia", "business", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Germania", "economy", 20, "Nu", lista)
    lista = Adauga_Rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = Adauga_Rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = Adauga_Rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = Modifica_Rezervare("2", "Franta", "economy plus", 20, "Nu", lista)

    assert get_ID(get_by_ID("2", lista)) == "2"
    assert get_nume(get_by_ID("2", lista)) == "Franta"
    assert get_clasa(get_by_ID("2", lista)) == "economy plus"
    assert get_pret(get_by_ID("2", lista)) == 20
    assert get_checkin(get_by_ID("2", lista)) == "Nu"