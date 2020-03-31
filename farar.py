import random

karty = [{"farba": "cerven", "hodnota": "eso", "meno": "Červené eso"},
         {"farba": "zelen", "hodnota": "eso", "meno": "Zelené eso"},
         {"farba": "zalud", "hodnota": "eso", "meno": "Žaluďové eso"},
         {"farba": "gula", "hodnota": "eso", "meno": "Guľové eso"},
         {"farba": "cerven", "hodnota": "kral", "meno": "Červený kráľ"},
         {"farba": "zelen", "hodnota": "kral", "meno": "Zelený kráľ"},
         {"farba": "zalud", "hodnota": "kral", "meno": "Žaľuďový kráľ"},
         {"farba": "gula", "hodnota": "kral", "meno": "Guľový kráľ"},
         {"farba": "cerven", "hodnota": "hornik", "meno": "Červený horník"},
         {"farba": "zelen", "hodnota": "hornik", "meno": "Zelený horník"},
         {"farba": "zalud", "hodnota": "hornik", "meno": "Žaľuďový horník"},
         {"farba": "gula", "hodnota": "hornik", "meno": "Guľový horník"},
         {"farba": "cerven", "hodnota": "dolnik", "meno": "Červený dolník"},
         {"farba": "zelen", "hodnota": "dolnik", "meno": "Zelený dolník"},
         {"farba": "zalud", "hodnota": "dolnik", "meno": "Žaľuďový dolník"},
         {"farba": "gula", "hodnota": "dolnik", "meno": "Guľový dolník"},
         {"farba": "cerven", "hodnota": "desiatka", "meno": "Červená desiatka"},
         {"farba": "zelen", "hodnota": "desiatka", "meno": "Zelená desiatka"},
         {"farba": "zalud", "hodnota": "desiatka", "meno": "Žaľuďová desiatka"},
         {"farba": "gula", "hodnota": "desiatka", "meno": "Guľová desiatka"},
         {"farba": "cerven", "hodnota": "deviatka", "meno": "Červená deviatka"},
         {"farba": "zelen", "hodnota": "deviatka", "meno": "Zelená deviatka"},
         {"farba": "zalud", "hodnota": "deviatka", "meno": "Žaľuďová deviatka"},
         {"farba": "gula", "hodnota": "deviatka", "meno": "Guľová deviatka"},
         {"farba": "cerven", "hodnota": "osmicka", "meno": "Červená osmička"},
         {"farba": "zelen", "hodnota": "osmicka", "meno": "Zelená osmička"},
         {"farba": "zalud", "hodnota": "osmicka", "meno": "Žaľuďová osmička"},
         {"farba": "gula", "hodnota": "osmicka", "meno": "Guľová osmička"},
         {"farba": "cerven", "hodnota": "sedmicka", "meno": "Červená sedmička"},
         {"farba": "zelen", "hodnota": "sedmicka", "meno": "Zelená sedmička"},
         {"farba": "zalud", "hodnota": "sedmicka", "meno": "Žaľuďová sedmička"},
         {"farba": "gula", "hodnota": "sedmicka", "meno": "Guľová sedmička"},]
karty1 = []
hraci = []

def refresh():
    global karty
    global karty1
    global hraci
    for i in range(len(karty1)):
        karty.append(karty1[i])
        del karty[i]
    for j in range(len(hraci)):
        for k in range(len(hraci[j]["karty"])):
            karty.append(hraci[j]["karty"][k])
            del hraci[j]["karty"][k]
def dalsi_hrac(poradie):
    hraci.append({"meno": "", "poc_kar": 5,"tah": True,"vypad": 0})
    hraci[poradie - 1]["tah"] = False
    hraci[poradie]["meno"] = input(f"Zadaj meno {poradie + 1} hráča: ")
def zamiesat():
    for j in range(32):
        global karty
        global karty1
        kart = random.randint(0, len(karty)-1)
        karty1.append(karty[kart])
        del karty[kart]
    karty, karty1 = karty1, karty
def rozdat(hrac):##skontrolovat/ale asi to je dobre
    if hrac:
        hrac_karty = []
        for i in range(hrac):
            kart = random.randint(0, len(karty)-1)
            hrac_karty.append(karty[kart])
            del karty[kart]
        return hrac_karty
def potiahni(kar_brat):
    global karty
    global karty1
    hrac_karty = []
    for i in range(kar_brat):
        hrac_karty.append(karty[0])
        del karty[0]
        check_kopa()
    return hrac_karty
def check_kartu(karta):
    global statie
    global branie
    global hraci
    poradie = []
    if karta["hodnota"] == "eso":
        statie += 1
    elif karta["hodnota"] == "hornik":
        print("Použil si horníka na akú farbu chceš zmeniť?")
        print("Zadaj:")
        print("1. pre červeň")
        print("2. pre zeleň")
        print("3. pre žaluď")
        print("4. pre guľu")
        while True:
            try:
                farba = int(input())
                if farba == 1:
                    karta["farba"] = "cerven"
                    break
                if farba == 2:
                    karta["farba"] = "zelen"
                    break
                if farba == 3:
                    karta["farba"] = "zalud"
                    break
                if farba == 4:
                    karta["farba"] = "gula"
                    break
            except ValueError:
                print("Nezadal si číslo")
    elif karta["hodnota"] == "sedmicka":
        if karta["farba"] == "cerven":
            print("Použil si červenú sedmu ")
            for i in range(len(hraci)):
                if hraci[i]["vypad"] == 1:
                    poradie.append(i)
                    if len(poradie) == 1:
                        print("Môžeš vrátiť do hry:")
                    print(len(poradie), hraci[i]["meno"])
            if len(poradie) == 0:
                print("Nemôžeš nikoho vrátiť do hry.")
                print("Ďalší hráč ťahá +3 karty")
                branie += 3
                return karta
            while True:
                try:
                    hracv = int(input("Zadaj číslo hráča ktorého chceš vrátiť do hry alebo 0 pre použitie červenej sedmy ako normalnu sedmu"))
                    if hracv >= 1 and hracov <= len(poradie):
                        poradie[hracv]
                    elif hacv == 0:
                        branie += 3
                    else:
                        print("Zadal si zlé číslo")
                except ValueError:
                    print("Nezadal si číslo")
        else:
            branie += 3##pozor!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cervena sedma chyba
    return karta
def check_kopa():
    global karty
    global karty1
    if not karty:
        print("prehodenie balíčka")
        karty, karty1 = karty1, karty
        karty1.append(karty[-1])
        del(karty[-1])
def hrac_kolo(hrac,hrac_karty,meno,vypad):##co kurva je hrac?? uz viem to je to povodne cym som urcoval if hrac zbehni vyhadzovanie ze ci ma karty ale da sa to aj len s kartami takze to pravdepodobne netreba,MOZNO HO VYUZIJEME PRI POCITANI VYTAZA/ale asi nie netreba to    
    global karty
    global karty1
    global statie
    global branie
    prihodenie = False
    potiahnutie = 0
    vyhovujuce = []
    vybrata_karta = []##pocitanie ukoncenia kola
    if not hrac_karty:
        return hrac_karty
    print("Na ťahu je " + meno)
    if statie >= 1:
        print("Stojíš")
        while True:
            vyhovujuce = []
            for i in range(len(hrac_karty)):
                pocet = i + 1
                if "eso" == hrac_karty[i]["hodnota"]:
                    vyhovujuce.append(i)
                    if len(vyhovujuce) == 1:
                        print("Môžeš sa prebiť:")
                    print(len(vyhovujuce) + ". " + hrac_karty[i]["meno"])
            if len(vyhovujuce) == 0:
                statie -= 1
                return hrac_karty
            while True:
                try:
                    cislo_kar_stat = int(input("Zadaj číslo karty ktorú chceš použiť alebo číslo 0 ak nechceš žiadnu: "))
                    hrac_karta = cislo_kar_stat - 1
                    if cislo_kar_stat == 0:
                        satie -= 1
                        return hrac_karty
                    elif cislo_kar_stat > 0 and cislo_kar_stat <= len(vyhovujuce):
                        statie += 1
                        karty1.append(hrac_karty[vyhovujuce[hrac_karta]])
                        del hrac_karty[vyhovujuce[hrac_karta]]
                        break
                except ValueError:
                    print("Nezadal si číslo")
    if branie >= 1:
        vyhovujuce = []
        print("Ťaháš")
        while True:
            for i in range(len(hrac_karty)):
                pocet = i + 1
                if "sedmicka" == hrac_karty[i]["hodnota"] or "Zelený dolník" == hrac_karty[i]["meno"]:
                    vyhovujuce.append(i)
                    if len(vyhovujuce) == 1:
                        print("Môžeš sa prebiť:")
                    print(len(vyhovujuce) + ". " + hrac_karty[i]["meno"])
            if len(vyhovujuce) == 0:
                if prihodenie == True:
                    return hrac_karty
                else:
                    potiahnutie += 1
                    if potiahnutie <= 3:
                        branie -= 1
                        potiahni(hrac_karty,1)
                        continue
                    else:
                        potiahni(hrac_karty,branie)
                        branie = 0
                        return hrac_karty
            while True:
                try:
                    cislo_kar_stat = int(input("Zadaj číslo karty ktorú chceš použiť alebo číslo 0 ak nechceš použiť žiadnu: "))
                    hrac_karta = cislo_kar_stat - 1
                    if cislo_kar_stat == 0:
                        if prihodenie == True:
                            return hrac_karty
                        potiahnutie += 1
                        if potiahnutie <= 3:
                            branie -= 1
                            potiahni(hrac_karty,1)
                            break
                        else:
                            potiahni(hrac_karty,branie)
                            branie = 0
                            return hrac_karty
                    elif cislo_kar_stat > 0 and cislo_kar_stat <= len(vyhovujuce):
                        if "sedmicka" == hrac_karty[vyhovujuce[hrac_karta]]["hodnota"]:
                            if potiahnutie == 0:
                                branie += 3
                                prihodenie = True
                                karty1.append(hrac_karty[vyhovujuce[hrac_karta]])
                                del hrac_karty[vyhovujuce[hrac_karta]]
                                break
                            else:
                                branie = 3
                                karty1.append(hrac_karty[hrac_karta])
                                del hrac_karty[hrac_karta]
                                return hrac_karty
                        elif "Zelený dolník" == hrac_karty[vyhovujuce[hrac_karta]]["meno"]:
                            if prihodenie == False:
                                branie = 0
                                karty1.append(hrac_karty[vyhovujuce[hrac_karta]])
                                del hrac_karty[vyhovujuce[hrac_karta]]
                                return hrac_karty
                            else:
                                print("Nemôžeš vyhodiť  kartu a potom dať Zeleného dolníka")
                    else:
                        print("Zadal si číslo mimo rozsahu")
                except ValueError:
                    print("Nezadal si číslo")
    print("Vyložená karta je: " + karty1[-1]["meno"])
    print(meno + " má na ruke:")
    for i in range(len(hrac_karty)):
        vyhovujuce.append(i)
        pocet = i + 1
        print(len(vyhovujuce) + ". " + hrac_karty [i]["meno"])
    while True:
        try:
            cislo_kar = int(input("Zadaj číslo karty ktorú chceš použiť alebo číslo 0 aby si poťiahol: "))
            if cislo_kar == 0:
                potiahni(hrac_karty)
                return hrac_karty
            elif cislo_kar > 0 and cislo_kar <= len(vyhovujuce):
                hrac_karta = cislo_kar - 1
                if hrac_karty[vyhovujuce[hrac_karta]]["farba"] == karty1[-1]["farba"] or hrac_karty[vyhovujuce[hrac_karta]]["hodnota"] == karty1[-1]["hodnota"] or hrac_karty[vyhovujuce[hrac_karta]]["hodnota"] == "hornik":
                    vybrata_karta.append(hrac_karty[vyhovujuce[hrac_karta]])
                    del hrac_karty[vyhovujuce[hrac_karta]]
                    while True:
                        vyhovujuce = []
                        for i in range(len(hrac_karty)):
                            pocet = i + 1
                            if vybrata_karta[0]["hodnota"] == hrac_karty[i]["hodnota"]:
                                vyhovujuce.append(i)
                                if len(vyhovujuce) == 1:
                                    print("Ešte môžeš vyhodiť:")
                                print(len(vyhovujuce) + ". " + hrac_karty [i]["meno"])##to pocitanie by chcelo upraviť/alebo by som to cele upravil aby to menej pomahalo hracovi ze to vypise vsetky karty
                        while True:
                            if len(vyhovujuce) == 0:  
                                vybrata_karta[0] = check_kartu(vybrata_karta[0])
                                karty1.append(vybrata_karta[0])
                                del vybrata_karta[0]
                                return hrac_karty
                            try:
                                cislo_kar1 = int(input("Zadaj číslo karty ktorú chceš použiť alebo číslo 0 ak nechceš žiadnu: "))
                                hrac_karta = cislo_kar1 - 1
                                if cislo_kar1 == 0:
                                    return hrac_karty
                                elif vybrata_karta[0]["hodnota"] == hrac_karty[vyhovujuce[hrac_karta]]["hodnota"]:
                                    vybrata_karta[0] = check_kartu(vybrata_karta[0])
                                    karty1.append(vybrata_karta[0])
                                    del vybrata_karta[0]
                                    vybrata_karta.append(hrac_karty[vyhovujuce[hrac_karta]])
                                    del hrac_karty[vyhovujuce[hrac_karta]]
                                    break##nedorobene/mozno uz hej/nemen za return
                            except ValueError:
                                print("Nezadal si číslo")
                else:
                    print("Túto kartu nemôžeš položiť na vrch tohto balíčka")
            else:
                print("Zadal si číslo mimo rozsahu")
        except ValueError:
            print("Nezadal si číslo")

vysledky = []
sucet_kol = 0
sucet_hrac = 0
poc_hrac = 0
blazon = 0
statie = 0
branie = 0
while True:
    try:
        poc_hrac = int(input("Zadaj počet hráčov(MIN 2 MAX 4): "))
        if poc_hrac >= 2 and poc_hrac <= 4:
            break
    except ValueError:
        if blazon % 2 == 1 and blazon != 0:
            print("Jebe ti?")
        elif blazon % 2 == 0 and blazon != 0:
            print("Tak ty si kokot")
        else:
            print("Nerozumel som, skús to znovu")
        blazon += 1
hraci.append({"meno": "", "poc_kar": 5,"tah": False,"vypad": 0})
hraci[0]["meno"] = input("Zadaj meno 1. hráča: ")
hraci.append({"meno": "", "poc_kar": 5,"tah": True,"vypad": 0})
hraci[1]["meno"] = input("Zadaj meno 2. hráča: ")
for i in range(4):
    if poc_hrac > i + 2:
        dalsi_hrac(i + 2)
while sucet_hrac != len(hraci) - 1:##hrac_sucet neni spraveny
    zamiesat()
    print("Vyložená karta je: " + karty [-1]["meno"])
    karty1.append(karty[-1])
    del karty[-1]
    print("Spodná karta je: " + karty [-1]["meno"])
    if karty[-1]["hodnota"] == "sedmicka" or karty[-1]["hodnota"] == "eso":
        print("Na Spodku balíčka je" + karty[-1]["meno"])
        if karta["hodnota"] == "eso":
            print("Prvý hráč stojí")
            statie += 1
        elif karta["hodnota"] == "sedmicka":
            print("Prvý hráč ťahá")
            branie += 3
    elif karty[-1]["hodnota"] == "hornik":##neni som si isty ako funguje mat horka na spodku balicka ale zda sa mi ze by to malo byt v tom ife hore a ostaval by v kartach/nesiel by do kariet1
        print("Na Spodku balíčka je" + karty[-1]["meno"])
        karty1.append(karty[-1])
        del karty[-1]
    sucet_hrac = 0
    for i in range(len(hraci)):
        hraci[i]["vypad"] = 0
        if hraci[i]["poc_kar"] != 0:
            vyherca = hraci[i]["meno"]
        else:
            sucet_hrac += 1
        hraci[i]["karty"] = potiahni(hraci[i]["poc_kar"])
    for i in range(len(hraci)):
        if hraci[i]["tah"] == True:
            hraci[i]["tah"] = False
            try:
                hraci[i + 1]["tah"] = True
                break
            except IndexError:
                hraci[0]["tah"] = True
                break
    while sucet_kol != len(hraci) - 1:
        sucet_kol = 0
        for i in range(len(hraci)):
            if hraci[i]["tah"] == True:
                hraci[i]["karty"] = hrac_kolo(hraci[i]["poc_kar"],hraci[i]["karty"],hraci[i]["meno"], hraci[i]["vypad"])
                if hraci[i]["karty"] == []:
                    hraci[i]["vypad"] += 1
                hraci[i]["tah"] = False
                try:
                    hraci[i + 1]["tah"] = True
                except IndexError:
                    hraci[0]["tah"] = True
                if hraci[i]["karty"] == []:
                    sucet_kol += 1
                    meno = hraci[i]["meno"]
    print(f"Kolo prehral hráč {meno}")
    for i in range(len(hraci)):
        if hrac[i]["poc_kar"] == 0:
            vysledky.append(hrac[i]["meno"])
        if hrac[i]["meno"] == meno:
            hrac[i]["poc_kar"] -= 1
    input("Stlač enter pre pokračovanie...")
    refresh()
print(f"Hru vyhral {vyherca}")
print(f"1. {vyherca}")##dokoncit cervenu sedmu(cervena sedma na konci)
for i in range(len(vysledky)):##treba fixnut vzber karat ked je ich menej viz cervena sedma/asi som myslel tahanie ked vsetky karty budu na ruke hraca a ziadna na kvopke a hrac bude chciet potiahnut
    print(i + 2, ". ", vysledky[len(vysledky) - 1 - i])##treba doplnit dalsi balicek ak je hracov viac ako 4(ale mozno sa nato vyjebem je to trochu kktina ale moyem obmedyit hracov na 4) a treba fixnut tahanie z balicka(ked tam uz nic nebude)
input("Stlač enter pre ukončenie...")##este chyba aj spalena

