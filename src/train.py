import joblib
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split


df = pd.read_csv('../data/FuelConsumptionCo2.csv')

x = df[['ENGINESIZE']]
y = df[['CO2EMISSIONS']]

train_engines, test_engines, train_co2, test_co2 = train_test_split(x, y, test_size=0.2, random_state=42)

model = linear_model.LinearRegression()
model.fit(train_engines, train_co2)

joblib.dump(model, '../models/model.pkl')

print('Model saved.')