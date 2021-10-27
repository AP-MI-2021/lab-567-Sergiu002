from Domain.rezervare import get_nume, Creeaza_Rezervare, get_clasa, get_ID, get_pret, get_checkin


def Trecerea_Rezervarilor_La_Clasa_Superioara(nume, lista):
    '''
    Trece clasa rezervarile cu numele "nume" la o clasa superioara
    :param nume: Numele rezervarilor pentru care trebuie modificata clasa la o clasa superioara
    :param lista: Lista rezervarilor
    :return: Lista rezervarilor modificata
    '''
    lista_noua = []
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == "economy":
                rezervare_noua = Creeaza_Rezervare(
                    get_ID(rezervare),
                    get_nume(rezervare),
                    "economy plus",
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                lista_noua.append(rezervare_noua)
            elif get_clasa(rezervare) == "economy plus":
                rezervare_noua = Creeaza_Rezervare(
                    get_ID(rezervare),
                    get_nume(rezervare),
                    "business",
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                lista_noua.append(rezervare_noua)
            elif get_clasa(rezervare) == "business":
                rezervare_noua = Creeaza_Rezervare(
                    get_ID(rezervare),
                    get_nume(rezervare),
                    get_clasa(rezervare),
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                lista_noua.append(rezervare_noua)
        else:
             lista_noua.append(rezervare)
    return lista_noua
def Ieftinirea_Rezervarilor_Cu_Un_Procentaj(procent, lista):
    '''
    Rezervarile care au facut checkin-ul vor fi ieftinite cu un procentaj dat "procent"
    :param procent: procentul cu care vor fi ieftinite preturile rezervarilor - string
    :param lista: Lista rezervarilor
    :return: Lista rezervarilor modificata
    '''
    procentaj = procent[0: len(procent) - 1]
    numar = float(procentaj)
    lista_noua = []
    for rezervare in lista:
        if get_checkin(rezervare) == "Da":
            rezervare_noua = Creeaza_Rezervare(
                get_ID(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                get_pret(rezervare) - numar / 100 * get_pret(rezervare),
                get_checkin(rezervare)
            )
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua
def Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista):
    '''
    Determina pretul maxim pentru fiecare clasa
    :param lista:Lista rezervarilor
    :return: Returneaza preturie maxime pentru fiecare clasa
    '''
    maxim_economy = -1
    maxim_economy_plus = -1
    maxim_business = -1
    for rezervare in lista:
        if get_clasa(rezervare) == "economy":
            if get_pret(rezervare) > maxim_economy:
                maxim_economy = get_pret(rezervare)
        elif get_clasa(rezervare) == "economy plus":
            if get_pret(rezervare) > maxim_economy_plus:
                maxim_economy_plus = get_pret(rezervare)
        elif get_clasa(rezervare) == "business":
            if get_pret(rezervare) > maxim_business:
                maxim_business = get_pret(rezervare)
    return "maxim_economy: {}, maxim_economy_plus: {}, maxim_business: {}".format(
        maxim_economy,
        maxim_economy_plus,
        maxim_business
    )
def Ordonare_Descrescator_Pret(lista):
    '''
    Ordoneaza lista descrescator dupa pretul rezervarilor
    :param lista: Lista rezervarilor
    :return: Lista ordonata descrescator dupa pretul rezervarilor
    '''
    lista_noua = sorted(lista, key = lambda i: i[3], reverse = True)
    return lista_noua
def Adaugare_In_Lista_Nume(lista_nume, lista):
    '''
    Introduce intr-o lista noua numele din lista veche. Acestea vor aparea doar o singura data
    :param lista_nume: lista numelor rezervarilor din lista "lista"
    :param lista: Lista rezervarilor
    :return:
    '''
    for rezervare in lista:
        if get_nume(rezervare) not in lista_nume:
            lista_nume.append(get_nume(rezervare))
    return lista_nume
def Suma_Preturi_Pentru_Un_Nume(Nume, lista):
    '''
    Aceasta functie face suma preturilor unei rezervari cu numele "Nume"
    :param Nume: Numele rezervarii pentru care trebuie facuta suma - string
    :param lista: Lista rezervarilor
    :return: Returneaza suma preturilor rezervarilor cu numele "Nume"
    '''
    suma = 0
    for rezervare in lista:
        if get_nume(rezervare) == Nume:
            suma = suma + get_pret(rezervare)
    return suma
def Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista):
    '''
    Aceasta functie returneaza sumele prețurilor pentru fiecare nume
    :param lista_nume: Lista numelor din lista rezervarilor
    :param lista: Lista rezervarilor
    :return: Returneaza sumele prețurilor pentru fiecare nume
    '''
    lista_sume = []
    for rezervare_nume in lista_nume:
        lista_sume.append(Suma_Preturi_Pentru_Un_Nume(rezervare_nume, lista))
    return lista_sume

def Lista_de_lista(Lista_lista, lista):
    '''
    Creeaza o lista de liste
    :param Lista_lista: O lista care este plina cu liste de dictionare
    :param lista: Lista rezervarilor
    :return: Returneaza lista de liste creata
    '''
    Lista_lista.append(lista)
    return Lista_lista

def Copiere_Lista_Fara_Ultimul_Parametru(Lista_lista):
    '''
    Sterge ultima lista de dictionare din lista de lista de dictionare
    :param Lista_lista: O lista care este plina cu liste de dictionare
    :return: Returneaza o lista de liste de dictionare fara ultima lista de dictionare
    '''
    Lista_lista_noua = []
    for l in range(0, len(Lista_lista) - 1):
        Lista_lista_noua.append(Lista_lista[l])
    return Lista_lista_noua

def Functia_Undo(Lista_lista):
    '''
    Atribuie unei liste ultima lista din lista de lista de dictionare
    :param Lista_lista: O lista care este plina cu liste de dictionare
    :return: Returneaza Ultima lista de dictionare din lista de lista
    '''
    Lista_lista_noua = Copiere_Lista_Fara_Ultimul_Parametru(Lista_lista)
    lista = Lista_lista_noua[-1]
    return lista

def Reducere_Len_Lista_de_Lista(Lista_lista):
    '''
    Reduce lungimea listei de liste
    :param Lista_lista: O lista care este plina cu liste de dictionare
    :return: Returneaza lista de liste de dictionare cu lungimea scazuta cu o unitate
    '''
    return Copiere_Lista_Fara_Ultimul_Parametru(Lista_lista)