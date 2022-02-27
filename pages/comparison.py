import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import pandas as pd

from data.data_prep import DataPreparation


class ComparisonChart:

    def __init__(self, plottype='overview'):
        self.plottype = plottype
        self.df = ComparisonChart.get_data()
        st.title("Összehasonlítás")
        st.markdown("Bla bla")
        self.select_year_multi = st.multiselect('Válassza ki az éveket az összehasonlításhoz:', self.df['Év'].unique(), default=self.df['Év'].unique())

    def run(self):
        income = self.create_income_comparison_chart(self.df)
        spending = self.create_spending_comparison_chart(self.df)
        st.write(income, spending)

    @staticmethod
    def get_data():
        data = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';', 'bar_chart')
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
                               orientation='h'))
        fig.update_yaxes(type='category')
        fig.update_layout(
            title='Bevételek'
        )

        st.write(fig)

    def create_spending_comparison_chart(self):

        df_ev = self.df[self.df['Év'].isin(self.select_year_multi)]
        df = df_ev[df_ev['oldal'] == 'Kiadas']
        # df = df[df['Ágazat alábontás'] == self.select_branch_sub]

        kiadas_df = df.groupby('Év').agg(total=('Kiadás (ezer Ft) - reálérték', 'sum')).reset_index()
        values = kiadas_df['total']
        split = kiadas_df['Év']

        fig = go.Figure(go.Bar(x=values,
                               y=split,
                               orientation='h'), )
        fig.update_yaxes(type='category')
        fig.update_layout(
            title='Kiadások'
        )

        st.write(fig)




