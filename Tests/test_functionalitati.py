from Domain.rezervare import get_clasa, get_pret
from Logic.CRUD import Adauga_Rezervare, get_by_ID
from Logic.functionalitati import Trecerea_Rezervarilor_La_Clasa_Superioara, Ieftinirea_Rezervarilor_Cu_Un_Procentaj, \
    Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa, Ordonare_Descrescator_Pret, Sume_Preturi_Pentru_Fiecare_Nume


def Test_Trecerea_Rezervarilor_La_Clasa_Superioara():
    lista = Adauga_Rezervare("1", "Suciu", "economy plus", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Suciu", "economy", 20, "Nu", lista)
    lista = Trecerea_Rezervarilor_La_Clasa_Superioara("Suciu", lista)
    assert get_clasa(get_by_ID("2", lista)) == "economy plus"
    assert get_clasa(get_by_ID("1", lista)) == "business"
def Test_Ieftinirea_Rezervarilor_Cu_Un_Procentaj():
    lista = Adauga_Rezervare("1", "Suciu", "economy plus", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Suciu", "economy", 20, "Nu", lista)
    lista = Ieftinirea_Rezervarilor_Cu_Un_Procentaj("10%", lista)
    assert get_pret(get_by_ID("1",lista)) == 90
def Test_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa():
    lista = Adauga_Rezervare("1", "Suciu", "economy plus", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Suciu", "economy", 20, "Nu", lista)
    assert Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista) == "maxim_economy: 20, maxim_economy_plus: 100, maxim_business: -1"
def Test_Ordonare_Descrescator_Pret():
    lista = Adauga_Rezervare("1", "Suciu", "economy plus", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Suciu", "economy", 20, "Nu", lista)
    lista = Adauga_Rezervare("3", "Sergiu", "economy plus", 80, "Da", lista)
    lista = Adauga_Rezervare("4", "Suciu", "economy", 10, "Nu", lista)
    lista = [rezervare['pret'] for rezervare in Ordonare_Descrescator_Pret(lista)]
    assert lista == [100, 80, 20, 10]
def Test_Sume_Preturi_Pentru_Fiecare_Nume():
    lista = Adauga_Rezervare("1", "Suciu", "economy plus", 100, "Da", [])
    lista = Adauga_Rezervare("2", "Suciu", "economy", 20, "Nu", lista)
    lista = Adauga_Rezervare("3", "Sergiu", "economy plus", 80, "Da", lista)
    lista = Adauga_Rezervare("4", "Suciu", "economy", 10, "Nu", lista)
    lista_sume = Sume_Preturi_Pentru_Fiecare_Nume(['Suciu', 'Sergiu'], lista)
    assert lista_sume == [130, 80]