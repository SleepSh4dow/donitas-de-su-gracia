from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Donitas de Su Gracia", layout="wide")

# Quita márgenes y elementos de Streamlit para que se vea solo tu página
st.markdown(
    "<style>header, footer {visibility: hidden;} .block-container {padding: 0;}</style>",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)