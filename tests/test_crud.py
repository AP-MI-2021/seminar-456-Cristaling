from domain.prajitura import getNewCookie, get_id
from logic.crud import create, read, update, delete


def get_data():
    return [
        getNewCookie(1, 'p1', 'desc 1', 100, 50, 2018),
        getNewCookie(2, 'p2', 'desc 2', 60.7, 80.32, 2015),
        getNewCookie(3, 'p3', 'desc 3', 0, 20, 2012),
        getNewCookie(4, 'p4', 'desc 4', 153534, 150, 2017),
        getNewCookie(5, 'p5', 'desc 5', 40.7775, 40.32, 2016),
    ]


def test_create():
    lista = get_data()
    new_cookie = getNewCookie(6, 'p6', 'desc 6', 40.7775, 40.32, 2016)
    lista_noua = create(lista, 6, 'p6', 'desc 6', 40.7775, 40.32, 2016)

    assert len(lista_noua) == len(lista) + 1
    assert new_cookie in lista_noua


def test_read():
    lista = get_data()
    random_cookie = lista[2]
    assert read(lista, get_id(random_cookie)) == random_cookie
    assert read(lista, None) == lista


def test_update():
    lista = get_data()
    new_cookie = getNewCookie(5, 'p6', 'desc 6', 40.7775, 40.32, 2016)
    lista_noua = update(lista, new_cookie)
    assert len(lista) == len(lista_noua)
    assert new_cookie in lista_noua
    assert lista[4] != lista_noua[4]


def test_delete():
    lista = get_data()
    delete_id = 3
    deleted_cookie = read(lista, delete_id)
    lista_noua = delete(lista, delete_id)
    assert len(lista_noua) == len(lista) - 1
    assert deleted_cookie not in lista_noua


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


test_crud()

# a = "abc"
# b = "dfg"
# c = "abc"
#
# lista = [a, b]
# print(lista)
# print(a in lista)
# print(c in lista)