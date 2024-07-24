import os
import re

def poisci(stran):
    """Funkcija v HTML-datoteki strani zadetkov poišče naslov in id posamezne računalniške igre. Vrne seznam parov"""

    with open(os.path.join("Neobdelani_podatki", "Strani", f"stran{stran}.html"), "r", encoding="utf-8") as dat:
        vsebina = dat.read()

        vzorec = r'"internal_url": "https://www.mobygames.com/game/(?P<id>\d+).*?"title": "(?P<naslov>.*?)", "user_score"'
        igre = []
        for najdba in re.finditer(vzorec, vsebina):
            igre.append((najdba["naslov"], najdba["id"]))
        
    return igre
# Default je očitno 18 na stran