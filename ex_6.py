# sprawdz, czy nawias ma swoja pare, jesli ma swroc True, jesli nie False

def para_nawiasow(tekst: str) -> bool:
    stos = []
    nawiasy = {"(": ")", "[": "]", "{": "}"}
    for znak in tekst:
        if znak in nawiasy:
            stos.append(nawiasy[znak])
        elif znak in nawiasy.values():
            if not stos or znak != stos.pop():
                return False
    return not stos