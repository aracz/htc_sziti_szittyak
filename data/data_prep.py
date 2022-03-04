import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect


class DataPreparation:

    def __init__(self, resources_dir, income_file, spending_file, encoding, separator, chart):
        self.resources_dir = resources_dir
        self.income = income_file
        self.spending = spending_file
        self.encoding = encoding
        self.separator = separator
        self.chart_type = chart

    def run(self):

        if self.chart_type == 'sankey':
            return self.sankey_data()
        elif self.chart_type == 'bar_chart':
            return self.barchart_data()
        elif self.chart_type == 'area':
            return self.area_data()
        else:
            return self.area_data()

    def import_sheets(self):

        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=[
                "https://www.googleapis.com/auth/spreadsheets",
            ],
        )
        conn = connect(credentials=credentials)

        def run_query(query):
            rows = conn.execute(query, headers=1)
            return rows

        bevetel_url = st.secrets["bevetel_url"]
        bevetel_raw = run_query(f'SELECT * FROM "{bevetel_url}"')

        bevetel = pd.DataFrame(bevetel_raw.fetchall())
        bevetel.columns = ["Bevétel típusa", "Főbb bevételi kategória", "Főbb bevételi kategória alkategóriái",
                           "Megnevezés", "Forrás", "Szervezeti egység", "Év", "Bevétel (ezer Ft) - nominál érték",
                           "Bevétel (ezer Ft) - reálérték"]

        kiadas_url = st.secrets["kiadas_url"]
        kiadas_raw = run_query(f'SELECT * FROM "{kiadas_url}"')

        kiadas = pd.DataFrame(kiadas_raw.fetchall())
        kiadas.columns = ["Címkód", "Címkód megnevezése", "Ágazat", "Ágazat alábontás", "Feladat megnevezése",
                          "Szervezeti egység", "Év", "Kiadás (ezer Ft) - nominál érték", "Kiadás (ezer Ft) - reálérték"]

        return bevetel, kiadas

    def sankey_data(self):

        bevetel, kiadas = self.raw_data()

        # kategoria hozzaadasa
        bevetel['oldal'] = 'Bevetel'
        kiadas['oldal'] = 'Kiadas'

        kiadas['Ágazat'] = kiadas['Ágazat'].str.split(')').str[1]

        bevetel['source'] = bevetel['Főbb bevételi kategória']
        bevetel['target'] = bevetel['Szervezeti egység']
        bevetel['value'] = bevetel['Bevétel (ezer Ft) - reálérték']

        kiadas['source'] = kiadas['Szervezeti egység']
        kiadas['target'] = kiadas['Ágazat']
        kiadas['value'] = kiadas['Kiadás (ezer Ft) - reálérték']

        # concat
        concat_df = pd.concat([bevetel, kiadas])

        #rename cat
        all_values = concat_df['source'].tolist() + kiadas['target'].tolist()
        all_values_unique = list(set(all_values))
        label_df = pd.DataFrame({'label': all_values_unique})
        label_df['code'] = label_df[['label']].apply(lambda col: pd.Categorical(col).codes)
        label_df = label_df.sort_values(by=['code'], ascending=True)

        rename_dict = dict(zip(label_df['label'], label_df['code']))
        concat_df['source_code'] = concat_df['source'].map(lambda s: rename_dict.get(s) if s in rename_dict else s)
        concat_df['target_code'] = concat_df['target'].map(lambda s: rename_dict.get(s) if s in rename_dict else s)

        concat_df['value'] = [float(str(i).replace(",", ".")) for i in concat_df['value']]
        concat_df = concat_df.groupby(['source', 'target', 'source_code', 'target_code', 'Év'])['value'].sum().reset_index()

        label_df['color'] = 'grey'
        color_dict = {'Főpolgármesteri Hivatal és Önkormányzat': "rgba(160, 217, 247, 0.8)",
                      'Költségvetési intézmények': "rgba(210, 179, 124, 0.8)"}
        label_df['color'] = label_df['label'].apply(
            lambda x: color_dict[x] if x in color_dict.keys() else 'grey')
        label_df['color'] = label_df['label'].apply(
            lambda x: color_dict[x] if x in color_dict.keys() else 'grey')

        concat_df['link_color'] = 'grey'
        for index, row in concat_df.iterrows():
            if row['source']=='Főpolgármesteri Hivatal és Önkormányzat' or row['target']=='Főpolgármesteri Hivatal és Önkormányzat':
                concat_df.loc[index, 'link_color'] = color_dict['Főpolgármesteri Hivatal és Önkormányzat']
            else:
                concat_df.loc[index, 'link_color'] = color_dict['Költségvetési intézmények']

        return concat_df, label_df

    def area_data(self):

        bevetel, kiadas = self.raw_data()

        kiadas['cimkod_str'] = kiadas['Címkód'].astype(str).str[-1]
        kiadas['Felhasználás célja'] = 'Kötelező kiadások'

        onkent = kiadas[kiadas['cimkod_str'] == '2']
        onkent['Felhasználás célja'] = 'Szabadon felhasználható, önként vállalt kiadások'

        kotelezo = kiadas[kiadas['cimkod_str'] == '1']

        hatosagi = kiadas[kiadas['cimkod_str'] == '3']
        hatosagi['Felhasználás célja'] = 'Hatósági kötelező kiadások'

        concat_df = pd.concat([onkent, kotelezo, hatosagi])

        return concat_df

    def raw_data(self):

        bevetel, kiadas = self.import_sheets()

        bevetel['Bevétel (ezer Ft) - reálérték'] = [float(str(i).replace(",", ".")) for i in
                                                   bevetel['Bevétel (ezer Ft) - reálérték']]

        kiadas['Kiadás (ezer Ft) - reálérték'] = [float(str(i).replace(",", ".")) for i in
                                                  kiadas['Kiadás (ezer Ft) - reálérték']]

        kiadas['Szervezeti egység'] = [str(i).replace("Költségvetési intézmény", "Költségvetési intézmények") for i in
                                       kiadas['Szervezeti egység']]

        bevetel['Év'] = bevetel['Év'].astype(str).str.split('.').str[0].astype(int)
        kiadas['Év'] = kiadas['Év'].astype(str).str.split('.').str[0].astype(int)
        kiadas['Címkód'] = kiadas['Címkód'].astype(str).str.split('.').str[0].astype(int)

        rename_dict = {"Főpolgármesteri Hivatal": "Főpolgármesteri Hivatal és Önkormányzat",
                       "Önkormányzat": "Főpolgármesteri Hivatal és Önkormányzat"}
        kiadas['Szervezeti egység'] = kiadas['Szervezeti egység'].map(
            lambda s: rename_dict.get(s) if s in rename_dict else s)
        bevetel['Szervezeti egység'] = bevetel['Szervezeti egység'].map(
            lambda s: rename_dict.get(s) if s in rename_dict else s)

        return bevetel, kiadas

    def barchart_data(self):

        bevetel, kiadas = self.raw_data()

        bevetel['oldal'] = 'Bevetel'
        kiadas['oldal'] = 'Kiadas'

        kiadas['Ágazat'] = kiadas['Ágazat'].str.split(')').str[-1]

        concat_df = pd.concat([bevetel, kiadas])

        return concat_df

