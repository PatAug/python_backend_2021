import random

s_x = random.randint(1, 10)
s_y = random.randint(1, 10)
print("Skarb", s_x, s_y)

g_x = random.randint(1, 10)
g_y = random.randint(1, 10)


def odl(a, b, c, d):
    return abs(a - b) + abs(c - d)


odleglosc = odl(s_x, g_x, s_y, g_y)
# abs(S_x - G_x) + abs(S_y - G_y)
print("Gracz", g_x, g_y, odleglosc)

krok=0
while not (g_x == s_x and s_y == g_y):
    ruch = input('Podaj ruch G D P L:')
    # G D P L

    if ruch.upper() == 'G' and g_y <= 10 and g_x <= 10:
        g_y += 1
    elif ruch.upper() == 'D' and g_y <= 10 and g_x <= 10:
        g_y += -1
    elif ruch.upper() == 'P' and g_x <= 10 and g_y <= 10:
        g_x += 1
    elif ruch.upper() == 'L' and g_x <= 10 and g_y <= 10:
        g_x += -1
    else:
        print("jestes poza plansza!")
        continue
    krok += 1
    test = odl(s_x, g_x, s_y, g_y)
    if test < odleglosc:
        print("dobrze idzie! ", g_x, g_y)
    elif test > odleglosc:
        print("Oddalasz sie", g_x, g_y)

    print(f"Wygrales!! Liczba krokow {krok}")
    if krok >2*odleglosc:
        s_x = random.randint(1, 10)
        s_y = random.randint(1, 10)
        odleglosc = odl(s_x, g_x, s_y, g_y)
        krok=0
