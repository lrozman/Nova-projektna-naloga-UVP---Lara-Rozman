import re
import os

def izlusci_igro(id):
    """Funkcija izlušči podatke o igri iz pridobljene HTML-strani in vrne slovar lastnosti."""

    with open(os.path.join("Neobdelani_podatki", "Igre", f'igra{id}.html'), "r", encoding="utf-8") as dat:
        vsebina = dat.read()
    

    # Izluscimo podatke o datumu izdaje.
    datum_re = re.compile(r'<dt>Released</dt>.*?<a href="/game/\S+\s*(\w+) (\d+), (\d+)\s*</a>', flags=re.DOTALL)
    najdba = datum_re.search(vsebina)
    if najdba is not None:
        m = najdba.group(1)
        meseci = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        mm = str(meseci.index(m) + 1)
        if len(mm) == 1:
            mm = "0" + mm
        dd = najdba.group(2)
        if len(dd) == 1:
            dd = "0" + dd
        yyyy = najdba.group(3)
        datum = yyyy + "/" + mm + "/" + dd
    else:
        datum_re = re.compile(r'<dt>Released</dt>.*?<a href="/game/\S+\s*.*?(\d+)\s*</a>', flags=re.DOTALL)
        najdba = datum_re.search(vsebina)
        if najdba is not None:
            datum = najdba.group(1)
        else:
            print("Napaka: datum", id)
            datum = "NG"


    # Izluscimo razvijalce in založnike.
    razvijalci = []
    devs_re1 = re.compile(r'<dt>Developers</dt>(.*?)<div class="info-score">', flags=re.DOTALL)
    najdba1 = devs_re1.search(vsebina)
    if najdba1 is not None:
        devs_re2 = re.compile(r'<a href="https://www.mobygames.com/company/(?P<id>\d+)/.*?}\'>(?P<dev>.+?)</a>')
        for najdba in devs_re2.finditer(najdba1.group(1)):
            razvijalci.append((najdba["dev"], najdba["id"]))
    else:
        print("Napaka: razvijalci", id)
    
    publishers = []
    pubs_re1 = re.compile(r'<dt>Publishers</dt>(.*?)</dd>', flags=re.DOTALL)
    najdba1 = pubs_re1.search(vsebina)
    if najdba1 is not None:
        pubs_re2 = re.compile(r'<a href="https://www.mobygames.com/company/(?P<id>\d+)/.*?}\'>(?P<pub>.+?)</a>')
        for najdba in pubs_re2.finditer(najdba1.group(1)):
            publishers.append((najdba["pub"], najdba["id"]))
    


    #Izluscimo podatke o ocenah.
    moby_re = re.compile(r'>Moby Score</span>.*?(\d\.\d)\s+</div>', flags=re.DOTALL)
    najdba = moby_re.search(vsebina)
    if najdba is not None:
        moby_score = float(najdba.group(1))
    else:
        print("Napaka: moby score", id)
        moby_score = "n/a"

    critics_re = re.compile(r'<dt>Critics</dt>.*?(\d\d)%', flags=re.DOTALL)
    najdba = critics_re.search(vsebina)
    if najdba is not None:
        critics = int(najdba.group(1))
    else:
        print("Napaka: kritiki", id)
        critics = "n/a"


    # Izluscimo podatke o žanrih ipd.
    zanri = []
    perspektiva = []
    gameplay = []
    interface = []
    setting = []
    podatki_re1 = re.compile(r'<div class="info-genres">(.*?)<div class="info-specs">', flags=re.DOTALL)
    blok = podatki_re1.search(vsebina)
    if blok is not None:
        blok = blok.group(1)
        podatki_re2 = re.compile(r'">(.*?)</a>')

        zanri_re1 = re.compile(r'<dt>Genre</dt>(.*?)</dd>', flags=re.DOTALL)
        najdba1 = zanri_re1.search(blok)
        if najdba1 is not None:
            for najdba in podatki_re2.finditer(najdba1.group(1)):
                zanri.append(najdba.group(1))
        else:
            print("Napaka: zanri", id)
        
        perspektiva_re1 = re.compile(r'<dt>Perspective</dt>(.*?)</dd>', flags=re.DOTALL)
        najdba1 = perspektiva_re1.search(blok)
        if najdba1 is not None:
            for najdba in podatki_re2.finditer(najdba1.group(1)):
                perspektiva.append(najdba.group(1))
        else:
            print("Napaka: perspektiva", id)
        
        gameplay_re1 = re.compile(r'<dt>Gameplay</dt>(.*?)</dd>', flags=re.DOTALL)
        najdba1 = gameplay_re1.search(blok)
        if najdba1 is not None:
            for najdba in podatki_re2.finditer(najdba1.group(1)):
                gameplay.append(najdba.group(1))                                # Beat 'em up je problem zaradi apostrofa.
        else:
            print("Napaka: gameplay", id)  
        
        interface_re1 = re.compile(r'<dt>Interface</dt>(.*?)</dd>', flags=re.DOTALL)
        najdba1 = interface_re1.search(blok)
        if najdba1 is not None:
            for najdba in podatki_re2.finditer(najdba1.group(1)):
                interface.append(najdba.group(1))
        else:
            print("Napaka: interface", id)         

        setting_re1 = re.compile(r'<dt>Setting</dt>(.*?)</dd>', flags=re.DOTALL)
        najdba1 = setting_re1.search(blok)
        if najdba1 is not None:
            for najdba in podatki_re2.finditer(najdba1.group(1)):
                setting.append(najdba.group(1))
        else:
            print("Napaka: setting", id) 



    # Izluscimo podatek o oznaki.
    oznaka_re = re.compile(r'Rating</dt>.*?">(.*?)</a>', flags=re.DOTALL)
    najdba = oznaka_re.search(vsebina)
    if najdba is not None:
        oznaka = najdba.group(1)
    else:
        print("Napaka: oznaka", id)
        oznaka = "NG"

    
    
    # Izluscimo podatka o tipu medija in podprtih vhodnih napravah.
    mediji = []
    media_re1 = re.compile(r'<dt>Media Type</dt>(.*?)</dd>', flags=re.DOTALL)
    najdba1 = media_re1.search(vsebina)
    if najdba1 is not None:
        for najdba in podatki_re2.finditer(najdba1.group(1)):  # Isti regex kot je uporabljen pri žanrih ipd.
            mediji.append(najdba.group(1))
    else:
        print("Napaka: mediji", id)
    
    input = []
    input_re1 = re.compile(r'<dt>Input Devices Supported/Optional</dt>(.*?)</dd>', flags=re.DOTALL)
    najdba1 = input_re1.search(vsebina)
    if najdba1 is not None:
        for najdba in podatki_re2.finditer(najdba1.group(1)):
            input.append(najdba.group(1))
    else:
        print("Napaka: input", id)    



    # Izluscimo podatke o eno- in večigralskih načinih igre.
    multiplayer = []
    multiplayer_re = re.compile(r'<dt>Multiplayer Options</dt>(.*?)</dd>', flags=re.DOTALL)
    najdba1 = multiplayer_re.search(vsebina)
    if najdba1 is not None:
        for najdba in podatki_re2.finditer(najdba1.group(1)):
            multiplayer.append(najdba.group(1))
    else:
        print("Napaka: multiplayer", id)          

    offline_re = re.compile(r'<dt>Number of Offline Players</dt>.*?">(\d+-?\d*?) Player', flags=re.DOTALL)
    najdba1 = offline_re.search(vsebina)
    if najdba1 is not None:
        st_offline = najdba1.group(1)
    else:
        st_offline = "NG"
        print("Napaka: st_offline", id)

    online_re = re.compile(r'<dt>Number of Online Players</dt>.*?">(\d+-?\d*?) Player', flags=re.DOTALL)
    najdba2 = online_re.search(vsebina)  
    if najdba2 is not None:
        st_online = najdba2.group(1)
    else:
        st_online = "NG"
        print("Napaka: st_online", id)
    

    # Izluscimo podatek o ceni.
    cene_used = []
    cene_new = []
    cena = "/"
    cena_re = re.compile(r'$(?P<cena>\d+\.\d+) (?P<stanje>)\w+\b')
    if cena_re.search(vsebina) is not None:
        for najdba in cena_re.finditer(vsebina):
            if najdba["stanje"] == "new":
                cene_new.append(float(najdba["cena"]))
            if najdba["stanje"] == "used":
                cene_used.append(float(najdba["cena"]))
        if cene_new:
            cena = "$" + str(min(cene_new)) + "new"
        elif cene_used:
            cena = "$" + str(min(cene_used)) + "used"




    return {
        "datum izdaje": datum,
        "razvijalci": razvijalci,
        "založniki": publishers,
        "Moby ocena": moby_score,
        "Ocena kritikov": critics,
        "žanri": zanri,
        "perspektiva": perspektiva,
        "gameplay": gameplay,
        "interface": interface,
        "setting": setting,
        "oznaka": oznaka,
        "tip medija": mediji,
        "vhodne naprave": input,
        "večigralski načini": multiplayer,
        "št. offline igralcev": st_offline,
        "št. online igralcev": st_online,
        "cena": cena
    }


# Ali naj izluščim tudi kakšne podatke o razvijalcih posebej? Kaj bi to lahko sploh bili?
# Problema: Kateri podatki so na voljo? Nekateri studii imajo 12 vnosov, nekateri 40 tisoč.
