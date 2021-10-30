from domain.prajitura import get_name, get_price, getNewCookie, get_id, get_description, get_calories, get_in_menu_since


def reduce_pret_pentru_str(lista, sir_caractere, procent):

    if not (0 <= procent <= 100):
        raise ValueError("Procentajul dat trebuie sa fie intre 0 si 100")

    if sir_caractere == '':
        raise ValueError("Textul cautat nu paote fi gol")

    result = []
    for prajitura in lista:
        if sir_caractere in get_name(prajitura):
            pret_nou = get_price(prajitura) * (100 - procent) / 100
            result.append(getNewCookie(
                get_id(prajitura),
                get_name(prajitura),
                get_description(prajitura),
                pret_nou,
                get_calories(prajitura),
                get_in_menu_since(prajitura)
            ))
        else:
            result.append(prajitura)

    return result
