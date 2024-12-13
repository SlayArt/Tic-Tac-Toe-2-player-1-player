# Initialisation des plateaux
plateaux = [[".", ".", "."],
            [".", ".", "."],
            [".", ".", "."]]

def joueur1():
    j1 = "x"
    list_j1 = input("Player 1 (x), give coordinates x y: ")
    res = list_j1.split()
    res.append(j1)
    return res

def joueur2():
    j2 = "o"
    list_j2 = input("Player 2 (o), give coordinates x y: ")
    res = list_j2.split()
    res.append(j2)
    return res

def affich(tab):
    for row in tab:
        print(" ".join(row))
    print()

def verif(plateau):
    # Vérifier les lignes
    for row in plateau:
        if row[0] == row[1] == row[2] and row[0] != ".":
            return "j1" if row[0] == "x" else "j2"

    # Vérifier les colonnes
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] and plateau[0][col] != ".":
            return "j1" if plateau[0][col] == "x" else "j2"

    # Vérifier les diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] != ".":
        return "j1" if plateau[0][0] == "x" else "j2"
    if plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] != ".":
        return "j1" if plateau[0][2] == "x" else "j2"

    return None  # Aucun gagnant pour l'instant

def play(tab, x, y, sign):
    while True:
        if tab[x][y] != ".":
            print("Can't play this position, try another.")
            x, y = map(int, input("Tell new x y: ").split())
        else:
            tab[x][y] = sign
            break

def game(tab):
    affich(tab)
    idx = 0

    while idx < 9:
        # Alternance des joueurs
        if idx % 2 == 0:
            joueur_info = joueur1()
        else:
            joueur_info = joueur2()

        x, y, sign = int(joueur_info[0]), int(joueur_info[1]), joueur_info[2]

        # Jouer le coup
        play(tab, x, y, sign)

        # Afficher le plateau après chaque coup
        affich(tab)

        # Vérifier si un joueur a gagné
        winner = verif(tab)
        if winner:
            print(f"{winner} ({'x' if winner == 'j1' else 'o'}) wins! | End of the Game!")
            return

        idx += 1

    # Si on sort de la boucle, c'est un match nul
    print("Draw! | End of the Game!")

# Lancer le jeu
main_plateau = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
game(main_plateau)
