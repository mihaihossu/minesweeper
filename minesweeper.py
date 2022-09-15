
import random

harta = {}
harta_activa = {}

class Box:
    def __init__(self, rand = 0, coloana = 0, vecini = None, tipul = " "):
        self.rand = rand
        self.coloana = coloana
        self.vecini = [] if vecini is None else vecini
        self.tipul = tipul

    def __repr__(self):
        return "Rand: {rand}, Coloana: {coloana}, Tipul: {tipul}, Vecini: {vecini}".format(rand = self.rand, coloana = self.coloana, tipul = self.tipul, vecini = self.vecini)

    def determina_tipul_box_selectat(self):
        if self.tipul == "X":
            pass
        else:
            self.determina_vecinii()
            self.tipul = self.count_bombs()

    def count_bombs(self):
        counter_bombs = 0
        for vecin in self.vecini:
            if vecin.tipul == "X":
                counter_bombs += 1
        return counter_bombs

    def determina_vecinii(self):
        if self.coloana in range(2, joc_1.numar_coloane) and self.rand in range(2, joc_1.numar_randuri):
            self.vecini += [harta[self.rand-1][self.coloana-2], harta[self.rand-1][self.coloana-1], harta[self.rand-1][self.coloana], harta[self.rand][self.coloana-2], harta[self.rand][self.coloana], harta[self.rand+1][self.coloana-2], harta[self.rand+1][self.coloana-1], harta[self.rand+1][self.coloana]]
        else:
            if self.rand == 1 and self.coloana == 1:
                self.vecini += [harta[1][1], harta[2][0], harta[2][1]]
            if self.rand == 1 and self.coloana == joc_1.numar_coloane:
                self.vecini += [harta[1][self.coloana-2], harta[2][self.coloana-2], harta[2][self.coloana-1]]
            if self.rand == joc_1.numar_randuri and self.coloana == 1:
                self.vecini += [harta[self.rand-1][self.coloana-1], harta[self.rand-1][self.coloana], harta[self.rand][self.coloana]]
            if self.rand == joc_1.numar_randuri and self.coloana == joc_1.numar_coloane:
                self.vecini += [harta[self.rand-1][self.coloana-1], harta[self.rand-1][self.coloana-2], harta[self.rand][self.coloana-2]]
            if self.rand == 1 and self.coloana in range(2, joc_1.numar_coloane):
                self.vecini += [harta[self.rand][self.coloana-2], harta[self.rand][self.coloana], harta[self.rand+1][self.coloana-2], harta[self.rand+1][self.coloana-1], harta[self.rand+1][self.coloana]]
            if self.rand == joc_1.numar_randuri and self.coloana in range(2, joc_1.numar_coloane):
                self.vecini += [harta[self.rand][self.coloana-2], harta[self.rand][self.coloana], harta[self.rand-1][self.coloana-2], harta[self.rand-1][self.coloana-1], harta[self.rand-1][self.coloana]]
            if self.coloana == 1 and self.rand in range(2, joc_1.numar_randuri):
                self.vecini += [harta[self.rand-1][self.coloana-1], harta[self.rand-1][self.coloana], harta[self.rand][self.coloana], harta[self.rand+1][self.coloana-1], harta[self.rand+1][self.coloana]]
            if self.coloana == joc_1.numar_coloane and self.rand in range(2, joc_1.numar_randuri):
                self.vecini += [harta[self.rand-1][self.coloana-1], harta[self.rand-1][self.coloana-2], harta[self.rand][self.coloana-2], harta[self.rand+1][self.coloana-2], harta[self.rand+1][self.coloana-1]]


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
        first_row = "   "
        for coloana in range(1, self.numar_coloane + 1):
            first_row += " {coloana} |".format(coloana=coloana)
        print(first_row)
        nr_coloane = ""
        for num in range(1, self.numar_randuri + 1):
            rand_nou = ""
            rand_nou += " {rand} ".format(rand = num)
            for coloana in range(1, self.numar_coloane + 1):
                rand_nou += " {} |".format(harta_activa[num][coloana-1].tipul)
            if num > 9:
                rand_nou = rand_nou[:3] + rand_nou[4:]
            print(rand_nou)

    def selectie(self):
        while joc_1.count_choice < joc_1.numar_coloane * joc_1.numar_randuri:
            print("TYPE \"F\" TO FLAG A BOMB || PRESS ENTER TO REVEAL A CLUE")
            input_selectie = input("")
            if input_selectie == "F":
                self.flag_a_bomb()
            else:
                input_rand = input("Introduceti randul: ")
                input_coloana = input("Introduceti coloana: ")
                self.reveal_clue(input_rand, input_coloana)
            all_boxes = []
            for lista in harta_activa.values():
                for box in lista:
                    if box.tipul is not " ":
                        all_boxes.append(box)
            if len(all_boxes) == joc_1.numar_coloane * joc_1.numar_randuri:
                print("FELICITARI {}, AI FINALIZAT JOCUL!".format(joc_1.denumire_jucator.upper()))
                exit()

    def flag_a_bomb(self):
        input_rand_bomba = int(input("Introduceti randul pentru semnalizare bomba: "))
        input_coloana_bomba = int(input("Introduceti coloana pentru semnalizare bomba: ")) - 1
        harta_activa[input_rand_bomba][input_coloana_bomba].tipul = "#"
        joc_1.count_choice += 1
        joc_1.vezi_harta_activa()

    def reveal_clue(self, input_rand, input_coloana):
        input_rand = int(input_rand)
        input_coloana = int(input_coloana) - 1
        box_selectat = harta[input_rand][input_coloana]
        if box_selectat.tipul == "X":
            joc_1.vezi_harta()
            print("GAME OVER")
            exit()
        else:
            if box_selectat.tipul == 0:
                harta_activa[input_rand][input_coloana] = box_selectat
                joc_1.count_choice += 1
                lista_vecini_zero = [box_selectat]
                for box in lista_vecini_zero:
                    for vecin in box.vecini:
                        if vecin.tipul == 0 and vecin not in lista_vecini_zero:
                            lista_vecini_zero.append(vecin)
                            harta_activa[vecin.rand][vecin.coloana-1] = vecin
                            for vecin_vecin in vecin.vecini:
                                harta_activa[vecin_vecin.rand][vecin_vecin.coloana-1] = vecin_vecin
                            joc_1.count_choice += 1
                joc_1.vezi_harta_activa()
            else:
                harta_activa[input_rand][input_coloana] = box_selectat
                joc_1.count_choice += 1
                joc_1.vezi_harta_activa()

    def populeaza_harta(self):
        all_boxes = list(harta.values())
        all_boxes_list = []
        for lista in all_boxes:
            for box in lista:
                all_boxes_list.append(box)
        for box in all_boxes_list:
            box.determina_tipul_box_selectat()

def initiere_joc():
    print("""
    WELCOME TO MINESWEEPER
    ----------------------
    
    """)
    nr_randuri = int(input("Numar randuri: "))
    nr_coloane = int(input("Numar coloane: "))
    max_nr_bombe = nr_randuri * nr_coloane  
    nr_recomandat_bombe = int(max_nr_bombe * 0.10)
    nr_bombe = int(input("Numar bombe (max {max}, recomandat {rec}): ".format(max = max_nr_bombe, rec = nr_recomandat_bombe)))
    denumire_jucator = input("Nume jucator: ")
    return Joc(nr_coloane, nr_randuri, nr_bombe, denumire_jucator)

joc_1 = initiere_joc()  
joc_1.generare_harta()
joc_1.generare_harta_activa()
joc_1.distribuire_bombe()
joc_1.populeaza_harta()
joc_1.vezi_harta_activa()
joc_1.selectie()
