

def getNewCookie(_id: int, _nume: str, _descriere: str, _pret: int, _calorii: int, _in_menu_since: int):
    cookie = {
        'id': _id,
        'nume': _nume,
        'descriere': _descriere,
        'pret': _pret,
        'calorii': _calorii,
        'in_menu_since': _in_menu_since
    }
    return cookie


def get_id(prajitura):
    return prajitura['id']


def get_name(prajitura):
    return prajitura['nume']


def get_description(prajitura):
    return prajitura['descriere']


def get_price(prajitura):
    return prajitura['pret']


def get_calories(prajitura):
    return prajitura['calorii']


def get_in_menu_since(prajitura):
    return prajitura['in_menu_since']


def get_cookie_string(prajitura):
    return f'Prajitura cu id-ul {get_id(prajitura)}, introdusa in anul {get_in_menu_since(prajitura)}, cu numele {get_name(prajitura)}'