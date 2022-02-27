import streamlit as st
import pandas as pd
import numpy as np
from data.data_prep import DataPreparation


class DeductionPage:
    def __init__(self, plottype='overview'):
        """

        :param type:
        """
        self.plottype=plottype
        self.df, self.label_df = DeductionPage.get_data()

        st.title("Szolidaritási hozzájárulás")

    def run(self):
        fig = self.create_deduction_chart(self.df)
        st.write(fig)

    @staticmethod
    def get_data():
        """

        :return:
        """
        data = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';', 'deduction')
        df, label_df = data.run()
        return df, label_df

    def create_deduction_chart(self):
        """

        :return:
        """
        chart_data = pd.DataFrame(self.df,
            self.label_df,
            columns=[""]
        )

        st.bar_chart(chart_data)
