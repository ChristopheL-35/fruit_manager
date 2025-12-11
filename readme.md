# 🍇 Fruit-Manager

Ce mini-projet **Fruit Manager** vise à tester l'utilisation de _git_ avec un petit programme de gestion d'inventaire, ainsi que de pratiquer les dashboards simples avec _streamlit_.

## 🛠️ Installation

Création de l'environnement virtuel : \
```poetry install```

Lancement du projet avec poetry : \
    ```poetry run streamlit run app.py```

## 🚀 Fonctionnalités

- **Vente de fruits** : Sélectionner un fruit et le nombre à vendre, puis cliquer sur le bouton ```Vendre```.
- **Récolte** : Ajoutez facilement de nouveaux fruits à l'inventaire après chaque récolte.
- **Suivi de trésorerie** : Visualisez le montant disponible après chaque opération.

## 🗂️ Structure du projet

- ```app.py``` : Interface principale _Streamlit_
- ```fruit_manager.py``` : Fonctions de gestion de l'inventaire, de sventes, des récoltes et de la trésorerie
- ```data/``` : Fichiers de données (inventaire, trésorerie, prix)

## 🍋 Exemple d'utilisation

- Accédez à l'[interface web](http://localhost:8501) générée par _Streamlit_.
- Utilisez la barre latérale pour récolter ou vendre des fruits.
- Consultez l'inventaire et la trésorerie mis à jour en temps réel.

## 🤝 Contribuer

Les contributions sont les bienvenues ; n'hésitez pas à ouvrir une _issue_ ou une _pull request_ pour proposer des améliorations.
