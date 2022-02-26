from data.data_prep import DataPreparation


df = DataPreparation('resources', 'bevetelek_2017_2021.csv', 'kiadasok_2017_2021.csv', 'UTF-8', ';', 'sankey')
df.run()

