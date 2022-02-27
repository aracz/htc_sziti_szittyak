import base64
import streamlit as st

from pages import home
from pages.sankey import SankeyPage
from pages.deduction import DeductionPage


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="logo-container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open("resources/logo.png", "rb").read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)

query_params = st.experimental_get_query_params()
tabs = ["Home", "Bevételek és kiadások", "Szolidaritási hozzájárulás"]
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "Home"

if active_tab not in tabs:
    st.experimental_set_query_params(tab="Home")
    active_tab = "Home"

li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
    </li>
    """
    for t in tabs
)
tabs_html = f"""
    <ul class="nav nav-tabs">
    {li_items}
    </ul>
"""

st.markdown(tabs_html, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if active_tab == "Home":
    fig = home.create_homepage()
elif active_tab == "Bevételek és kiadások":
    sankey_page = SankeyPage()
    fig = sankey_page.create_sankey()
elif active_tab == "Szolidaritási hozzájárulás":
    deduction_page = DeductionPage()
    fig = deduction_page.create_deduction_chart()
else:
    st.error("Something has gone terribly wrong.")
