import random

harta = {}
harta_activa = {}

class Box:
    def __init__(self, rand = 0, coloana = 0, vecini = [], tipul = ""):
        self.rand = rand
        self.coloana = coloana
        self.vecini = vecini
        self.tipul = tipul

    def __repr__(self):
        return "Rand: {rand}, Coloana: {coloana}, Tipul: {tipul}".format(rand = self.rand, coloana = self.coloana, tipul = self.tipul)

class Joc:
    numar_joc = 0
    lista_pozitii_bombe = []
    count_choice = 0

    def __init__(self, numar_coloane, numar_randuri, numar_bombe, denumire_jucator):
        self.numar_coloane = numar_coloane
        self.numar_randuri = numar_randuri
        self.numar_bombe = numar_bombe
        Joc.numar_joc += 1
        self.numar_joc = Joc.numar_joc
        self.scor = 0
        self.denumire_jucator = denumire_jucator

    def __repr__(self):
        return "Numar coloane: {numar_coloane}\nNumar randuri: {numar_randuri}\nNumar bombe: {numar_bombe}\nNumar joc: {numar_joc}\nScor: {scor}\nJucator: {denumire_jucator}".format(numar_coloane = self.numar_coloane, numar_randuri = self.numar_randuri, numar_bombe = self.numar_bombe, numar_joc = self.numar_joc, scor = self.scor, denumire_jucator = self.denumire_jucator)

    def generare_harta(self):
        for i in range(1, self.numar_randuri + 1):
            harta[i] = [Box(i, coloana + 1) for coloana in range(self.numar_coloane)]

    def generare_harta_activa(self):
        for i in range(1, self.numar_randuri + 1):
            harta_activa[i] = [Box(i, coloana + 1) for coloana in range(self.numar_coloane)]

    def distribuire_bombe(self):
        all_boxes = harta.values()
        selectii_random = []
        all_boxes = list(harta.values())
        all_boxes_list = []
        for lista in all_boxes:
            for box in lista:
                all_boxes_list.append(box)
        while len(selectii_random) < self.numar_bombe:
            selectie_random = random.choice(all_boxes_list)
            if selectie_random not in selectii_random:
                selectii_random.append(selectie_random)
        for selectie in selectii_random:
            harta[selectie.rand][selectie.coloana-1].tipul = "X"
    
    def vezi_harta(self):
        first_row = "   "
        for coloana in range(1, self.numar_coloane + 1):
            first_row += " {coloana} |".format(coloana=coloana)
        print(first_row)
        nr_coloane = ""
        for num in range(1, self.numar_randuri + 1):
            rand_nou = ""
            rand_nou += " {rand} ".format(rand = num)
            for coloana in range(1, self.numar_coloane + 1):
                rand_nou += " {} |".format(harta[num][coloana-1])
            if num > 9:
                rand_nou = rand_nou[:3] + rand_nou[4:]
            print(rand_nou)

    def vezi_harta_activa(self):
        first_row = "   "
        for coloana in range(1, self.numar_coloane + 1):
            first_row += " {coloana} |".format(coloana=coloana)
        print(first_row)
        nr_coloane = ""
        for num in range(1, self.numar_randuri + 1):
            rand_nou = ""
            rand_nou += " {rand} ".format(rand = num)
            for coloana in range(1, self.numar_coloane + 1):
                rand_nou += " {} |".format(harta_activa[num][coloana-1])
            if num > 9:
                rand_nou = rand_nou[:3] + rand_nou[4:]
            print(rand_nou)

    def verifica_vecini(self, randul=0, coloana=0):
        randul = int(input("Introduceti randul: "))
        coloana = int(input("Introduceti coloana: ")) - 1
        lista_vecini = []
        if harta[randul][coloana] == "X":
            joc_1.vezi_harta()
            return print("GAME OVER"), exit()
        else:
            try:
                lista_vecini.append(harta[randul-1][coloana-1])
            except (IndexError, KeyError):
                pass
            try:
                lista_vecini.append(harta[randul-1][coloana])
            except (IndexError, KeyError):
                pass
            try:
                lista_vecini.append(harta[randul-1][coloana+1])
            except (IndexError, KeyError):
                pass
            try:
                lista_vecini.append(harta[randul][coloana-1])
            except (IndexError, KeyError):
                pass
            try:
                lista_vecini.append(harta[randul][coloana+1])
            except (IndexError, KeyError):
                pass
            try:
                lista_vecini.append(harta[randul+1][coloana-1])
            except (IndexError, KeyError):
                pass
            try:
                lista_vecini.append(harta[randul+1][coloana])
            except (IndexError, KeyError):
                pass
            try:
                lista_vecini.append(harta[randul+1][coloana+1])
            except (IndexError, KeyError):
                pass
        return (lista_vecini, randul, coloana)

    def selectie(self, randul=0, coloana=0):
        lista_vecini, randul, coloana = self.verifica_vecini()
        if lista_vecini.count("X") == 0:
            harta[randul][coloana] = "O"
            harta_activa[randul][coloana] = "O"
            Joc.count_choice += 1

        else:
            harta[randul][coloana] = lista_vecini.count("X")
            harta_activa[randul][coloana] = lista_vecini.count("X")
            Joc.count_choice += 1
        print(lista_vecini)

def start_joc():
    nr_randuri = len(harta.keys())
    nr_coloane = len(harta[1])
    while Joc.count_choice < nr_randuri * nr_coloane:
        joc_1.selectie()
        joc_1.vezi_harta_activa()

joc_1 = Joc(10, 10, 30, "Mihai")

print(joc_1)
joc_1.generare_harta()
# joc_1.generare_harta_activa()
joc_1.distribuire_bombe()
print(harta)
# #joc_1.vezi_harta_activa()
# print(harta_activa)
# joc_1.vezi_harta_activa()
# start_joc()
