import csv
from datetime import datetime

# Fait : Sauvegarder la partie "de base", emplacement sur la map
# A faire : Sauvegarder le niveau des personnages, leur attaques, objets etc.

def sauvegarder_partie(choix_emplacement: int, current_map_name: str, player_x: int, player_y: int):
    save_file_content = []
    with open('saves/' + str(choix_emplacement) + "/base.csv", newline="") as savefile: # Ouverture du fichier de sauvegarde
        reader = csv.DictReader(savefile, delimiter=";")
        for row in reader:
            save_file_content.append(row)
    data = [int(save_file_content[-1]["save_number"]) + 1, datetime.now(), current_map_name, player_x, player_y] # Le numéro de sauvegarde, la date, la carte et les coordonées du jouer sont enregistrés
    with open('saves/' + str(choix_emplacement) + "/base.csv", "a", newline="") as savefile: # Ouverture du fichier principal de sauvegarde, cette fois ci en mode écriture
        f_csv = csv.writer(savefile, delimiter=";")
        f_csv.writerow(data)
    print(f"Sauvegarde Effectuée dans l'emplacement {choix_emplacement} le {datetime.now()}")