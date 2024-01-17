spiel_aktiv = True
aktiver_spieler = None
spielfeld = ['1','2','3','4','5','6','7','8','9']

def spielfeld_ausgeben():
    print(spielfeld[0], '|', spielfeld[1], '|', spielfeld[2])
    print(spielfeld[3], '|', spielfeld[4], '|', spielfeld[5])
    print(spielfeld[6], '|', spielfeld[7], '|', spielfeld[8])


def spieler_eingabe():
    while True:
        global spiel_aktiv
        spielzug = input('Wähle ein Feld aus: ')

        if spielzug.lower() == 'q':
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print('Zahl von 1 bis 9 eingeben')
        else:
            if spielzug >= 1 and  spielzug <= 9:
                if spielfeld[spielzug -1] == 'X' or spielfeld[spielzug -1] == 'O':#-1 weil der index 0-8 ist
                    print('Diese Feld ist bereits belegt')
                else:
                    return spielzug
            else:
                print('Zahl von 1 bis 9 eingeben')



def spieler_auswahl():
    spieler = input('Wähle aus, (x) für X oder (o) für O: ')
    if spieler.lower() == 'x':
        print('Du hast X')
        return 'X', 'O'
    elif spieler.lower() == 'o':
        print('Du hast O')
        return 'O', 'X'
    else:
        print('Ungültige Eingabe. Bitte wähle (x) für X oder (o) für O.')
        return  spieler_auswahl()
    


spieler1, spieler2 = spieler_auswahl()
aktiver_spieler = spieler1

def check_gewinn():
    # Horizontale Gewinnmuster überprüfen
    for i in range(0, 9, 3):
        if spielfeld[i] == spielfeld[i + 1] == spielfeld[i + 2] == 'X':
            print('X hat gewonnen')
            return True
        elif spielfeld[i] == spielfeld[i + 1] == spielfeld[i + 2] == 'O':
            print('O hat gewonnen')
            return True

    # Vertikale Gewinnmuster überprüfen
    for i in range(3):
        if spielfeld[i] == spielfeld[i + 3] == spielfeld[i + 6] == 'X':
            print('X hat gewonnen')
            return True
        elif spielfeld[i] == spielfeld[i + 3] == spielfeld[i + 6] == 'O':
            print('O hat gewonnen')
            return True

    # Diagonale Gewinnmuster überprüfen
    if spielfeld[0] == spielfeld[4] == spielfeld[8] == 'X' or spielfeld[2] == spielfeld[4] == spielfeld[6] == 'X':
        print('X hat gewonnen')
        return True
    elif spielfeld[0] == spielfeld[4] == spielfeld[8] == 'O' or spielfeld[2] == spielfeld[4] == spielfeld[6] == 'O':
        print('O hat gewonnen')
        return True

    return False

spieler1, spieler2 = spieler_auswahl()
aktiver_spieler = spieler1

def check_unentschieden():
    return all(cell == 'X' or cell == 'O' for cell in spielfeld)

while spiel_aktiv:
    spielfeld_ausgeben()
    if check_gewinn():
        print('Spiel beendet.')
        break
    if check_unentschieden():
        print('Unentschieden! Das Spielfeld ist voll.')
        break
    spielzug = spieler_eingabe()

    if spielzug is not None:
        spielfeld[spielzug - 1] = aktiver_spieler
        if aktiver_spieler == spieler1:
            aktiver_spieler = spieler2
        else:
            aktiver_spieler = spieler1
