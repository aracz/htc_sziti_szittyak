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
        st.markdown(
            "Ezen az oldalon a bevételeket és a kiadásokat tudod megvizsgálni, az egyes évek adatait tudod összehasonlítani különböző szempontok szerinti bontásban. ")
        st.markdown("Az éveket és a szűrési szempontokat a legördülő menükből tudod kiválasztani.")
        st.markdown("Például megvizsgálhatod, hogy 2018-ban vagy 2020-ban volt-e több költségvetési bevétele a fővárosnak. Vagy a kiadásokat nézve összevetheted, hogy 2020 után az önkormányzathoz tartozó színházak számának csökkenése hogyan érintette a kulturális és sport feladatokra költött pénzeket.")
        self.select_year_multi = st.multiselect('Válaszd ki az éveket az összehasonlításhoz:', self.df['Év'].unique(),
                                                default=self.df['Év'].unique())

    def run(self):
        income = self.create_income_comparison_chart(self.df)
        spending = self.create_spending_comparison_chart(self.df)
        st.write(income, spending)

    @staticmethod
    def get_data():
        data = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';',
                               'bar_chart')
        df = data.run()
        return df

    def create_income_comparison_chart(self):
        df_ev = self.df[self.df['Év'].isin(self.select_year_multi)]
        df = df_ev[df_ev['oldal'] == 'Bevetel']

        income_cat_list = self.df['Főbb bevételi kategória'].unique().tolist()
        income_cat_list_clean = [x for x in income_cat_list if str(x) != 'nan']
        income_cat_list_clean.insert(0, 'Összes bevételi kategória')
        selected_income_cat = st.selectbox('Válassz egyet a főbb bevételi kategóriák közül:', income_cat_list_clean,
                                           format_func=lambda x: 'Válassz egy lehetőséget' if x == '' else x, index=0)

        if selected_income_cat == 'Összes bevételi kategória':
            bevetel_df = df.groupby('Év').agg(total=('Bevétel (ezer Ft) - reálérték', 'sum')).reset_index()
        else:
            df = df[df['Főbb bevételi kategória'] == selected_income_cat]
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
            title=f'Bevételek - {selected_income_cat} - (ezer Ft) - reálérték'
        )

        fig.update_xaxes(
            title_text='Bevétel (ezer Ft) - reálérték',
            title_standoff=25)

        fig.update_yaxes(
            title_text="Év",
            title_standoff=25)

        st.write(fig)

    def create_spending_comparison_chart(self):
        df_ev = self.df[self.df['Év'].isin(self.select_year_multi)]
        df = df_ev[df_ev['oldal'] == 'Kiadas']

        branch_list = self.df['Ágazat'].unique().tolist()
        branch_list_clean = [x for x in branch_list if str(x) != 'nan']
        branch_list_clean.insert(0, 'Összes ágazat')
        selected_branch = st.selectbox('Válassz egyet a kiadási ágazatok közül:', branch_list_clean,
                                       format_func=lambda x: 'Válassz egy lehetőséget' if x == '' else x, index=0)

        if selected_branch == 'Összes ágazat':
            kiadas_df = df.groupby('Év').agg(total=('Kiadás (ezer Ft) - reálérték', 'sum')).reset_index()
        else:
            df = df[df['Ágazat'] == selected_branch]
            kiadas_df = df.groupby('Év').agg(total=('Kiadás (ezer Ft) - reálérték', 'sum')).reset_index()

        values = kiadas_df['total']
        split = kiadas_df['Év']

        fig = go.Figure(go.Bar(x=values,
                               y=split,
                               orientation='h',
                               marker_color='rgb(18, 50, 110)'), )
        fig.update_yaxes(type='category')
        fig.update_layout(
            title=f'Kiadások - {selected_branch} - (ezer Ft) - reálérték'
        )

        fig.update_xaxes(
            title_text='Kiadás (ezer Ft) - reálérték',
            title_standoff=25)

        fig.update_yaxes(
            title_text="Év",
            title_standoff=25)

        st.write(fig)
