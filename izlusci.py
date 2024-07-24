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
        print("Napaka: datum", id)


    # Izluscimo razvijalce.
    razvijalci = []
    devs_re1 = re.compile(r'<dt>Developers</dt>(.*?)<div class="info-score">', flags=re.DOTALL)
    najdba1 = devs_re1.search(vsebina)
    if najdba1 is not None:
        devs_re2 = re.compile(r'<a href="https://www.mobygames.com/company/(?P<id>\d+)/.*?}\'>(?P<dev>.+?)</a>')
        for najdba in devs_re2.finditer(najdba1.group(1)):
            razvijalci.append((najdba["dev"], najdba["id"]))
    else:
        print("Napaka: razvijalci", id)
    


    #Izluscimo podatke o ocenah.
    moby_re = re.compile(r'>Moby Score</span>.*?(\d\.\d)\s+</div>', flags=re.DOTALL)
    najdba = moby_re.search(vsebina)
    if najdba is not None:
        moby_score = float(najdba.group(1))
    else:
        print("Napaka: moby score", id)

    critics_re = re.compile(r'<dt>Critics</dt>.*?(\d\d)%', flags=re.DOTALL)
    najdba = critics_re.search(vsebina)
    if najdba is not None:
        critics = int(najdba.group(1))
    else:
        print("Napaka: kritiki", id)


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


    return {
        "datum izdaje": datum,
        "razvijalci": razvijalci,
        "Moby ocena": moby_score,
        "Ocena kritikov": critics,
        "žanri": zanri,
        "perspektiva": perspektiva,
        "gameplay": gameplay,
        "interface": interface,
        "setting": setting,
    }
