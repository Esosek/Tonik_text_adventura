# Datové struktury

## Primitives

- **Int**eger (celá čísla) – v kódu označován jako **int**
- Float (desetinná čísla) – v kódu označován jako **float**
- String (text) – v kódu označován jako **str**
- **Bool**ean (pravda / nepravda) – v kódu označován jako **bool**

### Integer

Zkráceně int se používá pro celá čísla. Stejně jako v matematice od sebe můžeš čísla přičítat, odečítat atd.

Základní matematické operace jsou

| Znaménko | Funkce    |
| -------- | --------- |
| +        | Sčítání   |
| -        | Odečítání |
| \*       | Násobení  |
| /        | Dělení    |

_Příklady_

    vek = 9
    vek = 12 - 6		// vek bude 6
    vek = 2 + vek		// vek bude 2 + 6, tedy 8
    print(vek / 2)		// vek bude 8 děleno 2, tedy 4

### Float

Platí to samé jako pro integery, ale jedná se o desetinné číslo. Desetinná čárka se píše tečkou!

_Příklad_

    moje_kousky_pizzy = 2.75

### String

Je označení pro text. Pokud chceš pracovat s textem, je potřeba ho otevřít a uzavřít uvozovkami. Můžeš použít složené i jednoduché uvozovky.

_Příklady_

    oblibeny_film = "Pán prstenů: Společenstvo Prstenu"
    oblibena_postava = 'Frodo Pytlík'

### Boolean

Zkráceně bool je datový typ, který může mít jen dvě hodnoty **True** (PRAVDA) nebo **False** (NEPRAVDA). Ten budeš používat ve hrách opravdu hodně.

Pokud ukládáš bool do proměnné, je dobrým zvykem vytvářet názvy jako otázky na které si odpovíš ano / ne.

_Příklady_

    mam_mec = True				// Mám meč
    jsem_unaveny = False		// Nejsem unavený

    nemam_mec = True			// Používat zápory v názvu je matoucí
