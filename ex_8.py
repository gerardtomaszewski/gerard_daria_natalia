# dla podanych dwoch punktow, oblicz, czy funkcja liniowa jest rozsnaca, czy malejaca
# dla niemalejacej zrwoc True
# dla malejacej zwroc False

def funkcja_liniowa(punkty) -> bool:
    
    posortowane_punkty = sorted(punkty, key=lambda x: x[0])
    y1=posortowane_punkty[0][1]
    y2=posortowane_punkty[1][1]
    
    if y2>y1:
        return True
    else:
        return False
