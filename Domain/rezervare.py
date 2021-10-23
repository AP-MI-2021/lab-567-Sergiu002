def Creaza_Rezervare(ID, nume, clasa, pret, checkin):
    '''
    Aceasta funtie creaza un dictionar de tip rezervare
    :param ID: ID-ul rezervarii- string
    :param nume: Numele rezervarii - string
    :param clasa: Clasa rezervarii (economy, economy plus, business) - string
    :param pret: Pretul rezervarii - float
    :param checkin: Checkin rezervare (Da sau Nu) - string
    :return: Returneaza un dictionar de retine o rezervare
    '''
    return {
        'ID': ID,
        'nume': nume,
        'clasa': clasa,
        'pret': pret,
        'checkin': checkin
    }

def get_ID(rezervare):
    '''
    Aceasta functie da ID-ul unei rezervari
    :param rezervare: un dictionar de tip rezervare
    :return: Returneaza ID-ul unei rezervari - string
    '''
    return rezervare["ID"]
def get_nume(rezervare):
    '''
    Aceasta functie da numele persoanei care a facut rezervarea
    :param rezervare: un dictionar de tip rezervare
    :return: Returneaza numele presoanei care a facut rezervarea
    '''
    return rezervare["nume"]
def get_clasa(rezervare):
    '''
    Aceasta functie da clasa unei rezervari
    :param rezervare: un dictionar de tip rezervare
    :return: Returneaza clasa unei rezervari
    '''
    return rezervare["clasa"]
def get_pret(rezervare):
    '''
    Aceasta functie da pretul unei rezervari
    :param rezervare: un dictionar de tip rezervare
    :return: Returneaza pretul unei rezervari
    '''
    return rezervare["pret"]
def get_checkin(rezervare):
    '''
    Aceasta functie da checkin-ul unei rezervari
    :param rezervare: un dictionar de tip rezervare
    :return: Returneaza checkin-ul unei rezervari
    '''
    return rezervare["checkin"]
def to_string(rezervare):
    '''
    :param rezervare: un dictionare de tip rezervare
    :return:
    '''
    return "ID: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        get_ID(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )