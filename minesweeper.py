from itertools import count
import random

harta = {}
harta_activa = {}

class Box:
    def __init__(self, rand = 0, coloana = 0, vecini = [], tipul = " "):
        self.rand = rand
        self.coloana = coloana
        self.vecini = vecini
        self.tipul = tipul

    def __repr__(self):
        return "Rand: {rand}, Coloana: {coloana}, Tipul: {tipul}, Vecini: {vecini}".format(rand = self.rand, coloana = self.coloana, tipul = self.tipul, vecini = self.vecini)

    def determina_tipul_box_selectat(self):
        self.determina_vecini()
        if self.tipul == "X":
            pass
        else:
            self.tipul = self.count_bombs()

    def count_bombs(self):
        counter_bombs = 0
        for vecin in self.vecini:
            if vecin.tipul == "X":
                counter_bombs += 1
        return counter_bombs

    def determina_vecini(self):
        if self.rand == 1 and self.coloana == 1:
            self.vecini += [harta[1][1], harta[2][0], harta[2][1]]
        if self.rand == 1 and self.coloana == joc_1.numar_coloane:
            self.vecini += [harta[1][self.coloana-2], harta[2][self.coloana-2], harta[2][self.coloana-1]]



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
                rand_nou += " {} |".format(harta[num][coloana-1].tipul)
            if num > 9:
                rand_nou = rand_nou[:3] + rand_nou[4:]
            print(rand_nou)

    def vezi_harta_activa(self):
        pass

    def selectie(self):
        input_rand = int(input("Introduceti randul: "))
        input_coloana = int(input("Introduceti coloana: ")) - 1
        box_selectat = harta[input_rand][input_coloana]

    def populeaza_harta(self):
        all_boxes = list(harta.values())
        all_boxes_list = []
        for lista in all_boxes:
            for box in lista:
                all_boxes_list.append(box)
        for box in all_boxes_list:
            box.rand += 1
            print(box)
        print(all_boxes_list)

joc_1 = Joc(3, 3, 3, "Mihai")
print(joc_1)
joc_1.generare_harta()
# joc_1.generare_harta_activa()
joc_1.distribuire_bombe()
# print(harta)

joc_1.vezi_harta()
joc_1.populeaza_harta()
