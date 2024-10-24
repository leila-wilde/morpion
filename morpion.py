print('\n\n\t','Bienvenue sur le jeu de morpion !')
print('\n\t    ','BONNE CHANCE AUX JOUEURS','\n\n')

# Fonction qui imprime morpion
def print_morpion(values):
    print('\n')
    print('\t     . . . . . . . . . . . . .')
    print('\t     .   _________________   .')
    print('\t     .  |     |     |     |  .')
    print('\t     .  |  {}  |  {}  |  {}  |  .'.format(values[0], values[1], values[2]))
    print('\t     .  |_____|_____|_____|  .')
    print('\t     .  |     |     |     |  .')
    print('\t     .  |  {}  |  {}  |  {}  |  .'.format(values[3], values[4], values[5]))
    print('\t     .  |_____|_____|_____|  .')
    print('\t     .  |     |     |     |  .')
    print('\t     .  |  {}  |  {}  |  {}  |  .'.format(values[6], values[7], values[8]))
    print('\t     .  |_____|_____|_____|  .')
    print('\t     .                       .')
    print('\t     . . . . . . . . . . . . .')
    print('\n')

# Fonction qui imprime le scoreboard
def print_scoreboard(score_board):
    print('\t  ********************************')
    print('\t             SCOREBOARD           ')
    print('\t  ********************************')
 
    players = list(score_board.keys())
    print('\t     ', players[0], '\t\t    ', score_board[players[0]])
    print('\t     ', players[1], '\t\t    ', score_board[players[1]])
 
    print('\t  --------------------------------\n')
 
# Fonction pour vérifier si un joueur a gagné
def check_win(player_pos, cur_player):
 
    # Toutes les combinaisons gagnantes possibles
    win_conditions = [
          [1, 2, 3], [4, 5, 6], [7, 8, 9], #lignes
          [1, 4, 7], [2, 5, 8], [3, 6, 9], #colonne
          [1, 5, 9], [3, 5, 7]             #diagonal
          ]
 
    # Boucle pour vérifier si une combinaison gagnante est satisfaite
    for x in win_conditions:
        if all(y in player_pos[cur_player] for y in x):
 
            # Retourne True si une combinaison gagnante satisfait
            return True
    # Retourne False si aucune combinaison n'est satisfaite       
    return False       
 
# Fonction qui vérifie si le jeu est à égalité
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Fonction pour un seul jeu de morpion
def single_game(cur_player):
 
    # Représente le jeu de morpion
    values = [' ' for x in range(9)]
     
    # Stocke les positions occupées par X et O
    player_pos = {'X':[], 'O':[]}
     
    # Boucle de jeu pour un seul jeu de morpion
    while True:
        print_morpion(values)
         
        # Try exception block pour MOVE input
        try:
            print('Player', cur_player, 'écrit un chiffre pour placer ton symbole entre (1-9) : ', end="")
            move = int(input()) 
        except ValueError:
            print('\nOption invalid réssaye')
            continue
 
        # Sanity check pour MOVE input
        if move < 1 or move > 9:
            print('\nOption invalid, veuilles entrer un chiffre entre 1 et 9')
            continue
 
        # Vérifier si la carré n'est pas déjà occupé
        if values[move-1] != ' ':
            print('\nCet emplacement est déjà pris, réssaye !')
            continue
 
        # Mise à jour des informations sur le jeu
 
        # Mise à jour de l'état de la grille 
        values[move-1] = cur_player
 
        # Mise à jour des positions des joueurs
        player_pos[cur_player].append(move)
 
        # Appel de fonction pour vérifier de jeu gagnant
        if check_win(player_pos, cur_player):
            print_morpion(values)
            print('Player', cur_player, 'à gagner !!')     
            print('\n')
            return cur_player
 
        # Appel de fonction pour vérification de jeu égal
        if check_draw(player_pos):
            print_morpion(values)
            print('Égalité')
            print('\n')
            return 'É'
 
        # Changement de joueurs
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


if __name__ == '__main__':
    
    
 
    print('Player 1')
    player1 = input('Entre le nom : ').strip().title()
    print('\n')
 
    print('Player 2')
    player2 = input('Entre le nom : ').strip().title()
    print('\n')
     
    # Stocke le joueur qui choisit X et O
    cur_player = player1
 
    # Stocke le choix des joueurs
    player_choice = {'X' : "", 'O' : ""}
 
    # Stocke les options
    options = ['X', 'O']
 
    # Stocke le scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # Boucle de jeu pour une série de morpion
    # La boucle continue jusqu'à ce que les joueurs quittent le jeu 
    while True:
 
        # Choix du joueur Menu
        print('Salut', cur_player, 'choisissez « X » ou « O »')
        print('\n\t     jouer comme « X » entre 1')
        print('\t     jouer comme « O » entre 2')
        print('\t          pour sortir, entre 3\n')
 
        # Try exception pour l'entrée CHOICE
        try:
            choice = int(input())
        except ValueError:
            print('Option invalid, réssaye\n')
            continue
 
        # Conditions pour le choix du joueur
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print('\nScore final\n')
            print_scoreboard(score_board)
            break  
 
        else:
            print('Option invalid, réssaye\n')
 
        # Stocke le gagnant d'un seul jeu de morpion
        winner = single_game(options[choice-1])
         
        # Modifie le scoreboard en accord avec le gagnant
        if winner != 'É' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        
        # Changement de joueur qui choisit X ou O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1