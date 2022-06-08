import numpy as np #te trzeba pobrać
import random as rand
import time
import os
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
#statystyki
poziom=0
exp=0
sila=10
szybkosc=5
czas=0
kasa=0
maxzdrowie=100
zdrowie=100
dzien=0
bron="patyk"
wymiana=""
ilosc_p=1
ekwipunek=np.array(["puste miejsce" for x in range(64)])
ekwipunek[0]="apteczka"
mapa = np.array([[x for y in range(16)] for x in range(16)])
for y in range(16):
    for x in range(16):
        mapa[y][x]=0
przeszkoda_y=np.array([rand.randint(0,15) for x in range(16)])
przeszkoda_x=np.array([rand.randint(0,15) for x in range(16)])
sklepy_y = np.array([rand.randint(2,12) for x in range(4)])
sklepy_x = np.array([rand.randint(2,12) for x in range(4)])
bossowie_x=np.array([rand.randint(0,15) for x in range(6)])
bossowie_y=np.array([rand.randint(0,15) for x in range(6)])
spawn=np.array([rand.randint(8,12) for x in range(2)])
for x in range(16):
    mapa[przeszkoda_x[x]][przeszkoda_y[x]]=3
for x in range(4):
    mapa[sklepy_x[x]][sklepy_y[x]]=1
sklepy=np.array([[sklepy_x[0],sklepy_y[0]],[sklepy_x[1],sklepy_y[1]],[sklepy_x[2],sklepy_y[2]],[sklepy_x[3],sklepy_y[3]]])
for x in range(6):
    if bossowie_x[x]<11 and bossowie_x[x]>4:
        if bossowie_x[x]>8:
            bossowie_x[x]=rand.randint(11,15)
        else:
            bossowie_x[x]=rand.randint(11,15)
    if bossowie_y[x]<11 and bossowie_y[x]>4:
        if bossowie_y[x]>8:
            bossowie_y[x]=rand.randint(11,15)
        else:
            bossowie_y[x]=rand.randint(11,15)
for x in range(3):
    mapa[bossowie_x[x]][bossowie_y[x]]=4
vismapa=""
def przeciwnicy():
    for x in range(16):
        for y in range(16):
            if mapa[x][y]==5:
                mapa[x][y]=0
    for x in range(rand.randint(50,300)//5):
        zgodnosc_wroga=False
        while zgodnosc_wroga==False:
            wrog_y=rand.randint(0,15)
            wrog_x=rand.randint(0,15)
            if mapa[wrog_x][wrog_y]==0:
                mapa[wrog_x][wrog_y]=5
                zgodnosc_wroga=True
def wyswietl(poz_x,poz_y):
    print("Dzień:"+str(dzien))
    print("aktualny poziom:"+str(poziom))
    print("zdrowie:"+str(zdrowie)+"/"+str(maxzdrowie))
    for x in range(16):
        vismapa="|"
        for y in range(16):
            if x==poz_x and y==poz_y:
                vismapa= vismapa + "0|"
            elif mapa[x][y]==0:
                vismapa= vismapa + " |"
            elif mapa[x][y]==1:
                vismapa= vismapa +"$|"
            elif mapa[x][y]==3:
                vismapa= vismapa + "#|"
            elif mapa[x][y]==4:
                vismapa= vismapa + "!|"
            elif mapa[x][y]==5:
                vismapa= vismapa + "X|"
            elif mapa[x][y]==6:
                vismapa=vismapa + "?|"
        print(vismapa)
przeciwnicy()
wyswietl(spawn[0],spawn[1])
pozycja=np.array([spawn[0],spawn[1]])
def atak():
    if bron=="patyk":
        return sila+5+4*poziom
    elif bron=="miecz":
        return sila//0.8+10+8*poziom
    elif bron=="topor":
        return sila//0.6+6*poziom
    elif bron=="wlocznia":
        return zdrowie//4+10*poziom+1
def walka():
    global zdrowie
    global maxzdrowie
    koniec=False
    while koniec==False:
        clear()
        poziom_wroga=dzien+rand.randint(0,4)-2
        if poziom_wroga<0:
            poziom_wroga=0
        wrog_zdrowie=20+4*poziom_wroga
        print("napotykasz wroga poziomu "+str(poziom_wroga)+" !")
        time.sleep(1.5)
        while zdrowie>0:
            clear()
            print("twoje zdrowie: "+str(zdrowie)+"/"+str(maxzdrowie))
            print("zdrowie wroga: "+str(wrog_zdrowie))
            print("co zrobisz?")
            print("1-atak 2-odwrót 3-leczenie(zużywa apteczkę)")
            opcja=0
            while int(opcja) < 1 or int(opcja) > 3:
                opcja=input()
            if int(opcja)==1:
                wrog_zdrowie=wrog_zdrowie-atak()
                print("zadałes "+str(atak())+" obrażeń!")
                if wrog_zdrowie<=0:
                    return 1
                    koniec=True
            elif int(opcja)==2:
                if rand.randint(0,1)==0:
                    print("nie udało się uciec!")
                else:
                    print("udało się uciec!")
                    return 2
                    koniec=True
            elif int(opcja)==3:
                while x!=-1:
                    if ekwipunek[x]=="apteczka":
                        zdrowie*=2
                        if zdrowie>maxzdrowie:
                            zdrowie=maxzdrowie
                        ekwipunek[x]=""
                        break
            print("kolej przeciwnika!")
            zdrowie-=poziom_wroga*2+5
            print("wrog zadał "+str(poziom_wroga*2+5)+"obrażeń!")
            if zdrowie<=0:
                return 0
            time.sleep(2.5)
numer_bossa=1
def boss():
    global zdrowie 
    global numer_bossa
    print("WALKA Z BOSSEM!")
    zdrowie_bossa=numer_bossa*numer_bossa*100
    while zdrowie>0:
        print("Twoje zdrowie:"+str(zdrowie))
        print("zdrowie bossa:"+str(zdrowie_bossa))
        print("co zrobisz?")
        print("1-atak 2-odwrót 3-leczenie(zużywa apteczkę)")
        opcja=0
        while int(opcja) < 1 or int(opcja) > 3:
            opcja=input()
        if int(opcja)==1:
            zdrowie_bossa=zdrowie_bossa-atak()
            print("zadałes "+str(atak())+" obrażeń!")
            if zdrowie_bossa<=0:
                return 1
                koniec=True
        elif int(opcja)==2:
            if rand.randint(0,1)==0:
                print("nie udało się uciec!")
            else:
                print("udało się uciec!")
                return 2
                koniec=True
        elif int(opcja)==3:
            while x!=-1:
                if ekwipunek[x]=="apteczka":
                    zdrowie*=2
                    if zdrowie>maxzdrowie:
                        zdrowie=maxzdrowie
                    ekwipunek[x]=""
                    break
        print("kolej bossa!")
        zdrowie-=25*numer_bossa*numer_bossa
        print("boss zadał "+str(25*numer_bossa*numer_bossa)+"obrażeń!")
        time.sleep(2.5)
        clear()
        if zdrowie<=0:
            return 0
def full():
    global ilosc_p
    print("proszę wybrać przedmiot do usunięcia z eq")
    for x in range(ilosc_p):
        print(str(x)+"."+ekwipunek[x])
    x = input()
    return x
def sklep():#dlaczego ja to tak komplikuję?
    global kasa
    global zdrowie
    global wymiana
    global bron
    global sila
    global szybkosc
    global czas
    print("Witamy w sklepie")
    if pozycja[0]==sklepy[0][0] and pozycja[1]==sklepy[0][1]:
        print("1.Miecz(45)")
        print("2.Apteczka(15)")
        print("3.Wypoczynek(5[-1 tura])")
        wybor=input()
        if int(wybor) == 1:
            if kasa >=45:
                kasa-=45
                wymiana=bron
                bron="miecz"
                if ilosc_p==64:
                    ekwipunek[full()]=wymiana
                else:
                    ekwipunek[ilosc_p]=wymiana
                print("zakupiłes miecz")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
        if int(wybor) == 2:
            if kasa >=15:
                kasa -= 15
                if ilosc_p==64:
                    ekwipunek[full()]="apteczka"
                else:
                    ekwipunek[ilosc_p]="apteczka"
                print("zakupiłes apteczkę")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
        if int(wybor) == 3:
            if kasa >=5:
                kasa -= 5
                czas +=1
                zdrowie = maxzdrowie
                if czas == szybkosc:
                    print("nowy dzień!")
                    dzien+=1
                    time.sleep(2)
                    czas=0
                print("wyleczyłeś się")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
    elif pozycja[0]==sklepy[1][0] and pozycja[1]==sklepy[1][1]:
        print("1.topór(45)")
        print("2.Perma Wzmocnienie("+str(sila*4+5)+")")
        print("3.Wypoczynek(5[-1 tura])")
        wybor=input()
        if int(wybor) == 1:
            if kasa >=45:
                kasa-=45
                wymiana=bron
                bron="topor"
                if ilosc_p==64:
                    ekwipunek[full()]=wymiana
                else:
                    ekwipunek[ilosc_p]=wymiana
                print("zakupiłes topór")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
        if int(wybor) == 2:
            if kasa >=sila*4+5:
                kasa -= sila*4+5
                sila+=1
                print("zakupiłes wzmocnienie")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
        if int(wybor) == 3:
            if kasa >=5:
                kasa -= 5
                czas +=1
                zdrowie = maxzdrowie
                if czas == szybkosc:
                    print("nowy dzień!")
                    dzien+=1
                    time.sleep(2)
                    czas=0
                print("wyleczyłes się")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
    elif pozycja[0]==sklepy[2][0] and pozycja[1]==sklepy[2][1]:
        print("1.włócznia(45)")
        print("2.Apteczka(15)")
        print("3.Wypoczynek(5[-1 tura])")
        wybor=input()
        if int(wybor) == 1:
            if kasa >=45:
                kasa-=45
                wymiana=bron
                bron="wlocznia"
                if ilosc_p==64:
                    ekwipunek[full()]=wymiana
                else:
                    ekwipunek[ilosc_p]=wymiana
                print("zakupiłes włócznie")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
        if int(wybor) == 2:
            if kasa >=15:
                kasa -= 15
                if ilosc_p==64:
                    ekwipunek[full()]="apteczka"
                else:
                    ekwipunek[ilosc_p]="apteczka"
                print("zakupiłes apteczkę")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
        if int(wybor) == 3:
            if kasa >=5:
                kasa -= 5
                czas +=1
                zdrowie = maxzdrowie
                if czas == szybkosc:
                    print("nowy dzień!")
                    dzien+=1
                    time.sleep(2)
                    czas=0
                print("wyleczyłes się")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
    elif pozycja[0]==sklepy[3][0] and pozycja[1]==sklepy[3][1]:
        print("1.Miecz(45)")
        print("2.przyspieszenie("+str(szybkosc*2+10)+")")
        print("3.Wypoczynek(15)")
        wybor=input()
        if int(wybor) == 1:
            if kasa >=45:
                kasa-=45
                wymiana=bron
                bron="miecz"
                if ilosc_p==64:
                    ekwipunek[full()]=wymiana
                else:
                    ekwipunek[ilosc_p]=wymiana
                print("zakupiłes miecz")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
        if int(wybor) == 2:
            if kasa >=szybkosc*2+10:
                kasa -= szybkosc*2+10
                print("zakupiłes przyspieszenie")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
        if int(wybor) == 3:
            if kasa >=15:
                kasa -= 15
                zdrowie = maxzdrowie
                print("wyleczyłes się")
                time.sleep(1.5)
            else:
                print("nie masz wystaczająco pieniędzy!")
                time.sleep(1.5)
while zdrowie > 0:
    zgodnosc_ruchu=False
    while zgodnosc_ruchu==False:
        print("co chcesz robić? (ruch-wasd)(interakcja-e)(POMOC - p)(Legenda - l)(ekwipunek - i)")
        ruch=input()
        if ruch=="w":
            if pozycja[0]!=0:
                if mapa[pozycja[0]-1][pozycja[1]]!=3:
                    pozycja[0]=pozycja[0]-1
                    zgodnosc_ruchu=True
        elif ruch=="a":
            if pozycja[1]!=0:
                if mapa[pozycja[0]][pozycja[1]-1]!=3:
                    pozycja[1]=pozycja[1]-1
                    zgodnosc_ruchu=True
        elif ruch=="s":
            if pozycja[0]!=15:
                if mapa[pozycja[0]+1][pozycja[1]]!=3:
                    pozycja[0]=pozycja[0]+1
                    zgodnosc_ruchu=True
        elif ruch=="d":
            if pozycja[1]!=15:
                if mapa[pozycja[0]][pozycja[1]+1]!=3:
                    pozycja[1]=pozycja[1]+1
                    zgodnosc_ruchu=True
        elif ruch=="p":
            print("Twoim celem jest dojście i pokonanie wszystkich bosów ukazanych na mapie, lecz będziesz potrzebował do tego silniejszego sprzętu."
            "Możesz wchodzić w interakcje wchodząc na to samo pole co obiekt interakcji np. sklep, wróg. "
            "Atakuj wrogów i zdobywaj z nich sprzęt oraz pienądze, które możesz wydać w sklepie.Powodzenia!")
        elif ruch=="l":
            print("0-twoja postać")
            print("$-sklep")
            print("#-formacja terenu uniemożliwiająca wejście na to pole")
            print("X-przeciwnik")
            print("!-boss (twój cel główny)")
        elif ruch=="e":
            if mapa[pozycja[0]][pozycja[1]]==1:
                sklep()
                time.sleep(2)
            if mapa[pozycja[0]][pozycja[1]]==5:
                wynik=walka()
                if wynik==0:
                    print("Dziękujemy za grę, lecz umarłeś :)")
                    time.sleep(4)
                    continue
                elif wynik==1:
                    exp+=10+2*dzien
                    print("wygrałeś!")
                    print("zdobywasz "+str(10+2*dzien)+" expa")
                    print("zdobywasz "+str(15+dzien)+" kasy")
                    kasa+=15+dzien
                    mapa[pozycja[0]][pozycja[1]]=0
                    if exp>=5+poziom*0.5:
                        time.sleep(0.5)
                        exp-=5+poziom*0.5
                        poziom+=1
                        print("poziom w górę!")
                        maxzdrowie = 100 + poziom * 25
                    time.sleep(2)
                    wyswietl(pozycja[0],pozycja[1])
                elif wynik==2:
                    time.sleep(2)
                    wyswietl(pozycja[0],pozycja[1])
            if mapa[pozycja[0]][pozycja[1]]==4:
                wynik=boss()
                if wynik==0:
                    print("Dziękujemy za grę, lecz umarłeś :)")
                    time.sleep(4)
                    continue
                elif wynik==1:
                    exp+=10+2*dzien
                    print("wygrałeś!")
                    mapa[pozycja[0]][pozycja[1]]=0
                    print("poziom w górę!x2")
                    poziom+=2
                    maxzdrowie = 100 + poziom * 25
                    time.sleep(2)
                    wyswietl(pozycja[0],pozycja[1])
                    kasa+=500*numer_bossa
                    numer_bossa+=1
                    if numer_bossa==4:
                        print("Gratuluję! Wygrałeś!")
        elif ruch=="i":
            print("masz 8 sekund na popatrzenie")
            print("bron:"+str(bron))
            for x in range(ilosc_p):
                print(str(x)+"."+str(ekwipunek[x]))
            time.sleep(8)
        if ruch!="i":
            czas+=1
            if czas==szybkosc:
                print("nowy dzień!")
                dzien+=1
                time.sleep(2)
                czas=0
                przeciwnicy()
    clear()
    wyswietl(pozycja[0],pozycja[1])