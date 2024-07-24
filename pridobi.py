import os
import requests

def pridobi_strani(stevilo_strani):

    headers = {"User-agent": "Chrome/124.0.6367.202"}

    for stran in range(7620, stevilo_strani + 1):
        url = f'https://www.mobygames.com/game/sort:moby_score/page:{stran}/'

        odgovor = requests.get(url, headers=headers)
        if odgovor.status_code != 200:
            print("Napaka", stran, odgovor.status_code)
            return
        
        with open(os.path.join("Neobdelani_podatki", "Strani", f"stran{stran}.html"), "w", encoding="utf-8") as dat:
            dat.write(odgovor.text)


def pridobi_igro(id):

    headers = {"User-agent": "Chrome/124.0.6367.202"}

    url = f'https://www.mobygames.com/game/{id}/'

    odgovor = requests.get(url, headers=headers)
    if odgovor.status_code != 200:
        print("Napaka", id, odgovor.status_code)
        return
    
    with open(os.path.join("Neobdelani_podatki", "Igre", f"igra{id}.html"), "w", encoding="utf-8") as dat:
        dat.write(odgovor.text)
