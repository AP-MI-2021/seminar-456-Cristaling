from domain.prajitura import getNewCookie, get_id


def create(lista_prajituri: list, _id: int, _nume: str, _descriere: str, _pret: int, _calorii: int, _in_menu_since: int):
    prajitura = getNewCookie(_id, _nume, _descriere, _pret, _calorii, _in_menu_since)
    # lista_prajituri.append(prajitura)
    # return lista_prajituri
    return lista_prajituri + [prajitura]


def read(lista_prajituri: list, id_prajitura: int=None):
    prajitura_gasita = None

    if id_prajitura is None:
        return lista_prajituri

    for prajitura in lista_prajituri:
        if get_id(prajitura) == id_prajitura:
            prajitura_gasita = prajitura

    return prajitura_gasita


def update(lista_prajituri, new_cookie):
    result = []

    for prajitura in lista_prajituri:
        if get_id(prajitura) == get_id(new_cookie):
            result.append(new_cookie)
        else:
            result.append(prajitura)

    return result


def delete(lista_prajituri, id_prajitura: int):
    result = []

    for prajitura in lista_prajituri:
        if get_id(prajitura) != id_prajitura:
            result.append(prajitura)

    return result

