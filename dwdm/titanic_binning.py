import pandas as pd
from warnings import filterwarnings

filterwarnings('ignore')

dataset = pd.read_csv('titanic_train.csv')
