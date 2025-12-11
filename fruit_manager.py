import json
import os
import datetime


DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")
HISTO_TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.json")


def ouvrir_inventaire(path=INVENTAIRE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    # Si le fichier n'existe pas on en crée un par défaut
    if not os.path.exists(path):
        inventaire_defaut = {
            "bananes": 50,
            "mangues": 65,
            "ananas": 70,
            "noix de coco": 30,
            "papayes": 10,
            "fruit de la passion": 90,
        }
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(inventaire_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


def ecrire_inventaire(invent, path=INVENTAIRE_PATH):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(invent, fichier, ensure_ascii=False, indent=4)


def afficher_inventaire(invent):
    print()
    print("🔍️ Inventaire actuel :")
    for fruit, quantite in invent.items():
        print(f"- {fruit.capitalize():<15} -- {quantite:>3} unités")


def recolter(invent, fruit, quantite):
    invent[fruit] = invent.get(fruit, 0) + quantite
    print(f"🍍 {fruit} récolté, {quantite} ajoutés à l'inventaire.")
    return invent


def vendre(invent, fruit, quantite, treso, prix):
    if quantite > invent.get(fruit, 0):
        print(f"❌ Vente impossible ; pas assez de {fruit}")
    else:
        invent[fruit] = invent.get(fruit, 0) - quantite
        treso += quantite * prix.get(fruit, 0)
        ecrire_historique_tresorerie(treso)
        print(f"✅ {fruit} vendu, {quantite} sortis de l'inventaire.")
    return invent, treso


def ouvrir_tresorerie(path=TRESORERIE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    # Si le fichier n'existe pas on en crée un par défaut
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(500.0, fichier)
    with open(path, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


def lire_historique_tresorerie(path=HISTO_TRESORERIE_PATH):
    # Si le fichier n'existe pas on en crée un par défaut
    if os.path.exists(path):
        with open(path, "r") as fichier:
            try:
                return json.load(fichier)
            except:
                return []


def ecrire_historique_tresorerie(tresorerie, path=HISTO_TRESORERIE_PATH):
    historique = []
    # Si le fichier n'existe pas on en crée un par défaut
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as fichier:
            try:
                historique = json.load(fichier)
            except:
                historique = []
    historique.append(
        {"timestamp": datetime.datetime.now().isoformat(), "tresorerie": tresorerie}
    )
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(historique, fichier)


def ecrire_tresorerie(treso, path=TRESORERIE_PATH):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(treso, fichier, ensure_ascii=False, indent=4)


def afficher_tresorerie(treso):
    print()
    print(f"💰️ Trésorerie actuelle : {treso:.2f} €")


def ouvrir_prix(path=PRIX_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    # Si le fichier n'existe pas on en crée un par défaut
    if not os.path.exists(path):
        prix_defaut = {
            "bananes": 2,
            "mangues": 7,
            "ananas": 3,
            "noix de coco": 5,
            "papayes": 4,
            "fruit de la passion": 1,
        }
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(prix_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)

    inventaire = recolter(inventaire, "fruit de la passion", 25)
    inventaire = recolter(inventaire, "mangues", 10)

    inventaire, tresorerie = vendre(inventaire, "mangues", 5, tresorerie, prix)
    inventaire, tresorerie = vendre(inventaire, "ananas", 10, tresorerie, prix)

    afficher_inventaire(inventaire)
    afficher_tresorerie(tresorerie)
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
