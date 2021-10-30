from domain.prajitura import get_cookie_string, getNewCookie, get_in_menu_since, get_calories, get_price, \
    get_description, get_name
from logic.crud import create, read, update, delete
from logic.ordonare import ordonare_prajituri
from logic.reducere import reduce_pret_pentru_str


def handle_add(prajituri):
    try:
        id_prajitura = int(input('Dati id-ul prajiturii: '))
        nume = input('Dati numele prajiturii: ')
        descriere = input('Dati descrierea prajiturii: ')
        pret = float(input('Dati pretul prajiturii: '))
        calorii = int(input('Dati caloriile prajiturii: '))
        an_introducere = int(input('Dati anul introducerii prajiturii: '))
        return create(prajituri, id_prajitura, nume, descriere, pret, calorii, an_introducere)
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri


def handle_show_all(prajituri):
    for prajitura in prajituri:
        print(get_cookie_string(prajitura))


def handle_show_details(prajituri):
    id_prajitura = int(input('Dati id-ul prajiturii pentru care doriti detalii: '))
    prajitura = read(prajituri, id_prajitura)
    print(f'Nume: {get_name(prajitura)}')
    print(f'Descriere: {get_description(prajitura)}')
    print(f'Pret: {get_price(prajitura)}')
    print(f'Calorii: {get_calories(prajitura)}')
    print(f'An introducere: {get_in_menu_since(prajitura)}')


def handle_update(prajituri):
    try:
        id_prajitura = int(input('Dati id-ul prajiturii care se actualizeaza: '))
        nume = input('Dati noul nume al prajiturii: ')
        descriere = input('Dati noua descriere prajiturii: ')
        pret = float(input('Dati noul pret al prajiturii: '))
        calorii = int(input('Dati noile calorii ale prajiturii: '))
        an_introducere = int(input('Dati noul an al introducerii prajiturii: '))
        return update(prajituri, getNewCookie(id_prajitura, nume, descriere, pret, calorii, an_introducere))
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri


def handle_delete(prajituri):
    try:
        id_prajitura = int(input('Dati id-ul prajiturii care se va sterge: '))
        prajituri = delete(prajituri, id_prajitura)
        print('Stergerea a fost efectuata cu succes.')
        return prajituri
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri


def handle_crud(prajituri):
    print('1. Adaugare')
    print('2. Modificare')
    print('3. Stergere')
    print('a. Afisare')
    print('d. Detalii prajitura')
    # print('b. Revenire')

    optiune = input('Optiunea aleasa: ')
    if optiune == '1':
        prajituri = handle_add(prajituri)
    elif optiune == '2':
        prajituri = handle_update(prajituri)
    elif optiune == '3':
        prajituri = handle_delete(prajituri)
    elif optiune == 'a':
        handle_show_all(prajituri)
    elif optiune == 'd':
        handle_show_details(prajituri)
    # elif optiune == 'b':
    #     break
    else:
        print('Optiune invalida.')
    return prajituri


def handle_reducere(prajituri):
    try:
        sir_caractere = input("Dati sirul de caractere cautat in nume: ")
        procentaj_reducere = int(input("Dati un procentaj de reducere(0-100):"))

        prajituri = reduce_pret_pentru_str(prajituri, sir_caractere, procentaj_reducere)

        print("Pretul prajiturilor a fost redus cu success")
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri


def handle_ordonare(prajituri):
    try:
        prajituri = ordonare_prajituri(prajituri)
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri


def show_menu():
    print('1. CRUD')
    print('2. Reducere pret pentru anumite prajituri.')
    print('3. Ordonoarea prajiturilor dupa raportul pret / calorii.')
    print('z. Undo.')
    print('y. Redo.')
    # print('4. Prajiturile cu numar maxim de calorii din fiecare an.')
    print('x. Exit')


def handle_new_list(list_versions, current_version, prajituri):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(prajituri)
    current_version += 1
    return list_versions, current_version


def handle_undo(list_versions, current_version):
    if current_version < 1:
        print("Nu se mai poate face undo.")
        return
    current_version -= 1
    return list_versions[current_version], current_version


def handle_redo(list_versions, current_version):
    if current_version == len(list_versions) - 1:
        print("Nu se mai poate face redo.")
        return
    current_version += 1
    return list_versions[current_version], current_version


def run_ui(prajituri):

    list_versions = [prajituri]
    current_version = 0

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            prajituri = handle_crud(prajituri)
            list_versions, current_version = handle_new_list(list_versions, current_version, prajituri)
        elif optiune == '2':
            prajituri = handle_reducere(prajituri)
            list_versions, current_version = handle_new_list(list_versions, current_version, prajituri)
        elif optiune == '3':
            prajituri = handle_ordonare(prajituri)
            list_versions, current_version = handle_new_list(list_versions, current_version, prajituri)
        elif optiune == 'z':
            prajituri, current_version = handle_undo(list_versions, current_version)
        elif optiune == 'y':
            prajituri, current_version = handle_redo(list_versions, current_version)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return prajituri