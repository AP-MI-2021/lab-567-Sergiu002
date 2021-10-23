from Domain.rezervare import Creaza_Rezervare, get_ID, get_nume, get_clasa, get_pret, get_checkin


def Test_Rezervare():
    rezervare = Creaza_Rezervare("1", "Suciu", "economy", 20, "Nu")

    assert get_ID(rezervare) == "1"
    assert get_nume(rezervare) == "Suciu"
    assert get_clasa(rezervare) == "economy"
    assert get_pret(rezervare) == 20
    assert get_checkin(rezervare) == "Nu"