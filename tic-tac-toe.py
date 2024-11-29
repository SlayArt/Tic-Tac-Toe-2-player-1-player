plateaux = [[".", ".", "."],
			[".", ".", "."],
			[".", ".", "."]]
plateaux_temp = [[".", ".", "."],
				[".", ".", "."],
				[".", ".", "."]]

def joueur1():
	j1 = "x"
	list_j1 = input("player1 tell x y : ")
	res = list_j1.split()
	res.append(j1)
	return res

def joueur2():
	j2 = "o"
	list_j2 = input("player2 tell x y : ")
	res = list_j2.split()
	res.append(j2)
	return res

def affich(tab):
	for c in range(len(tab)):
		for l in range(len(tab[c])):
			print(tab[c][l],end=" ")
		print()

def verif(plateau):
	if plateau[0][0] == "x" and plateau[0][1] == "x" and plateau[0][2] == "x":
		return "j1"
	elif plateau[0][0] == "o" and plateau[0][1] == "o" and plateau[0][2] == "o":
		return "j2"
	elif plateau[1][0] == "x" and plateau[1][1] == "x" and plateau[1][2] == "x":
		return "j1"
	elif plateau[1][0] == "o" and plateau[1][1] == "o" and plateau[1][2] == "o":
		return "j2"
	elif plateau[2][0] == "x" and plateau[2][1] == "x" and plateau[2][2] == "x":
		return "j1"
	elif plateau[2][0] == "o" and plateau[2][1] == "o" and plateau[2][2] == "o":
		return "j2"
	elif plateau[0][0] == "x" and plateau[1][1] == "x" and plateau[2][2] == "x":
		return "j1"
	elif plateau[0][0] == "o" and plateau[1][1] == "o" and plateau[2][2] == "o":
		return "j2"
	elif plateau[0][2] == "x" and plateau[1][1] == "x" and plateau[2][0] == "x":
		return "j1"
	elif plateau[0][2] == "o" and plateau[1][1] == "o" and plateau[2][0] == "o":
		return "j2"

def play(tab, x, y, sign):
	play = False
	while play == False:
		if tab[x][y] != ".":
			print("can't play this position try an other")
		else:
			plateaux_temp[x][y] = sign
			play = True
	
	return plateaux_temp

def rounds(tab, idx):
	plateaux = tab
	plateaux_temp = plateaux
	idx = idx

	if idx < 9:
		joueur1_list = joueur1()
		x1, y1, sign = int(joueur1_list[0]), int(joueur1_list[1]), joueur1_list[2]
		plateaux_temp = play(plateaux, x1, y1, sign)
		affich(plateaux)
		print("==>")
		affich(plateaux_temp)
		plateaux = plateaux_temp
		verif(plateaux)

		idx += 1
	else: return False

	if idx < 9:
		joueur2_list = joueur2()
		x2, y2, sign = int(joueur2_list[0]), int(joueur2_list[1]), joueur2_list[2]
		play(plateaux, x2, y2, sign)
		affich(plateaux)
		print("==>")
		affich(plateaux_temp)
		plateaux = plateaux_temp
		verif(plateaux)

		idx += 1
	else: return False

	return plateaux, verif, idx

def game(tab):
	idx = 0
	while idx < 9:
		print(idx)
		rounds(tab, idx)
		statement = verif(tab)
		if statement == "j1":
			print("j1 (x) win ! | End of the Game !")
			idx = 9
		elif statement == "j2":
			print("j2 (o) win ! | End of the Game !")
			idx = 9
		elif rounds(tab, idx) == False:
			print("Draw ! | End of the Game !")
			idx = 9
		idx += 1


def main_func(tab):
	affich(tab)
	idx = 0
	plateau = tab
	game(plateau)

main_func(plateaux)

