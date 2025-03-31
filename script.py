import os
import random
import time
import shutil

# Vérifier la taille du terminal
cols, rows = shutil.get_terminal_size()
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{}[]|:;<>?/\\"

# Créer une liste de colonnes avec des positions aléatoires
matrix = [random.randint(0, rows) for _ in range(cols)]

def hacker_matrix():
    while True:
        # Afficher une ligne de la cascade
        for i in range(cols):
            if random.random() < 0.1:  # 10% de chance de reset la colonne
                matrix[i] = 0
            else:
                matrix[i] += 1

            char = random.choice(chars)
            print(f"\033[{matrix[i]};{i}H\033[1;32m{char}\033[0m", end="")

        # Forcer l'affichage en temps réel
        print("\033[H", end="", flush=True)

        time.sleep(0.05)  # Vitesse d'affichage

try:
    # Effacer l'écran et cacher le curseur
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[?25l", end="")  # Cacher le curseur
    hacker_matrix()
except KeyboardInterrupt:
    print("\033[?25h")  # Réafficher le curseur
    os.system("cls" if os.name == "nt" else "clear")
    exit()

