def liian_pitka_rivi():
    return "Lapintiiralla (Sterna paradisaea) on eläinkunnan pisin tunnettu muuttomatka: se lentää joka vuosi pohjoiselta pesimäalueeltaan aina Etelämantereelle ja takaisin, kerryttäen vuodessa jopa 70 000- 96 000 kilometrin matkan"


def liian_syva(luvut):
    for luku in luvut:
        if luku > 0:
            if luku % 2 == 0:
                print(luku)


def liian_monta_lausetta():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    m = 12
    n = 13
    o = 14
    p = 15
    return a + b + c + d + e + f + g + h + i + j + k + m + n + o + p


def liian_monta_returnia(luku):
    if luku == 1:
        return "yksi"
    if luku == 2:
        return "kaksi"
    if luku == 3:
        return "kolme"
    return "muu"

def liian_monta_argumenttia(koko, nokka, varitys, rakenne, esiintyminen):
    return f"{koko}, {nokka}, {varitys}, {rakenne}, {esiintyminen}"