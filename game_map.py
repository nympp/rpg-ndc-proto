import csv

def get_map(map_name):
    path = "assets/maps/" + map_name
    map_name
    map_info = [] # Informations sur la carte
    collision_map = [] # Informations sur les collisions de la carte

    # Map de collision
    with open(path + "/map_collisions.csv", newline="") as map_collisions: 
        reader = csv.reader(map_collisions, delimiter=";")
        for row in reader:
            collision_map.append(row)
    
    # Informations sur la carte
    with open(path + "/map_info.csv", newline="") as map_info_csv:
        reader = csv.DictReader(map_info_csv, delimiter=";")
        for row in reader:
            map_info.append(row)

    return map_name, collision_map, map_info

def read_collision_map(current_collision_map): # current_collision_map est une liste (voir dans map_collisions.csv)
    
    # Détection des ennemis
    
    enemy_1 = []
    enemy_2 = []
    enemy_3 = [] # Maximum de 3 enemis affichés sur une carte de 16x9 c

    enemy_count = 0

    for y_axis in range(len(current_collision_map)):
        for x_axis in range(len(current_collision_map[y_axis])):
            if current_collision_map[y_axis][x_axis][:5] == "ENEMY": # Un enemi a été trouvé (ENEMYID=00&LVL=010)
                # print(f"Enemi trouvé! {current_collision_map[y_axis][x_axis]}, en X={x_axis} Y={y_axis}")
                if enemy_count == 0:
                    enemy_1 = [current_collision_map[y_axis][x_axis][8:10], current_collision_map[y_axis][x_axis][15:18], x_axis, y_axis, current_collision_map[y_axis][x_axis][27:30]] # [ID: str, LVL: str; X: int, Y: int, LOOKING: str]
                elif enemy_count == 1:
                    enemy_2 = [current_collision_map[y_axis][x_axis][8:10], current_collision_map[y_axis][x_axis][15:18], x_axis, y_axis, current_collision_map[y_axis][x_axis][27:30]] # [ID: str, LVL: str; X: int, Y: int, LOOKING: str]
                else:
                    enemy_3 = [current_collision_map[y_axis][x_axis][8:10], current_collision_map[y_axis][x_axis][15:18], x_axis, y_axis, current_collision_map[y_axis][x_axis][27:30]] # [ID: str, LVL: str; X: int, Y: int, LOOKING: str]
                enemy_count += 1               
    
    # print(enemy_1, enemy_2, enemy_3)

    # Détections des NPC
    # A faire

    return [enemy_1, enemy_2, enemy_3], [] # , [npc_1] etc. tuple contenant deux listes
