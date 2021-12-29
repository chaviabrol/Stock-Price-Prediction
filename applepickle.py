import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pickle
regressor_f = open("Stock-Analyzer/stock_analyzer.pickle","rb")
regressor = pickle.load(regressor_f)
apple = pd.read_csv("https://raw.githubusercontent.com/arnavjune2/stock-analyzer/main/AAPL.csv" , index_col='Date')

sc = MinMaxScaler(feature_range = (0,1))
test_set = apple['Open'].iloc[9000:]
test_set = pd.DataFrame(test_set)
test_set = apple[len(apple)- len(test_set) -60:].values
test_set = test_set.reshape(-1,1)
test_set = sc.fit_transform(test_set,)
X_test = []
for i in range(60,80):
  X_test.append(test_set[i-60:i,0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)
print(predicted_stock_price)