###############################################
# VARIABLES THAT CAN BE CHANGED BY THE PLAYER #
###############################################
GAME_FPS = 120 # Change this number to change the base framerate of the Game
# Should work, though I did not try everywhere on the game so idk
# Most animations uses the frame count as a way to reper the time, I tried to make the calculation "universal" but it might be a little bit broken in some aeras

# Importation des dépendances

import pyxel

# Importation des scripts du jeu

import game_character # Script pour les déplacements et apparence du personnage
import game_utils # Script pour des fonctions générales
import game_map # Script pour des fonctions en rapport avec la gestion des cartes etc.
import game_enemies # Script qui gère l'apparition et le combat avec les enemis
import game_save # Script qui gère la sauvegarde

# Jeu

pyxel.init(256,144,title="Jeu",fps=GAME_FPS) # Initialisation de la fenêtre, 256x144px à 120FPS
# pyxel.load("res.pyxres")
pyxel.mouse(True)

map = "test_map"

current_collision_map = game_map.get_map(map)[1] # Liste contenant la map de collision

# [Temp] Tests

# print(game_map.get_map(map)[2])
print(game_map.read_collision_map(current_collision_map)) # [0][0][0]
print(game_enemies.get_enemy(game_map.read_collision_map(current_collision_map)[0][2][0]))

print(game_map.read_collision_map(current_collision_map)[0][2][4])

compteur_test = 0

# Fonctionnement du jeu

def update():
    game_character.bouger_personnage(current_collision_map)
    if pyxel.btnr(pyxel.KEY_M):
        game_save.sauvegarder_partie(0, map, game_character.trouver_position_joueur(current_collision_map)["x"], game_character.trouver_position_joueur(current_collision_map)["y"])

# draw() : Affichage à l'écran, fonction utilisée pour afficher des objets sur l'écran

def draw():
    global compteur_test

    pyxel.cls(0)
    game_character.afficher_personnage(current_collision_map)

    # Enemies management
    # A map cannot contain more than 3 enemies at once, call it a technical limitation lol (just easier for me, maybe adding more enemies at once later if i'm not lazy af)

    if not game_map.read_collision_map(current_collision_map)[0][0] == []: # Si un premier ennemi a été trouvé (si la liste d'info du premier enemi n'est pas vide)

        # Récupération des infos du premier ennemi

        enemy_1_id = game_map.read_collision_map(current_collision_map)[0][0][0]
        enemy_1_x = game_map.read_collision_map(current_collision_map)[0][0][2]
        enemy_1_y = game_map.read_collision_map(current_collision_map)[0][0][3]

        game_enemies.draw_enemy(enemy_1_id, enemy_1_x, enemy_1_y) # Afficher l'ennemi d'ID et aux coordonées précedemment récupérés
        print("Enemy 1 detects Player :", game_enemies.is_player_in_enemy_line(game_map.read_collision_map(current_collision_map)[0][0][4], current_collision_map))
    

        if not game_map.read_collision_map(current_collision_map)[0][1] == []: # Même logique que pour les tests précédents, mais avec les ennemis 2 puis 3

            enemy_2_id = game_map.read_collision_map(current_collision_map)[0][1][0]
            enemy_2_x = game_map.read_collision_map(current_collision_map)[0][1][2]
            enemy_2_y = game_map.read_collision_map(current_collision_map)[0][1][3]

            game_enemies.draw_enemy(enemy_2_id, enemy_2_x, enemy_2_y)
            print("Enemy 2 detects Player :", game_enemies.is_player_in_enemy_line(game_map.read_collision_map(current_collision_map)[0][1][4], current_collision_map))

            if not game_map.read_collision_map(current_collision_map)[0][2] == []:
                
                enemy_3_id = game_map.read_collision_map(current_collision_map)[0][2][0]
                enemy_3_x = game_map.read_collision_map(current_collision_map)[0][2][2]
                enemy_3_y = game_map.read_collision_map(current_collision_map)[0][2][3]

                game_enemies.draw_enemy(enemy_3_id, enemy_3_x, enemy_3_y)
                print("Enemy 3 detects Player :", game_enemies.is_player_in_enemy_line(game_map.read_collision_map(current_collision_map)[0][2][4], current_collision_map))

pyxel.run(update,draw)