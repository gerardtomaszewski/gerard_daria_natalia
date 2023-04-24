# Policz studentki i studentow i zwroc wynik w formacie: [k, m]
# Przyjmij, ze imie dla kobiety konczy sie na "a"
def policz_studentow_plec(studenci) -> [int, int]:

    liczba_k = 0
    liczba_m = 0

    for imie in studenci:
            if imie[-1] == 'a':
                liczba_k += 1
            else:
                liczba_m += 1

    return [liczba_k, liczba_m]
