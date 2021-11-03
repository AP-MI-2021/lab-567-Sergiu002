from Domain.rezervare import Creeaza_Rezervare, get_ID


def Adauga_Rezervare(ID, nume, clasa, pret, checkin, lista):
    '''
    Aceasta functie adauga o rezervare noua intr-o lista
    :param ID: ID-ul rezervarii- string
    :param nume: Numele rezervarii - string
    :param clasa: Clasa rezervarii (economy, economy plus, business) - string
    :param pret: Pretul rezervarii - float
    :param checkin: Checkin rezervare (Da sau Nu) - string
    :param lista: Lista rezervarilor
    :return: Returneaza lista veche + rezervarea noua
    '''
    if get_by_ID(ID, lista) is not None:
        raise ValueError("\033[31mId-ul exista deja!")
    rezervare_noua = Creeaza_Rezervare(ID, nume, clasa, pret, checkin)
    return lista + [rezervare_noua]
def get_by_Nume(nume, lista):
    '''
    Cauta daca exista o rezerare cu numele "nume" in lista de rezervari
    :param nume: Numele rezervarii pe care o cautam
    :param lista: Lista rezervarilor
    :return: Returneaza rezervarea daca aceasta a fost gasita in lista sau None in caz contrar
    '''
    for rezervare in lista:
        if rezervare[1] == nume:
            return rezervare
    return None
def get_by_ID(ID, lista):
    '''
    Cauta daca exista o rezervare cu ID-ul "ID" in lista de rezervari
    :param ID: ID-ul rezervarii pe care o cautam - string
    :param lista: Lista rezervarilor
    :return: Returneaza rezervarea daca rezervarea cu ID-ul "ID" a fost gasita in lista, respectiv None in caz contrar
    '''
    for rezervare in lista:
        if rezervare[0] == ID:
            return rezervare
    return None

def Sterge_Rezervare(ID, lista):
    '''
    Sterge o rezervare din lista dupa ID
    :param ID: ID-ul rezervarii pe care dorim sa o stergem
    :param lista: Lista rezervarilor
    :return: Returneaza o lista noua in care rezervarea cu ID-ul "ID" nu mai exista
    '''
    return [rezervare for rezervare in lista if get_ID(rezervare) != ID]
def Modifica_Rezervare(ID, nume, clasa, pret, checkin, lista):
    '''
    Modifica o rezervare din lista dupa ID
    :param ID: ID-ul rezervarii- string
    :param nume: Numele nou al rezervarii - string
    :param clasa: Clasa noua a rezervarii (economy, economy plus, business) - string
    :param pret: Pretul nou al rezervarii - float
    :param checkin: Checkin-ul nou al rezervarii (Da sau Nu) - string
    :return:
    '''
    lista_noua = []
    for rezervare in lista:
        if get_ID(rezervare) == ID:
            rezervare_noua = Creeaza_Rezervare(ID, nume, clasa, pret, checkin)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua