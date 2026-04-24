import pyxel
from datetime import datetime

def trouver_position_joueur(current_collision_map):
    for i in range(len(current_collision_map)):  # i = y
        for j in range(len(current_collision_map[i])):  # j = x
            if current_collision_map[i][j] == "P":  # Position du joueur sur la carte
                return {
                    "x":j,
                    "y":i
                }  # Le joueur se trouve en x = j et y = i dans le système de coordonées du jeu (x_max = 15, y_max = 8)

def afficher_personnage(current_collision_map):
    pyxel.rect(trouver_position_joueur(current_collision_map)["x"] * 16, trouver_position_joueur(current_collision_map)["y"] * 16, 16, 16, 7)

def bouger_personnage(current_collision_map):
    position_joueur_x = trouver_position_joueur(current_collision_map)["x"]
    position_joueur_y = trouver_position_joueur(current_collision_map)["y"]

    # Gauche

    if pyxel.btnr(pyxel.KEY_Q): # Si le joueur appuie sur Q / A / Left
        # Mouvement attendu : Une case vers la gauche
        # print(f"[{datetime.now()}] [game_character.py] Movement to the left from X={position_joueur_x} Y={position_joueur_y} to X={position_joueur_x - 1} Y={position_joueur_y}")
        if not position_joueur_x == 0: # Le joueur ne doit pas se trouver sur la bordure gauche
            if current_collision_map[position_joueur_y][position_joueur_x - 1] == ".": # Le déplacement est possible que si la case à gauche est vide (symbolisée par un "." dans le csv)
                current_collision_map[position_joueur_y][position_joueur_x] = "." # La case où se situait le joueur devient vide
                current_collision_map[position_joueur_y][position_joueur_x - 1] = "P" # La case à gauche du joueur devient occupée par ce dernier

    # Droite

    if pyxel.btnr(pyxel.KEY_D): # Si le joueur appuie sur D / Right
        # Mouvement attendu : une case vers la droite
        # print(f"[{datetime.now()}] [game_character.py] Movement to the right from X={position_joueur_x} Y={position_joueur_y} to X={position_joueur_x + 1} Y={position_joueur_y}")
        if not position_joueur_x == 15: # Le joueur ne doit pas se trouver sur la case bordure, le déplacement serait impossible
            if current_collision_map[position_joueur_y][position_joueur_x + 1] == ".": # Le déplacement est possible, la case est vide
                current_collision_map[position_joueur_y][position_joueur_x] = "." # La case ou était le joueur devient vide
                current_collision_map[position_joueur_y][position_joueur_x + 1] = "P" # La case ou le joueur vient de bouger est occupée par le joueur
    
    # Haut

    if pyxel.btnr(pyxel.KEY_Z): # Si le joueur appuie sur D / Up
        # Mouvement attendu : une case vers le haut
        # print(f"[{datetime.now()}] [game_character.py] Movement to the top from X={position_joueur_x} Y={position_joueur_y} to X={position_joueur_x} Y={position_joueur_y - 1}")
        if not position_joueur_y == 0: # Le joueur ne doit pas se trouver sur la case bordure haut
            if current_collision_map[position_joueur_y - 1][position_joueur_x] == ".": # Le déplacement n'est possible que si la case en haut est vide
                current_collision_map[position_joueur_y][position_joueur_x] = "." # La case devient vide
                current_collision_map[position_joueur_y - 1][position_joueur_x] = "P" # La case où le joueur vient de bouger devient occupée par cette dernière

    # Bas

    if pyxel.btnr(pyxel.KEY_S): # Même principe
        # print(f"[{datetime.now()}] [game_character.py] Movement to the bottom from X={position_joueur_x} Y={position_joueur_y} to X={position_joueur_x} Y={position_joueur_y + 1}")
        if not position_joueur_y == 8:
            if current_collision_map[position_joueur_y + 1][position_joueur_x] == ".":
                current_collision_map[position_joueur_y][position_joueur_x] = "."
                current_collision_map[position_joueur_y + 1][position_joueur_x] = "P"