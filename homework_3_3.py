def thesaurus(*args):
    names = dict()
    for name in args:
        first_letter = name[0]
        if first_letter not in names:
            names[first_letter] = []
        names[first_letter].append(name)
    return names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))