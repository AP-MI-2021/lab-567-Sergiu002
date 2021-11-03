from Logic.CRUD import Adauga_Rezervare, Sterge_Rezervare, Modifica_Rezervare, get_by_ID
from UI.console import Show_All


def Citeste_In_Linie():
    '''
    Citire lista in linie
    La parametrul "; " gasit se va sparge lista si vor fi create doua liste separate
    La parametrul ", " gasit se va sparge lista, astfel incat lista noastra va fi parcursa cuvant cu cuvant
    :return:
    '''
    lista_mare = []
    lista_mica = []
    print("\033[36mSeparatori de comenzi: '; '")
    print("\033[36mSeparatori de cuvinte: ', '")
    print("\033[35m!Nu uitati sa puneti spatiu dupa fiecare separator!")
    sir = input("\033[36mDati niste comenzi din lista {Adauga, Sterge, Modifica, ShowAll}: ")
    lista = sir.split('; ')
    for index in lista:
        cuvant = index.split(', ')
        lista_mica = []
        for y in range(len(cuvant)):
            lista_mica.append(cuvant[y])
        lista_mare.append(lista_mica)
    return lista_mare
def UI_Adauga_O_Rezervare(lista, lista_mea):
        '''
        Adauga o rezervare in lista noastra
        :param lista: lista de rezervari
        :param lista_mea: lista care contine rezervarea mea curenta care trebuie adaugata in lista de rezervari
        :return:
        '''
        try:
            ID = lista_mea[0]
            nume = lista_mea[1]
            clasa = lista_mea[2]
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("\033[31mNu ati introdus o clasa existenta!!!")
                return lista
            checkin = lista_mea[4]
            if checkin != "Da" and checkin != "Nu":
                print("\033[31mNu ati introdus Da sau Nu")
                return lista
            pret = float(lista_mea[3])
            return Adauga_Rezervare(lista_mea[0], lista_mea[1], lista_mea[2], float(lista_mea[3]), lista_mea[4], lista)
        except IndexError as ve:
            print("\033[31mEroare: {}".format(ve))
            return lista
        except ValueError as ve:
            print("\033[31mEroare: {}".format(ve))
            return lista

def UI_Sterge_O_Rezervare(lista, lista_mea):
        '''
        Sterge o rezervare in lista noastra
        :param lista: lista de rezervari
        :param lista_mea: lista care contine rezervarea mea curenta care trebuie adaugata in lista de rezervari
        :return:
        '''
        try:
            ID = lista_mea[0]
            if get_by_ID(ID, lista) is None:
                print("\033[31mId-ul nu exista!")
                return lista
            else:
                return Sterge_Rezervare(lista_mea[0], lista)
        except IndexError as ve:
            print("\033[31mEroare: {}".format(ve))
            return lista
def UI_Modifica_O_Rezervare(lista, lista_mea):
        '''
        Modifica o rezervare in lista noastra
        :param lista: lista de rezervari
        :param lista_mea: lista care contine rezervarea mea curenta care trebuie adaugata in lista de rezervari
        :return:
        '''
        try:
            ID = lista_mea[0]
            nume = lista_mea[1]
            clasa = lista_mea[2]
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("\033[31mNu ati introdus o clasa existenta!!!")
                return lista
            checkin = lista_mea[4]
            if checkin != "Da" and checkin != "Nu":
                print("\033[31mNu ati introdus Da sau Nu")
                return lista
            pret = float(lista_mea[3])
            return Modifica_Rezervare(lista_mea[0], lista_mea[1], lista_mea[2], float(lista_mea[3]), lista_mea[4],
                                      lista)
        except IndexError as ve:
            print("\033[31mEroare: {}".format(ve))
            return lista
        except ValueError as ve:
            print("\033[31mEroare: {}".format(ve))
            return lista


def Run_MENU(lista_rezervari):
    lista_lista = Citeste_In_Linie()
    lista_comenzi = ["Adauga", "Sterge", "Modifica", "ShowAll"]
    for lista in lista_lista:
         if lista[0] in lista_comenzi:
            if lista[0] == lista_comenzi[0]:
                lista_noua = lista[1:]
                lista_rezervari = UI_Adauga_O_Rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[1]:
                lista_noua = lista[1:]
                lista_rezervari = UI_Sterge_O_Rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[2]:
                lista_noua = lista[1:]
                lista_rezervari = UI_Modifica_O_Rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[3]:
                Show_All(lista_rezervari)
