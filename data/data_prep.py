import pandas as pd


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
            return self.raw_data()
        else:
            return self.raw_data()

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

        return concat_df, label_df

    def raw_data(self):

        bevetel = pd.read_csv(f'{self.resources_dir}/{self.income}', sep=self.separator, header=0,
                              encoding=self.encoding)
        kiadas = pd.read_csv(f'{self.resources_dir}/{self.spending}', sep=self.separator, header=0,
                             encoding=self.encoding)

        bevetel['Bevétel(ezer Ft) - reálérték'] = [float(str(i).replace(",", ".")) for i in
                                                   bevetel['Bevétel (ezer Ft) - reálérték']]

        kiadas['Kiadás (ezer Ft) - reálérték'] = [float(str(i).replace(",", ".")) for i in
                                                  kiadas['Kiadás (ezer Ft) - reálérték']]

        kiadas['Szervezeti egység'] = [str(i).replace("Költségvetési intézmény", "Költségvetési intézmények") for i in
                                       kiadas['Szervezeti egység']]

        return bevetel, kiadas

    def barchart_data(self):
        return True
