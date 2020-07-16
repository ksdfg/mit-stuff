import pandas as pd
from warnings import filterwarnings
from sklearn import preprocessing as pp
from scipy import stats


filterwarnings('ignore')

dataset = pd.read_csv('titanic_train.csv')

print("Min Max : Before\n")
print(dataset[['PassengerId', 'Fare']], '\n')

mm_scaler = pp.MinMaxScaler()
dataset['fare_normalised_min_max'] = pd.DataFrame(mm_scaler.fit_transform(dataset[['Fare']].values.astype(float)))
print("Min Max : After\n")
print(dataset[['PassengerId', 'Fare', 'fare_normalised_min_max']], '\n')

print("Z score : Before\n")
print(dataset[['PassengerId', 'Fare']].sort_values(by='Fare'), '\n')

dataset['fare_normalised_z_score'] = stats.zscore(dataset['Fare'])
print("Z SCore : After\n")
print(dataset[['PassengerId', 'Fare', 'fare_normalised_z_score']], '\n')
