# GDE Objektumorintentált szoftverfejlesztés VIZSGA 2023.12.10 14:00-17:00

Ez a 2023.12.10-i vizsga feladat
A megoldásra 3 órátok van. A vizsga 14:00-17:00-ig tart.
A github-on lévő utolsó commit nem lehet 17:00 után. Csak az azelőtti utolsó commmit-ot veszem figyelembe az értékelésnél.


## Általános elvárások
- Pythonban készítsétek a vizsgafeladatot
- a "tesztkerdesek.txt"-t töltsétek le, és tegyétek bele a Python projektetekbe
- a "tesztkerdesek.txt"-ben töltsétek ki a neveteket, szakotokat és neptun kódotokat, ílletve írjátok be a helyes válaszokat
- kész projektet osszátok meg a saját github repositorytokba PUBLIC-ra
- 3 órátok van a feladat megoldására, és github-ra való push-olására
- hogy biztos legyen, a végén egy browser incognito ablakában nézzétek meg az elküldendő github repositoryt (látható, fent van az utolsó commit is)
- a feladat elvégzése végén küldjétek el nekem email-ben a boga.aron@gde.hu címre a github repositorytok url-jét



## 1. A tesztkérdések (35%)

A válasz helyre írjátok be a helyes választ. Jó válasz 1 pont, rossz válasz -1 pont, nincs válasz 0 pont.

## 2. Programozási feladat (65%)

Fejlessz egy egyszerű biciklikölcsönző rendszert Pythonban. A rendszernek képesnek kell lennie biciklik kezelésére, kölcsönzések kezelésére, létrehozására és lemondására, valamint a kölcsönzések listázására és egyéb kapcsolódó szolgáltatások kezelésére.

### Feladatok

#### Osztályok Létrehozása 

- Bicikli absztrakt osztály létrehozása alap attribútumokkal (pl. típus, ár, állapot). (5 pont)
- Különböző típusú biciklik (pl. OrszágútiBicikli, HegyiBicikli) leszármaztatott osztályok létrehozása. (5 pont)
- Kölcsönző osztály létrehozása, amely több Bicikli objektumot tartalmaz, és saját attribútumokkal rendelkezik (pl. név). (10 pont)
- Kölcsönzés osztály létrehozása a biciklik kölcsönzésének kezelésére. (10 pont)

#### Foglalások Kezelése

- Biciklik kölcsönzésének lehetősége egy adott napra, a kölcsönzés árának kiszámításával. (15 pont)
- Kölcsönzések lemondásának lehetősége. (5 pont)
- Kölcsönzések listázásának lehetősége. (5 pont)

#### Felhasználói Interfész és adatvalidáció
- Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. kölcsönzés, lemondás, listázás). (20 pont)

- A kölcsönzés létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni vagy aznapi) és a bicikli elérhető-e akkor. (10 pont)
- Biztosítsd, hogy a lemondások csak létező és jövőbeni foglalásokra lehetségesek. (5 pont)
- Töltsd fel az futtatás után a rendszert tesztadatokkal (1 kölcsönző, több bicikli, néhány kölcsönzés) a felhasználói interakció előtt. (10 pont)

Jó munkát! Légyszi önálló munkában, internettel...