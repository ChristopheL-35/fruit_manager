import streamlit as st
from fruit_manager import *
from matplotlib import pyplot as plt

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

liste_fruits = inventaire.keys()

st.set_page_config(layout="wide")
st.title("🧭 Dashboard de la plantation")
st.divider()
c1, _, c2 = st.columns((2, 1, 1))

with c1:
    st.title("🔍️ Inventaire")
    st.table(inventaire, border="horizontal")

    fig, ax = plt.subplots()
    inventaire = dict(
        sorted(inventaire.items(), key=lambda item: item[1], reverse=True)
    )
    ax.bar(inventaire.keys(), inventaire.values())
    ax.tick_params("x", rotation=90)
    ax.tick_params("y", rotation=45)
    ax.set_xlabel("Fruit")
    ax.set_ylabel("Quantité")
    ax.set_title("Inventaire")
    st.pyplot(fig)

with c2:
    st.title("💰️ Trésorerie")
    st.metric(label="Montant disponible", value=f"{tresorerie:.2f} €")

st.sidebar.title("⚖️ Gestion de l'inventaire")

st.sidebar.subheader("Récolte de fruits")
nb_fruit_recolte = st.sidebar.number_input(
    "Nombre de fruits à récolter", min_value=0, step=1
)
fruit_recolte = st.sidebar.selectbox("Fruit à récolter", liste_fruits)
if st.sidebar.button("Récolter"):
    inventaire = recolter(inventaire, fruit_recolte, nb_fruit_recolte)
    ecrire_inventaire(inventaire)
    st.rerun()

st.sidebar.divider()

st.sidebar.subheader("Vente de fruits")
nb_fruit_vente = st.sidebar.number_input(
    "Nombre de fruits à vendre", min_value=0, step=1
)
fruit_vente = st.sidebar.selectbox("Fruit à vendre", liste_fruits)
if st.sidebar.button("Vendre"):
    inventaire, tresorerie = vendre(
        inventaire, fruit_vente, nb_fruit_vente, tresorerie, prix
    )
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
    st.rerun()
