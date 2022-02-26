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

    def create_sankey(self):
        """

        :return:
        """
        df_ev = self.df[self.df['Év'] == self.select_year]

        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=self.label_df['label'].tolist(),
                color=['Color']
            ),
            link=dict(
                source=df_ev['source_code'].tolist(),
                target=df_ev['target_code'].tolist(),
                value=df_ev['value'].tolist()
            ))])

        st.write(fig)
