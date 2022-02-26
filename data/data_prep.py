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

        bevetel = self.raw_data()[0]
        kiadas = self.raw_data()[1]

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

        return concat_df

    def raw_data(self):

        bevetel = pd.read_csv(f'{self.resources_dir}/{self.income}', sep=self.separator, header=0,
                              encoding=self.encoding)
        kiadas = pd.read_csv(f'{self.resources_dir}/{self.spending}', sep=self.separator, header=0,
                             encoding=self.encoding)

        return bevetel, kiadas

    def barchart_data(self):
        return True
