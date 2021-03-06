from Tests.test_CRUD import Test_Adauga_Rezervare, Test_Sterge_Rezervare, Test_Modifica_Rezervare, Test_get_by_ID, \
    Test_get_by_Nume
from Tests.test_Domain import Test_Rezervare
from Tests.test_functionalitati import Test_Trecerea_Rezervarilor_La_Clasa_Superioara, \
    Test_Ieftinirea_Rezervarilor_Cu_Un_Procentaj, Test_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa, \
    Test_Ordonare_Descrescator_Pret, Test_Sume_Preturi_Pentru_Fiecare_Nume, Test_Functia_Undo_Si_Redo, \
    Test_Trecerea_Rezervarilor_La_Clasa_Superioara_Undo_Redo, Test_Ieftinirea_Rezervarilor_Cu_Un_Procentaj_Undo_Redo, \
    Test_Ordonare_Descrescator_Pret_Undo_Redo


def Run_All():
    '''
    In aceasta functie se introduc toate testele
    :return:
    '''
    Test_get_by_Nume()
    Test_get_by_ID()
    Test_Rezervare()
    Test_Adauga_Rezervare()
    Test_Sterge_Rezervare()
    Test_Modifica_Rezervare()
    Test_Trecerea_Rezervarilor_La_Clasa_Superioara()
    Test_Ieftinirea_Rezervarilor_Cu_Un_Procentaj()
    Test_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa()
    Test_Ordonare_Descrescator_Pret()
    Test_Sume_Preturi_Pentru_Fiecare_Nume()
    Test_Functia_Undo_Si_Redo()
    Test_Trecerea_Rezervarilor_La_Clasa_Superioara_Undo_Redo()
    Test_Ieftinirea_Rezervarilor_Cu_Un_Procentaj_Undo_Redo()
    Test_Ordonare_Descrescator_Pret_Undo_Redo()