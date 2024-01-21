
def Lisamine(i:list,p:list,k:int):
    """Andmete lisamine listidesse
    Tagastab listud
    
    :param list i: Inimeste nimekiri
    :param list p: Palkage loetelu
    :param int k: Inimeste kogus
    :rtype:list, list
    """
    
    for x in range(k):
        nimi=input("Mis on inimese nimi?")
        palk=int(input("Kui suur palk tal on? "))
        i.append(nimi)
        p.append(palk)
    return i,p
def SuurimPalk(i:list,p:list):
    """
    """
    nimi_list=[]
    max_=max(p)#suurim palk
    #kogus=p.count(max_)#nende kogus
    a=0
    for palk in p:
        if palk==max_:
            ind=p.index(max_,a)
            nimi=i[ind]
            a+=1
            nimi_list.append(nimi)
    return max_,nimi_list

def Sort(i:list,p:list,a:int):
    """
    """
    N=len(i)
    if a==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    kaust=p[n]
                    p[n]=p[m]
                    p[m]=kaust
                    kaust=i[n]
                    i[n]=i[m]
                    i[m]=kaust
    else:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]>p[m]:
                    kaust=p[n]
                    p[n]=p[m]
                    p[m]=kaust
                    kaust=i[n]
                    i[n]=i[m]
                    i[m]=kaust
    return i,p

def Kustutamine(i:list,p:list):
    """
    """
    nimi=input("Nimi: ")
    n=i.count(nimi)   
    if n>0:
        for x in i:
            if x==nimi:
                ind=i.index(x)
                i.remove(x)
                p.pop(ind)
    else:
        print(nimi,"ei ole nimekirjas")
    return i,p

        
def lyudi_s_odinakovoy_zarplatoi(imena, zarplati):
    """
    Найти людей, у которых одинаковая зарплата, найти сколько таких людей и вывести их данные на экран.

    :param list imena: Список имен
    :param list zarplati: Список зарплат
    """
    unikalnye_zarplati = set(zarplati)

    for zarplata in unikalnye_zarplati:
        indeksy = [i for i, x in enumerate(zarplati) if x == zarplata]
        if len(indeksy) > 1:
            print(f"Люди с зарплатой {zarplata}:")

            for indeks in indeksy:
                print(f"Имя: {imena[indeks]}, Зарплата: {zarplati[indeks]}")

def poisk_zarplaty_po_imeni(imena, zarplati, poisk_imeni):
    """
    Найти зарплату человека по его имени.

    :param list imena: Список имен
    :param list zarplati: Список зарплат
    :param str poisk_imeni: Имя для поиска
    :return: Зарплата найденного человека или None, если человек не найден
    """
    indeksy = [i for i, x in enumerate(imena) if x == poisk_imeni]

    if indeksy:
        indeks_zarplaty = indeksy[0]
        return zarplati[indeks_zarplaty]
    else:
        return None

def spisok_lyudey_s_zarplatami(imena, zarplati, porogovaja_zarplata, vverh=True):
    """
    Вывести список людей (с зарплатами), кто получает больше/меньше чем указанная сумма.

    :param list imena: Список имен
    :param list zarplati: Список зарплат
    :param int porogovaja_zarplata: Пороговая зарплата
    :param bool vverh: True, если нужно вывести тех, кто получает больше, False - меньше
    """
    otfiltrirovannye_lyudi = [(imena[i], zarplati[i]) for i in range(len(imena)) if (zarplati[i] > порогovaya_zarplata) == vverh]

    print(f"Люди {'с зарплатой выше' if vverh else 'с зарплатой ниже'} {порогovaya_zarplata}:")

    for chelovek in otfiltrirovannye_lyudi:
        print(f"Имя: {chelovek[0]}, Зарплата: {chelovek[1]}")

def top_bogatye_i_bednye(imena, zarplati, n=5):
    """
    Вывести ТОП n самых бедных и самых богатых людей.

    :param list imena: Список имен
    :param list zarplati: Список зарплат
    :param int n: Количество человек в ТОПе
    """
    ototsortirovannye_lyudi = sorted(zip(imena, zarplati), key=lambda x: x[1])

    print(f"ТОП {n} самых бедных:")
    for i in range(n):
        print(f"Имя: {ototsortirovannye_lyudi[i][0]}, Зарплата: {ototsortirovannye_lyudi[i][1]}")

    print(f"\nТОП {n} самых богатых:")
    for j in range(-1, -n-1, -1):
        print(f"Имя: {ototsortirovannye_lyudi[j][0]}, Зарплата: {ototsortirovannye_lyudi[j][1]}")
        

from zarplata import *

palgad=[1200,4200,750,395,8200]
inimesed=["A","B","A","D","E"]

while True:
    print("Lisamine-1\nKustutamine-2\nSuurimPalk-3\nSort-5")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest lisame? "))
        inimesed,palgad=Lisamine(inimesed,palgad,k)
        for i in range(len(palgad)):
            print(inimesed[i],"saab kätte",palgad[i])
    elif v==2:
        inimesed,palgad=Kustutamine(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif v==3:
        maxpalk,nimi=SuurimPalk(inimesed,palgad)
        print(nimi,"saab kätte",maxpalk,"Eur")
    elif v==5:
        i=int(input("Kasvab-0,Kahaneb-1"))
        inimesed,palgad=Sort(inimesed,palgad,i)
        for i in range(len(palgad)):
            print(palgad[i],"on",inimesed[i],"-l")
    elif v == 6:
        lyudi_s_odinakovoy_zarplatoi(inimesed, palgad)
    elif v == 7:
        poisk_imeni = input("Sisestage otsitava inimese nimi: ")
        zarplata = poisk_zarplaty_po_imeni(inimesed, palgad, poisk_imeni)
        if zarplata is not None:
            print(f"{poisk_imeni} saab kätte {zarplata} Eur")
        else:
            print(f"{poisk_imeni} ei ole nimekirjas")
    elif v == 8:
        порогovaya_zarplata = int(input("Sisestage пороговая_зарплата: "))
        vverh = bool(int(input("Vverh (1) või Vniz (0): ")))
        spisok_lyudey_s_zarplatami(inimesed, palgad, порогovaya_zarplata, vverh)
    elif v == 9:
        n = int(input("Kui palju inimesi näidata TOPis? "))
        top_bogatye_i_bednye(inimesed, palgad, n)


