import pridobi
import poisci_igre
import izlusci
import shrani

stevilo_strani = 7626
# Če je default 18 zadetkov na stran, je število strani 7626. 
# Če je default 50 (to je največ), je število strani 2746, če pa 12 (to je najmanj), pa 11439. 

#pridobi.pridobi_strani(stevilo_strani)
# Že pridobljeno.

vse_igre = []
for stran in range(1, stevilo_strani + 1):
    igre = poisci_igre.poisci(stran)
    vse_igre.extend(igre)

vsi_podatki = []
ids = set()
for igra in vse_igre:
    id = igra[1]
    if id in ids:
        continue
    naslov = igra[0]
    user_score = igra[2]
    pridobi.pridobi_igro(id)
    podatki = izlusci.izlusci_igro(id)
    podatki["id"] = id
    podatki["naslov"] = naslov
    podatki["Ocena uporabnikov"] = user_score
    vsi_podatki.append(podatki)
    print(len(vsi_podatki), "/", len(vse_igre), id)
    ids.add(id)

shrani.shrani(vsi_podatki)