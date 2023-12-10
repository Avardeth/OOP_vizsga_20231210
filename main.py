from abc import ABC
from datetime import datetime


class Bicikli(ABC):
    def __init__(self, tipus, ar, allapot, cimke):
        self.tipus = tipus
        self.ar = ar
        self.allapot = allapot
        self.cimke = cimke


class Orszagutibicikli(Bicikli):
    def __init__(self, ar, allapot, cimke):
        self.tipus = "Országúti"
        super().__init__(self.tipus, ar, allapot, cimke)


class HegyiBicikli(Bicikli):
    def __init__(self, ar, allapot, cimke):
        self.tipus = "Hegyi"
        super().__init__(self.tipus, ar, allapot, cimke)


class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.biciklik: [HegyiBicikli | Orszagutibicikli] = [
            HegyiBicikli(100, "Jó", "Hegyi 1"),
            HegyiBicikli(90, "Megfelelő", "Hegyi 2"),
            HegyiBicikli(70, "Rossz", "Hegyi 3"),
            Orszagutibicikli(120, "Kiválló", "Országúti 1"),
            Orszagutibicikli(90, "Jó", "Országúti 2"),
            Orszagutibicikli(100, "Jó", "Országúti 3")
        ]

    def listazas(self):
        l: HegyiBicikli | Orszagutibicikli
        for i, l in enumerate(self.biciklik):
            print(f"[{i + 1}] Név: {l.cimke}, állapot: {l.allapot}, ár: {l.ar} Ft")


class Kolcsonzes:
    def __init__(self):
        self.kolcsonzo = Kolcsonzo("Tuti bicikli kölcsönző")
        self.foglalasok = [
            {"nap": "2024-01-21", "bckl": "Hegyi 1"},
            {"nap": "2024-01-01", "bckl": "Országúti 2"},
            {"nap": "2024-01-01", "bckl": "Országúti 3"}
        ]

    def kolcsonzes(self, nap: datetime, bckl_szam: int) -> int:
        today = datetime.now().date()
        if today > nap.date():
            print("Sajnos a foglalás nem lehetséges mivel egy már elmúlt dátumot adott meg.")
            return -1
        bckl: HegyiBicikli | Orszagutibicikli = self.kolcsonzo.biciklik[bckl_szam]
        for item in self.foglalasok:
            if item["nap"] == nap and item["cimke"] == bckl.cimke:
                print("Sajnos a bicikli foglalása nem lehetséges erre a napra.")
                return -1
        self.foglalasok.append({"nap": str(nap.date()), "bckl": bckl.cimke})
        return bckl.ar

    def lemondas(self, index: int):
        lemond = self.foglalasok[index]
        today = datetime.now().date()
        if today > datetime.strptime(lemond['nap'], "%Y-%m-%d"):
            print("Sajnos ennek a foglalásnak a lemondása már nem lehetséges.")
            return
        self.foglalasok.remove(lemond)
        print("A lemondás sikeresen megtörtént.")

    def listazas(self):
        for f in self.foglalasok:
            print(f"Bicikli neve: {f["bckl"]}, foglalás napja: {f["nap"]}")


if __name__ == '__main__':
    kolcsonzes = Kolcsonzes()
    while True:
        print("Kérem válasszon az alábbi lehetőségek közül:")
        print("\t[1]Kölcsönzés")
        print("\t[2]Lemondás")
        print("\t[3]Listázás")
        print("\t[4]Kilépés")
        i = input()

        if i.lower() == "kilépés" or i == "4":
            break
        elif i.lower() == "listázás" or i == "3":
            kolcsonzes.listazas()
        elif i.lower() == "lemondás" or i == "2":
            print("Kérem válasszon az alábbiak közül:")
            for i, f in enumerate(kolcsonzes.foglalasok):
                print(f"[{i + 1}] Bicikli neve: {f["bckl"]}, foglalás napja: {f["nap"]}")
            lemondas = input()
            kolcsonzes.lemondas(int(lemondas))
        elif i.lower() == "kölcsönzés" or i == "1":
            while True:
                print("Kérem válassszon az alábbi biciklik közül:")
                kolcsonzes.kolcsonzo.listazas()
                try:
                    bckl_szam = int(input())
                    if bckl_szam > len(kolcsonzes.kolcsonzo.biciklik):
                        print("Kérem egy valós számot adjon meg!")
                        continue
                except ValueError:
                    print("Kérem egy valós számot adjon meg!")
                    continue

                print("Kérem adja meg a foglalás dátumát (formátum: YYYY-MM-DD, pl: 2023-01-11)")
                try:
                    nap = datetime.strptime(input(), "%Y-%m-%d")
                except ValueError:
                    print("Érvénytelen dátum formátum.")
                    continue

                res = kolcsonzes.kolcsonzes(nap, bckl_szam - 1)
                if res == -1:
                    continue
                print(f"A foglalás sikeresen megtörtént. A foglalás ára {res} Ft")
                break
