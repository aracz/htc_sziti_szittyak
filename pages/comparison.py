import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

from data.data_prep import DataPreparation


class ComparisonChart:

    def __init__(self, plottype='overview'):
        self.plottype = plottype
        self.df = ComparisonChart.get_data()
        st.title("Összehasonlítás")
        st.markdown("Ezen az oldalon a bevételeket és a kiadásokat tudod megvizsgálni, az egyes évek adatait tudod összehasonlítani különböző szempontok szerinti bontásban. Az éveket és a szűrési szempontokat a legördülő menükből tudod kiválasztani.")
        self.select_year_multi = st.multiselect('Válassza ki az éveket az összehasonlításhoz:', self.df['Év'].unique(),
                                                default=self.df['Év'].unique())
        # self.cols = st.columns([1, 2])
        # self.cols2 = st.columns([1, 2])
        # self.select_branch = st.selectbox('Válasszon egyet a kiadási ágazatok közül:', self.df['Ágazat'].unique())
        self.select_income_cat = st.selectbox('Válassz egyet a főbb bevételi kategóriák közül:', self.df['Főbb bevételi kategória'].unique())

    def run(self):
        income = self.create_income_comparison_chart(self.df)
        spending = self.create_spending_comparison_chart(self.df)
        st.write(income, spending)

    @staticmethod
    def get_data():
        data = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';',
                               'bar_chart')
        df = data.run()
        print(type(df))
        return df

    def create_income_comparison_chart(self):
        df_ev = self.df[self.df['Év'].isin(self.select_year_multi)]
        df = df_ev[df_ev['oldal'] == 'Bevetel']


        bevetel_df = df.groupby('Év').agg(total=('Bevétel (ezer Ft) - reálérték', 'sum')).reset_index()
        values = bevetel_df['total']
        split = bevetel_df['Év']

        fig = go.Figure(go.Bar(x=values,
                               y=split,
                               orientation='h',
                               marker_color='rgb(18, 50, 110)')
                        )
        fig.update_yaxes(type='category')

        fig.update_layout(
            title='Bevételek - Összes bevétel (ezer Ft) - reálérték'
        )

        st.write(fig)

    def create_spending_comparison_chart(self):
        df_ev = self.df[self.df['Év'].isin(self.select_year_multi)]
        df = df_ev[df_ev['oldal'] == 'Kiadas']
        # branch_options = ~ self.df['Ágazat'].unique()
        select_branch = st.selectbox('Válassz egyet a kiadási ágazatok közül:', self.df['Ágazat'].unique(), format_func=lambda x: 'Válassz egy lehetőséget' if x == 'nan' else x, index=0)

        kiadas_df = df.groupby('Év').agg(total=('Kiadás (ezer Ft) - reálérték', 'sum')).reset_index()
        values = kiadas_df['total']
        split = kiadas_df['Év']

        fig = go.Figure(go.Bar(x=values,
                               y=split,
                               orientation='h',
                               marker_color='rgb(18, 50, 110)'), )
        fig.update_yaxes(type='category')
        fig.update_layout(
            title='Kiadások - Összes kiadás (ezer Ft) - reálérték'
        )

        st.write(fig)
