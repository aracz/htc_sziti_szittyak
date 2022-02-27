import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
from data.data_prep import DataPreparation
from streamlit_metrics import metric, metric_row
import plotly.express as px

class AreaPage:
    def __init__(self):
        self.df = AreaPage.get_data()

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
        fig.data[0].line.color = '#12326E'
        fig.data[1].line.color = '#D2B37C'
        fig.data[2].line.color = '#A0D9F7'
        fig.for_each_trace(lambda trace: trace.update(fillcolor=trace.line.color))
        fig.update_layout(
            width=950,
            height=400,
            margin=dict(l=0, r=20, t=20, b=10),
            #paper_bgcolor='rgba(0,0,0,0)',
            #plot_bgcolor='rgba(0,0,0,0)'
        )

        st.write(fig)
