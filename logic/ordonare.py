from domain.prajitura import get_calories, get_price, get_id


def raport_pret_calorii(prajitura):
    return get_price(prajitura) / get_calories(prajitura)


def ordonare_prajituri(lista):
    return sorted(lista, key=raport_pret_calorii)