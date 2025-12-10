import json


def ouvrir_inventaire(path="./data/inventaire.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ecrire_inventaire(invent, path="data/inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(invent, fichier, ensure_ascii=False, indent=4)


def afficher_inventaire(invent):
    print()
    print("✋ Inventaire actuel :")
    for fruit, quantite in invent.items():
        print(f"- {fruit.capitalize():<15} -- {quantite:>3} unités")
    print()


def recolter(invent, fruit, quantite):
    invent[fruit] = invent.get(fruit, 0) + quantite
    print(f"✋ {fruit} récolté, {quantite} ajoutés à l'inventaire.")


def vendre(invent, fruit, quantite, treso, prix):
    if quantite > invent.get(fruit, 0):
        print(f"❌ Vente impossible ; pas assez de {fruit}")
    else:
        invent[fruit] = invent.get(fruit, 0) - quantite
        treso += quantite * prix.get(fruit, 0)
        print(f"✅ {fruit} vendu, {quantite} sortis de l'inventaire.")
    return treso


def ouvrir_tresorerie(path="data/tresorerie.txt"):
    with open(path, "r", encoding="utf-8") as fichier:
        tresorerie = json.load(fichier)
    return tresorerie


def ecrire_tresorerie(treso, path="data/tresorerie.txt"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(treso, fichier, ensure_ascii=False, indent=4)


def afficher_tresorerie(treso):
    print(f"✨ Trésorerie actuelle : {treso:.2f} €")
    print()


def ouvrir_prix(path="./data/prix.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        prix = json.load(fichier)
    return prix


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)

    recolter(inventaire, "fruit de la passion", 25)
    recolter(inventaire, "mangues", 10)

    tresorerie = vendre(inventaire, "mangues", 5, tresorerie, prix)
    tresorerie = vendre(inventaire, "ananas", 10, tresorerie, prix)

    afficher_inventaire(inventaire)
    afficher_tresorerie(tresorerie)
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
