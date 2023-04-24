# Oblicz liczbę nawiasów w zmiennej, zwroc: [otwierajace, zamykajace]

def nawiasy(tekst: str) -> [int, int]:
    otwierajace = 0
    zamykajace = 0

    for znak in tekst:
        if znak == "(":
            otwierajace += 1
        elif znak == ")":
            zamykajace += 1
        elif znak == "[":
            otwierajace += 1
        elif znak == "]":
            zamykajace += 1
        elif znak == "{":
            otwierajace += 1
        elif znak == "}":
            zamykajace += 1

    return [otwierajace, zamykajace]