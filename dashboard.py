import base64
import streamlit as st

from pages.comparison import ComparisonChart
from pages import home
from pages.sankey import SankeyPage
from pages.area import AreaPage



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

st.markdown("<h1 style='text-align: center; color: #12326E;'>KÖZÉRTHETŐ KÖLTSÉGVETÉS</h1>", unsafe_allow_html=True)


query_params = st.experimental_get_query_params()
tabs = ["Bevezető", "Áttekintés", "Összehasonlítás", "Mozgástér"]
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "Bevezető"

if active_tab not in tabs:
    st.experimental_set_query_params(tab="Bevezető")
    active_tab = "Bevezető"

li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="?tab={t}" target="_self">{t}</a>
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

if active_tab == "Bevezető":
    fig = home.create_homepage()
elif active_tab == "Áttekintés":
    sankey_page = SankeyPage()
    fig = sankey_page.run()
elif active_tab == "Mozgástér":
    area_page = AreaPage()
    fig = area_page.run()
elif active_tab == 'Összehasonlítás':
    comparison_page = ComparisonChart()
    title1 = 'Bevételek'
    fig1 = comparison_page.create_income_comparison_chart()
    title2 = 'Kiadások'
    fig2 = comparison_page.create_spending_comparison_chart()
else:
    st.error("Valami elromlott.")
