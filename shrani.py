import csv

def shrani(podatki):
    with open("igre.csv", "w", encoding="utf-8") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "id",
                "naslov",
                "datum izdaje",
                "razvijalci",
                "založniki",
                "Ocena uporabnikov",
                "Moby ocena",
                "Ocena kritikov",
                "žanri",
                "perspektiva",
                "gameplay",
                "interface",
                "setting",
                "oznaka",
                "tip medija",
                "vhodne naprave",
                "večigralski načini",
                "št. offline igralcev",
                "št. online igralcev"
            ]
        )
        for podatek in podatki:
            pisatelj.writerow(
                [
                    podatek["id"],
                    podatek["naslov"],
                    podatek["datum izdaje"],
                    podatek["razvijalci"],
                    podatek["založniki"],
                    podatek["Ocena uporabnikov"],
                    podatek["Moby ocena"],
                    podatek["Ocena kritikov"],
                    podatek["žanri"],
                    podatek["perspektiva"],
                    podatek["gameplay"],
                    podatek["interface"],
                    podatek["setting"],
                    podatek["oznaka"],
                    podatek["tip medija"],
                    podatek["vhodne naprave"],
                    podatek["večigralski načini"],
                    podatek["št. offline igralcev"],
                    podatek["št. online igralcev"]
                ]
            )
    

    # Še ne vem, za kaj oziroma ali bom potrebovala spodnje csv-tabele.

    with open("igre_zanri.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id", "zanr"])
        for podatek in podatki:
            for zanr in podatek["žanri"]:
                pisatelj.writerow([podatek["id"], zanr])
    

    with open("igre_devs.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_razvijalca", "id_igre"])
        for podatek in podatki:
            for dev in podatek["razvijalci"]:
                pisatelj.writerow([podatek["id"], dev[1]])
    

    with open("igre_pubs.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_založnika", "id_igre"])
        for podatek in podatki:
            for pub in podatek["založniki"]:
                pisatelj.writerow([podatek["id"], pub[1]])