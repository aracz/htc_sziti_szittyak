import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
from data.data_prep import DataPreparation
from streamlit_metrics import metric, metric_row
import plotly.express as px

class AreaPage:
    def __init__(self):
        self.df = AreaPage.get_data()
        st.title("KÖLTSÉGVETÉSI  MOZGÁSTÉR")
        st.markdown("""Mennyi mozgástere van a kiadások csökkentésére vagy plusz bevételek szerzésére a fővárosi önkormányzatnak? - Ezt a kérdést mi is feltettük magunknak.
Az alábbi grafikonon látszik, hogy 2019-ről 2020-ra ez a mozgástér a kiadások tekintetében - vagyis az önként vállalt kiadások aránya - nagyon lecsökkent.""")

    @staticmethod
    def get_data():
        """

        :return:
        """
        data = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';', 'area')
        df = data.run()
        return df

    def create_area(self):
        print(self.df)

        df_summed = self.df.groupby(['Év', 'Felhasználás célja'])[
           'Kiadás (ezer Ft) - reálérték'].sum().reset_index()

        print(df_summed)

        fig = px.area(df_summed, x='Év', y='Kiadás (ezer Ft) - reálérték', color='Felhasználás célja')
        fig.data[0].line.color = "rgba(18,50,110,0.7)"
        fig.data[1].line.color = "rgba(210, 179, 124, 0.7)"
        fig.data[2].line.color = "rgba(160, 217, 247, 0.7)"
        fig.for_each_trace(lambda trace: trace.update(fillcolor=trace.line.color))
        fig.update_layout(
            width=950,
            height=400,
            margin=dict(l=0, r=20, t=20, b=10),
            #paper_bgcolor='rgba(0,0,0,0)',
            #plot_bgcolor='rgba(0,0,0,0)'
        )

        st.write(fig)

        self.create_bar()

    def create_bar(self):
        st.title("5 legnagyobb szabadon felhasználható, önként vállalt kiadás")
        self.select_year = st.selectbox('Kérem válasszon egy évet:', self.df['Év'].unique())
        self.df_ev = self.df[self.df['Év'] == self.select_year]
        szabad = self.df[self.df['cimkod_str'] == "2"]
        szabad_summed = self.df.groupby(["Feladat megnevezése"])[
           'Kiadás (ezer Ft) - reálérték'].sum().reset_index()
        szabad5 = szabad_summed.sort_values(by=['Kiadás (ezer Ft) - reálérték'], ascending=False).iloc[:5]

        fig = go.Figure(data=[go.Bar(
                    x=szabad5["Feladat megnevezése"], y=szabad['Kiadás (ezer Ft) - reálérték'],
                    textposition='auto', marker_color="rgba(160, 217, 247, 0.7)"
                )])

        fig.update_layout(
            width=950,
            height=400,
            margin=dict(l=0, r=20, t=20, b=10),
            #paper_bgcolor='rgba(0,0,0,0)',
            #plot_bgcolor='rgba(0,0,0,0)'
        )

        st.write(fig)


