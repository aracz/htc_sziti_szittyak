import json
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
from data.data_prep import DataPreparation
from streamlit_metrics import metric, metric_row

class SankeyPage:
    def __init__(self, plottype='overview'):
        """

        :param type:
        """
        self.plottype=plottype
        self.df, self.label_df = SankeyPage.get_data()
        st.title("Bevételek és kiadások")
        st.markdown("Bla bla")
        self.select_year = st.selectbox('Valasszon egy évet:', self.df['Év'].unique())
        self.df_ev = self.df[self.df['Év'] == self.select_year]
        self.df_ev_tminus1 = self.df[self.df['Év'] == (self.select_year-1)]

    def run(self):
        fig = self.create_sankey(self.df)
        st.write(fig)

    @staticmethod
    def get_data():
        """

        :return:
        """
        data = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';', 'sankey')
        df, label_df = data.run()
        return df, label_df

    def create_kpi(self):
        """

        :return:
        """
        df_kiadas = self.df_ev[self.df_ev['source'].isin(
            ['Főpolgármesteri Hivatal és Önkormányzat', 'Költségvetési intézmények'])]
        df_bevetel = self.df_ev[~self.df_ev['source'].isin(
            ['Főpolgármesteri Hivatal és Önkormányzat', 'Költségvetési intézmények'])]
        kiadas_total = df_kiadas['value'].sum()
        bevetel_total = df_bevetel['value'].sum()

        df_kiadas_tminus1 = self.df_ev_tminus1[self.df_ev_tminus1['source'].isin(
            ['Főpolgármesteri Hivatal és Önkormányzat', 'Költségvetési intézmények'])]
        df_bevetel_tminus1 = self.df_ev_tminus1[~self.df_ev_tminus1['source'].isin(
            ['Főpolgármesteri Hivatal és Önkormányzat', 'Költségvetési intézmények'])]
        kiadas_total_tminus1 = df_kiadas_tminus1['value'].sum()
        bevetel_total_tminus1 = df_bevetel_tminus1['value'].sum()

        kiadas_delta = kiadas_total/kiadas_total_tminus1
        bevetel_delta = bevetel_total/bevetel_total_tminus1
        if kiadas_delta >= 1:
            kiadas_delta = "{:.0%}".format(kiadas_delta)
        else:
            kiadas_delta = "-{:.0%}".format(kiadas_delta)
        if bevetel_delta >= 1:
            bevetel_delta = "{:.0%}".format(bevetel_delta)
        else:
            bevetel_delta = "-{:.0%}".format(bevetel_delta)

        if self.select_year == 2017:
            metric_row(
                {
                    "Bevétel": SankeyPage.human_format(bevetel_total),
                    "Kiadás": SankeyPage.human_format(kiadas_total),
                })
        else:
            col1, col2 = st.columns(2)
            col1.metric("Bevétel", SankeyPage.human_format(bevetel_total), str(bevetel_delta))
            col2.metric("Kiadás", SankeyPage.human_format(kiadas_total), str(kiadas_delta))

    @staticmethod
    def human_format(num):
        num = float('{:.3g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


    def create_sankey(self):
        """

        :return:
        """
        self.create_kpi()

        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=self.label_df['label'].tolist(),
                color="rgba(18,50,110,0.7)"
            ),
            link=dict(
                source=self.df_ev['source_code'].tolist(),
                target=self.df_ev['target_code'].tolist(),
                value=self.df_ev['value'].tolist(),
                color=self.df_ev['link_color'].tolist()
            ))])

        fig.update_layout(
            width=800,
            height=600,
            margin=dict(l=0, r=20, t=20, b=10)
        )

        st.write(fig)
