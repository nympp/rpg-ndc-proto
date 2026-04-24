import csv
import pyxel

def calculer_distance(x_a, y_a, x_b, y_b):
    return (x_b - x_a)**2 + (y_b - y_a)**2

# Deprecated, use game_map.py instead

def changer_map(map_name):
    map_name = "assets/maps/"+ map_name + ".csv"
    current_map = []
    with open(map_name, newline="") as map:
        reader = csv.reader(map, delimiter=";")
        for row in reader:
            current_map.append(row)
    return current_map

def debug_draw_walls(wall_x: int, wall_y: int):
    pyxel.rect(wall_x * 16, wall_y * 16, 16, 16, 10)
