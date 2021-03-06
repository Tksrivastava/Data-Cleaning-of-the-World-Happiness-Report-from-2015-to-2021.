import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()

# IMPORTING THE DATA SETS ----
# 2015 -
data_set_1 = pd.read_csv('C:/Users/TANUL/PycharmProjects/worldHappinessReport2021DataAnalysisProject/'
                         'World_Happiness_Report_2015.csv')
# 2016 -
data_set_2 = pd.read_csv('C:/Users/TANUL/PycharmProjects/worldHappinessReport2021DataAnalysisProject/'
                         'World_Happiness_Report_2016.csv')
# 2017 -
data_set_3 = pd.read_csv('C:/Users/TANUL/PycharmProjects/worldHappinessReport2021DataAnalysisProject/'
                         'World_Happiness_Report_2017.csv')
# 2018 -
data_set_4 = pd.read_csv('C:/Users/TANUL/PycharmProjects/worldHappinessReport2021DataAnalysisProject/'
                         'World_Happiness_Report_2018.csv')
# 2019 -
data_set_5 = pd.read_csv('C:/Users/TANUL/PycharmProjects/worldHappinessReport2021DataAnalysisProject/'
                         'World_Happiness_Report_2019.csv')
# 2020 -
data_set_6 = pd.read_csv('C:/Users/TANUL/PycharmProjects/worldHappinessReport2021DataAnalysisProject/'
                         'World_Happiness_Report_2020.csv')
# 2021 -
data_set_7 = pd.read_csv('C:/Users/TANUL/PycharmProjects/worldHappinessReport2021DataAnalysisProject/'
                         'World_Happiness_Report_2021.csv')

# MANIPULATING THE COLUMN NAMES OF data2015.csv ----
data_set_1.rename(columns={'Economy (GDP per Capita)': 'GDP per capita',
                           'Health (Life Expectancy)': 'Life Expectancy',
                           'Trust (Government Corruption)': 'Corruption'}, inplace=True)

# MANIPULATING THE COLUMN NAMES OF data2016.csv ----
data_set_2.rename(columns={'Economy (GDP per Capita)': 'GDP per capita',
                           'Health (Life Expectancy)': 'Life Expectancy',
                           'Trust (Government Corruption)': 'Corruption'}, inplace=True)

# MANIPULATING THE COLUMN NAMES OF data2017.csv ----
data_set_3.rename(columns={'Economy..GDP.per.Capita.': 'GDP per capita',
                           'Health..Life.Expectancy.': 'Life Expectancy',
                           'Trust..Government.Corruption.': 'Corruption',
                           'Happiness.Score': 'Happiness Score',
                           'Happiness.Rank': 'Happiness Rank',
                           'Dystopia.Residual': 'Dystopia Residual',
                           'Whisker.high': 'Whisker High',
                           'Whisker.low': 'Whisker Low'}, inplace=True)
data_set_3.drop(['Whisker High', 'Whisker Low'], axis='columns', inplace=True)

# MANIPULATING THE COLUMN NAMES OF data2018.csv ----
data_set_4.rename(columns={'Overall rank': 'Happiness Rank',
                           'Country or region': 'Country',
                           'Score': 'Happiness Score',
                           'Healthy life expectancy': 'Life Expectancy',
                           'Freedom to make life choices': 'Freedom',
                           'Perceptions of corruption': 'Corruption'}, inplace=True)

# MANIPULATING THE COLUMN NAMES OF data2019.csv ----
data_set_5.rename(columns={'Overall rank': 'Happiness Rank',
                           'Country or region': 'Country',
                           'Score': 'Happiness Score',
                           'Healthy life expectancy': 'Life Expectancy',
                           'Freedom to make life choices': 'Freedom',
                           'Perceptions of corruption': 'Corruption'}, inplace=True)

# MANIPULATING THE COLUMN NAMES OF data2020.csv ----
data_set_6.rename(columns={'Country name': 'Country',
                           'Regional indicator': 'Region',
                           'Ladder score': 'Happiness Score',
                           'Standard error of ladder score': 'Standard error of Happiness Score',
                           'Logged GDP per capita': 'log of GDP per capita',
                           'Healthy life expectancy': 'Life Expectancy',
                           'Perceptions of corruption': 'Corruption',
                           'Ladder score in Dystopia': 'Dystopia Residual',
                           'Socia support': 'Social Support',
                           'Explained by: Log GDP per capita': 'Explained by: log of GDP per capita',
                           'Explained by: Social support': 'Explained by: Social Support',
                           'Explained by: Healthy life expectancy': 'Explained by: Life Expectancy',
                           'Explained by: Freedom to make life choices': 'Explained by: Freedom',
                           'Explained by: Perceptions of corruption': 'Explained by: Corruption',
                           'Dystopia + residual': 'Explained by: Dystopia Residual',
                           'Freedom to make life choices': 'Freedom'}, inplace=True)
data_set_6.drop(['upperwhisker', 'lowerwhisker'], axis='columns', inplace=True)

# MANIPULATING THE COLUMN NAMES OF data2021.csv ----
data_set_7.rename(columns={'Country name': 'Country',
                           'Regional indicator': 'Region',
                           'Ladder score': 'Happiness Score',
                           'Standard error of ladder score': 'Standard error of Happiness Score',
                           'Logged GDP per capita': 'log of GDP per capita',
                           'Healthy life expectancy': 'Life Expectancy',
                           'Perceptions of corruption': 'Corruption',
                           'Freedom to make life choices': 'Freedom',
                           'Ladder score in Dystopia': 'Dystopia Residual',
                           'Socia support': 'Social Support',
                           'Explained by: Log GDP per capita': 'Explained by: log of GDP per capita',
                           'Explained by: Social support': 'Explained by: Social Support',
                           'Explained by: Healthy life expectancy': 'Explained by: Life Expectancy',
                           'Explained by: Freedom to make life choices': 'Explained by: Freedom',
                           'Explained by: Perceptions of corruption': 'Explained by: Corruption',
                           'Dystopia + residual': 'Explained by: Dystopia Residual'}, inplace=True)
data_set_7.drop(['upperwhisker', 'lowerwhisker'], axis='columns', inplace=True)

# HEATMAP OF data_set_6 ----
plt.figure(figsize=(20, 20))
plt.title('Heatmap of World Happiness Report 2020', fontweight='bold')
sns.heatmap(data_set_6.corr())
plt.show()

# HEATMAP data_set_7 ----
plt.figure(figsize=(20, 20))
plt.title('Heatmap of World Happiness Report 2021', fontweight='bold')
sns.heatmap(data_set_7.corr())
plt.show()

# REMOVING THOSE EXTRA SET OF COLUMNS AS THEY ARE NOTING BUT THE SCALED VERSIONS OF THOER COLUMNS ----
data_set_6.drop(['Explained by: log of GDP per capita',
                 'Explained by: Social Support', 'Explained by: Life Expectancy',
                 'Explained by: Freedom', 'Explained by: Generosity',
                 'Explained by: Corruption', 'Explained by: Dystopia Residual'], axis='columns', inplace=True)
data_set_7.drop(['Explained by: log of GDP per capita',
                 'Explained by: Social Support', 'Explained by: Life Expectancy',
                 'Explained by: Freedom', 'Explained by: Generosity',
                 'Explained by: Corruption', 'Explained by: Dystopia Residual'], axis='columns', inplace=True)

# CREATING 'GDP/capita' COLUMN FROM 'GDP per capita' AND 'log GDP per capita' columns ----
data_set_1['GDP/capita'] = np.exp(data_set_1['GDP per capita'])
data_set_2['GDP/capita'] = np.exp(data_set_1['GDP per capita'])
data_set_3['GDP/capita'] = np.exp(data_set_1['GDP per capita'])
data_set_4['GDP/capita'] = np.exp(data_set_1['GDP per capita'])
data_set_5['GDP/capita'] = np.exp(data_set_1['GDP per capita'])
data_set_6['GDP/capita'] = np.exp(data_set_6['log of GDP per capita'])
data_set_7['GDP/capita'] = np.exp(data_set_7['log of GDP per capita'])

# DELETING 'GDP per capita' AND 'log of GDP per capita' FROM THE DATAFRAMES ----
data_set_1.drop('GDP per capita', axis='columns', inplace=True)
data_set_2.drop('GDP per capita', axis='columns', inplace=True)
data_set_3.drop('GDP per capita', axis='columns', inplace=True)
data_set_4.drop('GDP per capita', axis='columns', inplace=True)
data_set_5.drop('GDP per capita', axis='columns', inplace=True)
data_set_6.drop('log of GDP per capita', axis='columns', inplace=True)
data_set_7.drop('log of GDP per capita', axis='columns', inplace=True)

# ADDING 'Year' COLUMN TO EACH DATAFRAME ----
data_set_1['Year'] = 2015
data_set_2['Year'] = 2016
data_set_3['Year'] = 2017
data_set_4['Year'] = 2018
data_set_5['Year'] = 2019
data_set_6['Year'] = 2020
data_set_7['Year'] = 2021

# REMOVING 'region' COLUMN FROM EVERY DATAFRAME ----
data_set_1.drop('Region', axis='columns', inplace=True)
data_set_2.drop('Region', axis='columns', inplace=True)
data_set_6.drop('Region', axis='columns', inplace=True)
data_set_7.drop('Region', axis='columns', inplace=True)

# ADDING 'Happiness Rank' COLUMN IN THE DATAFRAME OF 2020 AND 2021 WORLD HAPPINESS REPORT ----
data_set_6 = data_set_6.sort_values('Happiness Score', ascending=False)
data_set_6['Happiness Rank'] = data_set_6.index + 1
data_set_7 = data_set_7.sort_values('Happiness Score', ascending=False)
data_set_7['Happiness Rank'] = data_set_7.index + 1

# CHECKING FOR COMMON COLUMNS IN ALL DATAFRAMES ----
colSet_1 = set(data_set_1.columns)
colSet_2 = set(data_set_2.columns)
colSet_3 = set(data_set_3.columns)
colSet_4 = set(data_set_4.columns)
colSet_5 = set(data_set_5.columns)
colSet_6 = set(data_set_6.columns)
colSet_7 = set(data_set_7.columns)
commonCol = list(colSet_1.intersection(colSet_2, colSet_3, colSet_4, colSet_5, colSet_6, colSet_7))

# CREATING NEW DATAFRAMES WITH COMMON COLUMNS ----
data_set_filtered_1 = data_set_1[commonCol]
data_set_filtered_2 = data_set_2[commonCol]
data_set_filtered_3 = data_set_3[commonCol]
data_set_filtered_4 = data_set_4[commonCol]
data_set_filtered_5 = data_set_5[commonCol]
data_set_filtered_6 = data_set_6[commonCol]
data_set_filtered_7 = data_set_7[commonCol]

# CREATING THE FINAL DATAFRAME ----
data_set = pd.concat([data_set_filtered_1, data_set_filtered_2, data_set_filtered_3, data_set_filtered_4,
                      data_set_filtered_5, data_set_filtered_6, data_set_filtered_7], axis=0)

# REINDEXING COLUMNS AND ROWS ----
col_order = ["Country", "Year", "Happiness Rank", "Happiness Score", "Freedom", "Generosity", "Life Expectancy",
             "GDP/capita", "Corruption"]
data_set = data_set.reindex(columns=col_order)
data_set.insert(0, 'Index', range(0, 0 + len(data_set)))
data_set.set_index('Index', inplace=True)

# SAVING THE FINAL DATAFRAME ----
data_set.to_csv('World_Happiness_Report_Cleaned.csv')
