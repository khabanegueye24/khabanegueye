import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mon CV", page_icon="📍", layout="wide")

# Sidebar pour Contacts et Logiciels
st.sidebar.header("📞 **Contacts**")
st.sidebar.markdown("""
**Adresse**  
Thiès, Diamaguène, Rue 15

**Téléphone**  
[+221 76 158 94 25](tel:+221761589425)

**Email**  
[khabanegueye020@gmail.com](mailto:khabanegueye020@gmail.com)
""")

st.sidebar.header("💻 **Logiciels maîtrisés**")
logiciels = [
    "QGIS / ArcGIS",
    "AutoCAD", 
    "Pix4D",
    "Excel",
    "PowerPoint",
    "Erdas"
]
for logiciel in logiciels:
    st.sidebar.markdown(f"• **{logiciel}**")

st.sidebar.markdown("---")
st.sidebar.markdown("*Géomaticien - L2 en cours*")

# Main content
st.title("KHABANE GUEYE")
st.markdown(" Géomaticien")

## Compétences
st.header("🎯 **Compétences**")
competences = [
    "Maîtrise des techniques de levés topographiques",
    "Conception et mise en page de cartes thématiques de qualité professionnelle",
    "Utilisation des instruments : Niveau, Station totale(manuelle,rebotisées), Drone, GPS",
    "Géo-référencement",
    "Implanter une base de données",
    "Capacité à implanter des projets (bâtiments, voirie) à partir de plans"
]

for comp in competences:
    st.markdown(f"• **{comp}**")

## Expériences Professionnelles
st.header("💼 **Expériences Professionnelles**")

st.subheader("**Juin - Septembre 2024**")
st.markdown("**DIAM'O – Représentant commercial**")
st.markdown("- Interroger les clients")
st.markdown("- Faire connaître et vendre une eau spécifique")

## Formation
st.header("🎓 **Formation**")

st.markdown("""
**2025 - 2026**  
**Centre d'entrepreneuriat et de développement technique (CEDT) le G15**  
*Licence 2 en Géomatique (Formation en cours)*

**2024 - 2025**  
**Centre d'entrepreneuriat et de développement technique (CEDT) le G15**  
*Licence 1 en Géomatique*

**2022 - 2023**  
**Yatinga**  
*Baccalauréat*
""")



