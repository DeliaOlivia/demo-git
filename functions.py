def cleanup(string):
    """Sterge spatiile de la inceput si sfarsit
    Transforma string-ul in formatul prima litera mare, urmatoarele mici
    Returneaza string-ul
    :param string: un string care va fi transformat
    :returns: string-ul fara spatii si cu prima litera mare
    """
    new_string = string.strip()  # elimina spatiile de la inceput si sfarsit
    new_string = new_string.capitalize()
    return new_string


def newf():
    # to do
    pass


def add(first, second):
    """Adds three values
    Parameters:
        first: primul parametru care va fi adunat
        second: al doilea parametru care va fi adunat
    Returns:
        Suma celor doi parametri
    """
    return first + second


print(cleanup(" text de transformat"))
print(cleanup("tesT"))
print(cleanup(" un text "))
print(cleanup(" un text de schimbat in functia cleanup"))
print(cleanup.__doc__)
help(cleanup)
help(add)