<span id="top"></span>

<div align="center">
    <img src="https://nymp.app/mp-gps-csv/plushie.ico" width="80px">
    <h1>Prototype RPG Pyxel</h1>
    <p>Prototype d'un RPG écrit en Python avec Pyxel.</p>
</div>

## Table des matières

- [Explication des fichiers](#explication-des-fichiers)
    - [Fichiers](#fichiers)
    - [Dossiers](#dossiers)
- [To-Do List](#to-do-list)

## Explication des fichiers

### Fichiers

`app.py` est le fichier principal, celui qu'il faut lancer pour lancer le jeu en lui même.

Le module `pyxel` doit être installé : 
```bash
python -m pip install pyxel
```

Les fichiers s'appelant `game_xxxxx.py` sont des fichiers qui contiennent des fonctions utiles au jeu appelées dans `app.py`. 

### Dossiers

`/assets` contient les assets du prototype (info sur des enemis, collisions des maps...)

`/saves` contient les sauvegardes (position/map du joueur, ou il en est dans le jeu...)

## To-Do List

- Ajouter le système de combat
- Ajouter un inventaire sommaire
- Ajouter menu
    - Ajouter charge save

---

[Retourner en haut](#top)