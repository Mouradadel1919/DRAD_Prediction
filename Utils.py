import pandas as pd
import numpy as np
import pickle
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


# IQR Function with quantiles (10, 90) 
def IQR(column_name, data):
    IQR = 0
    
    q1 = data[column_name].quantile(.10)
    q3 = data[column_name].quantile(.90)
    
    IQR= q3 - q1
    
    lower= q1 - 1.5 * IQR
    upper= q3 + 1.5 * IQR
    
    data.drop(data[((data[column_name] > upper) | (data[column_name] < lower))].index, inplace= True, axis=0)




trash = pd.read_excel("data.xlsx", header=1)
features = trash.iloc[:,:12]
target = trash.iloc[:,12]
df = pd.concat([features, target], axis=1)




df.drop(df[(df["DRAD"] > 3) | (df["DRAD"] < -3)].index, axis=0, inplace= True)





for num in range(2):
    for col in df.columns.to_list():
        IQR(col, df)
        
    df.reset_index(inplace=True, drop= True)





features = df.iloc[:,:-1]
target = df.iloc[:,-1]





x_train, X_test, y_train, Y_test = train_test_split(features, target, test_size=.2, random_state=42, shuffle=True)





pipeline = Pipeline([
    ("scaler", StandardScaler())
])
x_train_final = pipeline.fit_transform(x_train)




def preprocess_new(x_new):
    return pipeline.transform(x_new)


