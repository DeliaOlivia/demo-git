def cleanup(string):
    """Sterge spatiile de la inceput si sfarsit
    Transforma string-ul in formatul prima litera mare, urmatoarele mici
    Returneaza string-ul
    """
    new_string = string.strip()
    new_string = new_string.capitalize()
    return new_string


print(cleanup(" text de transformat"))