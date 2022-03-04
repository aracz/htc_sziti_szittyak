import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
from data.data_prep import DataPreparation
import plotly.express as px

class AreaPage:

    def __init__(self):
        self.df = AreaPage.get_data()
        st.title("KÖLTSÉGVETÉSI  MOZGÁSTÉR")
        st.markdown("""Mennyi mozgástere van a fővárosi önkormányzatnak abban, hogy mire költi a pénzét? - Ezt a kérdést mi is feltettük magunknak. \n
Az önkormányzatok működését törvények szabályozzák, amelyek előírnak olyan feladatokat, amiket az önkormányzatoknak kötelező ellátniuk. Ezen felül vállalhatnak további feladatokat. Az így keletkező kiadásokra az állam részben a költségvetésen keresztül célzottan biztosít pénzt, ezen felül az önkormányzat törvényben szabályozott keretek között saját bevételt is szerezhet. Értelemszerűen a bevételekből elsősorban a kötelező feladatok kiadásait kell fedezni, ezen felül lehet további feladatokat vállalni, ha van miből. \n
Erre a mozgástérre voltunk kíváncsiak.
A grafikonon látszik, hogy 2019-ről 2020-ra az önként vállalt kiadások aránya - vagyis az önkormányzat mozgástere abban, hogy mire költ - nagyon lecsökkent.\n
\n
\n
""")

    def run(self):
        self.create_area(self.df)
        select_year = st.selectbox('Válassz egy évet:', self.df['Év'].unique())
        df_ev = self.df[self.df['Év'] == select_year]
        self.create_bar(df_ev, select_year)

    @staticmethod
    def get_data():
        data = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';', 'area')
        df = data.run()
        return df

    def create_area(self, df):

        df_summed = df.groupby(['Év', 'Felhasználás célja'])[
           'Kiadás (ezer Ft) - reálérték'].sum().reset_index()

        fig = px.area(df_summed, x='Év', y='Kiadás (ezer Ft) - reálérték', color='Felhasználás célja')
        fig.data[0].line.color = "rgba(18, 50, 110, 0.7)"
        fig.data[1].line.color = "rgba(210, 179, 124, 0.7)"
        fig.data[2].line.color = "rgba(160, 217, 247, 0.7)"
        fig.for_each_trace(lambda trace: trace.update(fillcolor=trace.line.color))
        fig.update_layout(
            width=950,
            height=400,
            margin=dict(l=0, r=20, t=40, b=10),
            title=f'Kötelező és önként vállalt kiadások megoszlása'
        )

        st.write(fig)

    def create_bar(self, df, year):
        szabad = df[df['cimkod_str'] == "2"]
        szabad_summed = szabad.groupby(["Feladat megnevezése"])[
           'Kiadás (ezer Ft) - reálérték'].sum().reset_index()
        szabad5 = szabad_summed.sort_values(by=['Kiadás (ezer Ft) - reálérték'], ascending=False).iloc[:10]

        fig = go.Figure(data=[go.Bar(
                    x=szabad5["Feladat megnevezése"], y=szabad5['Kiadás (ezer Ft) - reálérték'],
                    textposition='auto', marker_color="rgba(160, 217, 247, 0.7)"
                )])

        fig.update_layout(
            width=950,
            height=600,
            margin=dict(l=0, r=20, t=40, b=10),
            title=f'Tíz legnagyobb önként vállalt kiadás  - {year}'
        )

        fig.update_yaxes(
            title_text='Kiadás (ezer Ft) - reálérték',
            title_standoff=25)

        st.write(fig)


