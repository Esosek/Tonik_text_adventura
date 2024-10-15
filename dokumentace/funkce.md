# Funkce

Python funkce jsou zjednodušeně obalem pro akce, které se provedou po jejím **zavolání**. Funkce se definují (vytvářejí) pomocí klíčového slova **def**. Skládají se z hlavičky a těla. Procesu vytváření funkce se říká **deklarace**.

## Deklarace

Tělo funkce musí být odsazeno (klávesa TAB).

_Příklad_

    def nazev_funkce():		// hlavička
        pass				// tělo je odsazeno jedním tabem

Můžeš deklarovat funkce s různými **parametry**, které musíš libovolně pojmenovat a říct, jaké jsou [datové struktury](./datove_struktury.md).

    def secist(a: int, b: int):	// tato funkce vyžaduje dva parametry typu int
    	pass

    def secist(a, b :int):	// můžeš použít zkrácený zápis, pokud jsou parametry stejného typu
    	pass

Funkce mohou, ale nemusí vracet **hodnotu** (například proměnnou).

    def secist(a, b: int): // funkce vrátí (return) součet obou parametrů
    	return a + b

## Volání funkci

Deklarace funkce sama o sobě nic nedělá. Aby se vykonala akce, kterou jsi funkci definoval, je potřeba funkci zavolat pomocí jejího jména a jednoduchých závorek.

    jmeno_funkce()

_Příklady volání_

    vypis_jmeno()			// volání funkce bez parametrů
    secist(2, 5)			// volání funkce s parametry
    soucet = secist(1, 2)	// výstup funkce (return) můžeš uložit do proměnné

_Příklady deklarace a volání_
Pozor! Je nutné dodržet pořadí, že nejprve funkci zadefinuješ a teprve potom zavoláš.

    def vypis_jmeno():
        print("Toník")

    vypis_jmeno()


    def secist(a, b: int):
    	return a + b

    soucet = secist(1, 2)		// hodnota proměnné soucet bude 3
