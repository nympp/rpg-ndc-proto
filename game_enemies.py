import csv
import pyxel
import game_character

enemy_global_x = int
enemy_global_y = int

def get_enemy(enemy_id):
    enemy_path = "assets/enemies/" + enemy_id
    enemy_info = []

    # Enemy Info
    with open(enemy_path + "/info.csv", newline="") as info:
        reader = csv.DictReader(info, delimiter=";")
        for row in reader:
            enemy_info.append(row)

    return enemy_info

def draw_enemy(enemy_id: str, enemy_x: int, enemy_y: int):
    global enemy_global_x, enemy_global_y

    enemy_global_x = enemy_x
    enemy_global_y = enemy_y
    
    # Récupération du design de l'ennemi [A ajouter]
    # Pour l'instant, utilisation d'un carré 1c rouge
    pyxel.rect(enemy_x * 16, enemy_y * 16, 16, 16, 8)

def is_player_in_enemy_line(direction: str, current_collision_map: list):
    # player_found = False
    # La ligne que l'ennemi tient
    if direction == "TOP":
        return game_character.trouver_position_joueur(current_collision_map)["x"] == enemy_global_x and game_character.trouver_position_joueur(current_collision_map)["y"] < enemy_global_y and enemy_global_y - game_character.trouver_position_joueur(current_collision_map)["y"] < 7
    elif direction == "BOT":
        return game_character.trouver_position_joueur(current_collision_map)["x"] == enemy_global_x and game_character.trouver_position_joueur(current_collision_map)["y"] > enemy_global_y and game_character.trouver_position_joueur(current_collision_map)["y"] - enemy_global_y < 7       
    elif direction == "LEF":
        return game_character.trouver_position_joueur(current_collision_map)["y"] == enemy_global_y and game_character.trouver_position_joueur(current_collision_map)["x"] < enemy_global_x and enemy_global_x - game_character.trouver_position_joueur(current_collision_map)["x"] < 7
    elif direction == "RIG":
        return game_character.trouver_position_joueur(current_collision_map)["y"] == enemy_global_y and game_character.trouver_position_joueur(current_collision_map)["x"] > enemy_global_x and game_character.trouver_position_joueur(current_collision_map)["x"] - enemy_global_x < 7