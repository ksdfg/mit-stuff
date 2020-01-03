import graphviz
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz, DecisionTreeRegressor

data = pd.read_csv("temps.csv")
print(data)
print(data.shape)
print(data.describe())

data_dummy = pd.get_dummies(data, columns=['week'])
print(data_dummy)
y = data_dummy['actual']
data = data_dummy.drop('actual', axis=1)
feature_list = data_dummy.columns
x = data_dummy[feature_list]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.3)

dtr = DecisionTreeRegressor(criterion='mse', min_samples_leaf=10, max_depth=4)
dtr.fit(x_train, y_train)
y_pred = dtr.predict(x_test)
print(y_pred)
print(dtr.score(x_test, y_test))

dot_data = export_graphviz(dtr, out_file=None, feature_names=feature_list, class_names=data_dummy['actual'].unique(),
                           filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("temps_graph")
