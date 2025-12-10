import streamlit as st
from fruit_manager import *

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

liste_fruits = inventaire.keys()

st.set_page_layout(layout="wide")
st.title("🧭 Dashboard de la plantation")
st.divider()
c1, _, c2 = st.columns(2, 1, 1)

with c1:
    st.title("🔍️ Inventaire")
    st.metric(label="Montant disponible", value=f"{tresorerie:.2f} €")

with c2:
    st.title("💰️ Trésorerie")
    st.table(inventaire)

st.sidebar.title("Gestion de l'inventaire")

st.sidebar.subheader("Récolte de fruits")
nb_fruit_recolte = st.sidebar.number_input(
    "Nombre de fruits à récolter", min_value=0, step=1
)
fruit_recolte = st.sidebar.selectbox("Fruit à récolter", liste_fruits)
if st.button("Récolter"):
    recolter(inventaire, fruit_recolte, nb_fruit_recolte)

st.sidebar.divider()

st.sidebar.subheader("Vente de fruits")
nb_fruit_vente = st.sidebar.number_input(
    "Nombre de fruits à vendre", min_value=0, step=1
)
fruit_vente = st.sidebar.selectbox("Fruit à vendre", liste_fruits)
if st.button("Vendre"):
    vendre(inventaire, fruit_vente, nb_fruit_vente, tresorerie, prix)
