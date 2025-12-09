import json


def ouvrir_inventaire(path="./data/inventaire.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ecrire_inventaire(invent, path="data/inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(invent, fichier, ensure_ascii=False, indent=4)


def afficher_inventaire(invent):
    print("Inventaire actuel :")
    for fruit, quantite in invent.items():
        print(f"- {fruit.capitalize():<15} -- {quantite:>3} unités")


def recolter(invent, fruit, quantite):
    invent[fruit] = invent.get(fruit, 0) + quantite
    print(f"{fruit} récolté, {quantite} ajoutés à l'inventaire.")


def vendre(invent, fruit, quantite):
    vendus = min(invent.get(fruit, 0), quantite)
    invent[fruit] = max(invent.get(fruit, 0) - quantite, 0)
    print(f"{fruit} vendus, {vendus} sortis de l'inventaire.")


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    afficher_inventaire(inventaire)
    recolter(inventaire, "fruit de la passion", 25)
    recolter(inventaire, "bananes", 10)
    vendre(inventaire, "mangues", 15)
    vendre(inventaire, "ananas", 70)
    afficher_inventaire(inventaire)
    ecrire_inventaire(inventaire)
