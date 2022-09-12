import random

print("""
Welcome to Minesweeper!!!
-------------------------


""")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y","z"]
coloane = []
randuri = []
nr_mine = 0
harta = {}

input_coloane = int(input("Cate coloane? __"))
input_randuri = int(input("Cate randuri? __"))
input_bombe = int(input("Cate bombe? __"))

coloane += alphabet[:input_coloane]

for i in range(input_randuri):
    randuri += [i + 1]

nr_mine = input_bombe

def first_row():
    first_row = "  "
    for coloana in coloane:
        first_row += " {coloana} |".format(coloana=coloana)
    print(first_row)

first_row()

def print_randuri():
    nr_coloane = ""
    for coloana in coloane:
        nr_coloane += "   |"
    for num in randuri:
        rand_nou = " " + str(num) + nr_coloane
        print(rand_nou)
        harta[num] = ["" for i in coloane]


print_randuri()

def plaseaza_bombele():
    poz_rand = [key for key in harta]
    poz_coloana = [numb for numb in range(len(coloane))]
    pozitii_tabel = []
    for poz in poz_rand:
        for col in poz_coloana:
            pozitii_tabel.append((poz, col))
    selectii_random = []
    while len(selectii_random) < nr_mine:
        selectie_random = random.choice(pozitii_tabel)
        if selectie_random not in selectii_random:
            selectii_random.append(selectie_random)
    for pozitie in selectii_random:
        harta[pozitie[0]][pozitie[1]] = "X"
    return selectii_random

pozitii_bombe = plaseaza_bombele()
print(pozitii_bombe)
print(harta)

def lista_vecini(pozitie):
    lista_vecini = []
    key_pozitie = pozitie[0]
    index_pozitie = pozitie[1]
    try:
        if (key_pozitie-1) in harta.keys():
            lista_vecini.append(harta[key_pozitie-1][index_pozitie-1])
    except IndexError:
        pass
    try:
        if (key_pozitie-1) in harta.keys():
            lista_vecini.append(harta[key_pozitie-1][index_pozitie])
    except IndexError:
        pass
    try:
        if (key_pozitie-1) in harta.keys():
            lista_vecini.append(harta[key_pozitie-1][index_pozitie+1])
    except IndexError:
        pass
    try:
        lista_vecini.append(harta[key_pozitie][index_pozitie-1])
    except IndexError:
        pass
    try:
        lista_vecini.append(harta[key_pozitie][index_pozitie+1])
    except IndexError:
        pass
    try:
        if (key_pozitie+1) in harta.keys():
            lista_vecini.append(harta[key_pozitie+1][index_pozitie-1])
    except IndexError:
        pass
    try:
        if (key_pozitie+1) in harta.keys():
            lista_vecini.append(harta[key_pozitie+1][index_pozitie])
    except IndexError:
        pass
    try:
        if (key_pozitie+1) in harta.keys():
            lista_vecini.append(harta[key_pozitie+1][index_pozitie])
    except IndexError:
        pass
    return lista_vecini

for value in harta.values():
    print(value)
print(lista_vecini((3, 3)))
