def feladat_1(szoveg: str, also, felso):
    return also <= len(szoveg) <= felso


def feladat_2(also, felso):
    szo = input("Kérek egy rendelést 3 és 10 tétel között: ")
    while not feladat_1(szo, also, felso):
        szo = input("Hibás! Kérek egy rendelést 3 és 10 tétel között: ")
    return szo


def feladat_3(hossz):
    lista = []
    for i in range(hossz):
        kisbetu = feladat_2(3, 10).lower()
        lista.append(kisbetu)
    return lista


def feladat_4(lista):
    db = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == "g":
                db += 1
    return print(f"A listában {db} darab 'g'/'G' szerepel.")


def feladat_4_nehez(lista):
    tanyerok = 0
    fajtak = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if fajtak.count(lista[i][j]) == 0:
                fajtak.append(lista[i][j])
                tanyerok += 1

    return print(f"A pincérnek {tanyerok} db tányért kell előkészítenie a rendelés alapján.")
