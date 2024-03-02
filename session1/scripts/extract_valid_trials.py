import pandas as pd

df = pd.read_csv('C:/Users/sanan/OneDrive/Documents/iBOTS_Workshop_Git_Projects/iBOTS-Developing-Data-Analysis-Projects/session1/data/raw/session.csv')

ValidTrials = df.loc[df['valid'] == True]

