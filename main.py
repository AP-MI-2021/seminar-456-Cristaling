
# Scrieți un program pentru gestionarea unei cofetării. Vor fi suportate operațiile:
#
# Adăugare / ștergere / modificare prăjitură (CRUD): se efectuează pe bază de ID. O prăjitură are: ID, nume, descriere (nenule), preț, calorii, anul introducerii în meniu.
# Reducerea pretului pentru toate prăjiturile care conțin în nume un string dat.
# Afișarea tuturor prăjiturilor introduse începând cu un an dat.
# Determinarea prăjiturii cu cel mai mare număr de calorii din fiecare an al introducerii.
# Ordonarea prăjiturilor crescător după raportul preț / calorii.
# Afișarea sumelor prețurilor pentru fiecare an al introducerii.
# Undo + redo.
# Se va lucra pe 3 iterații, similar cu Lab 5-7, cu cerințe noi în fiecare săptămână. Se va folosi aceeași organizare pe fișiere cu cea cerută în cadrul Lab 5-7.
#
# Nu vor fi abordate subiectele bonus în mod direct, acestea necesitând studiu individual. Puteți cere însă feedback cadrelor didactice de la seminar.

from logic.crud import create
from tests.test_crud import test_crud
from user_interface.console import run_ui


# lista = create(lista, 1, "Prajitura1", "Prima prajitura", 10, 1000, 2020)
# lista = create(lista, 2, "Prajitura2", "A doua prajitura", 12, 1100, 2021)
# prajitura1 = read(lista, 1)
#
# newCookie = getNewCookie(1, "Prajitura 1 noua", "Prima prajitura updated", 10, 1000, 2020)
# lista = update(lista, newCookie)
#
# prajitura1 = read(lista, 1)
# print(prajitura1)
#
# lista = delete(lista, 1)
# prajitura1 = read(lista, 1)
# print(prajitura1)

def main():
    prajituri = []
    prajituri = create(prajituri, 1, 'ecler', 'gustos, foarte', 10, 500, 2013)
    prajituri = create(prajituri, 2, 'amandina', 'foarte dulce', 12, 600, 2020)
    prajituri = create(prajituri, 3, 'inghetata ciocolata', 'prea mult zahar', 17, 700, 2013)
    prajituri = create(prajituri, 4, 'tort', 'pentru mai multe persoane', 60, 2500, 2015)
    prajituri = create(prajituri, 5, 'inghetata vanilie', 'fara ciocolata :(', 21, 300, 2020)
    prajituri = create(prajituri, 6, 'cheese cake', 'nu imi place', 14, 700, 2020)
    prajituri = create(prajituri, 7, 'brownie', 'de mai multe feluri', 23, 300, 2013)
    prajituri = run_ui(prajituri)

if __name__ == '__main__':
    test_crud()
    main()
