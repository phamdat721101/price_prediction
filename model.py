import datetime
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler

import numpy as np
import joblib
import pandas as pd
import yfinance as yf
from prophet import Prophet

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

BASE_DIR = Path(__file__).resolve(strict=True).parent
TODAY = datetime.date.today()

def new_dataset(dataset, step_size):
	data_X, data_Y = [], []
	for i in range(len(dataset)-step_size-1):
		a = dataset[i:(i+step_size), 0]
		data_X.append(a)
		data_Y.append(dataset[i + step_size, 0])
	return np.array(data_X), np.array(data_Y)

def build_model():
    # Initialising the RNN
    regressor = Sequential()
    
    # Adding the First input hidden layer and the LSTM layer
    # return_sequences = True, means the output of every time step to be shared with hidden next layer
    regressor.add(LSTM(units = 10, activation = 'relu', input_shape = (TimeSteps, TotalFeatures), return_sequences=True))
    
    # Adding the Second Second hidden layer and the LSTM layer
    regressor.add(LSTM(units = 5, activation = 'relu', input_shape = (TimeSteps, TotalFeatures), return_sequences=True))
    
    # Adding the Second Third hidden layer and the LSTM layer
    regressor.add(LSTM(units = 5, activation = 'relu', return_sequences=False ))
    
    
    # Adding the output layer
    regressor.add(Dense(units = 1))
    
    # Compiling the RNN
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    return regressor

def train(model):
    dataset = pd.read_csv('eur_usd.csv', usecols=[4])
    # dataset = dataset.reindex(index = dataset.index[::-1])
    price_test = dataset
    price_test = np.reshape(price_test.values, (len(price_test), 1))
    scaler = MinMaxScaler(feature_range=(0,1))
    price_test = scaler.fit_transform(price_test)

    trainX, trainY =new_dataset(price_test, 1)
    model.fit(trainX, trainY, batch_size = 3, epochs = 60)
    return model

def predict(ticker="MSFT", days=7):
    dataset = pd.read_csv('EURUSD_M5.csv', encoding='utf-8')
    dataset = dataset['<CLOSE>']
    datatrain = np.reshape(datatrain.values, (len(datatrain), 1))
    scaler = MinMaxScaler(feature_range=(0,1))
    datatrain = scaler.fit_transform(datatrain)

    #building model 
    # Initialising the RNN
    model = Sequential()
    
    # Adding the First input hidden layer and the LSTM layer
    # return_sequences = True, means the output of every time step to be shared with hidden next layer
    model.add(LSTM(units = 10, activation = 'relu', input_shape = (1, 1), return_sequences=True))
    
    # Adding the Second Second hidden layer and the LSTM layer
    model.add(LSTM(units = 5, activation = 'relu', input_shape = (1, 1), return_sequences=True))
    
    # Adding the Second Third hidden layer and the LSTM layer
    model.add(LSTM(units = 5, activation = 'relu', return_sequences=False ))
    
    
    # Adding the output layer
    model.add(Dense(units = 1))
    
    # Compiling the RNN
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')

    #train to fit model 
    trainX, trainY =new_dataset(datatrain, 1)
    model.fit(trainX, trainY, batch_size = 3, epochs = 3)

    test_data = pd.read_csv('eur_usd_test.csv', usecols=[4])
    # test_data = test_data.reindex(index = test_data.index[::-1])
    price_test = test_data
    price_test = np.reshape(price_test.values, (len(price_test), 1))
    scaler = MinMaxScaler(feature_range=(0,1))
    price_test = scaler.fit_transform(price_test)
    price_test = np.reshape(price_test, (price_test.shape[0], 1, price_test.shape[1]))

    pricePredict = model.predict(price_test)
    pricePredict = scaler.inverse_transform(pricePredict)
    print("Price predict: ", pricePredict, " -length: ", len(pricePredict))
    return pricePredict

def convert(prediction_list):
    dataset = pd.read_csv('eur_usd.csv', usecols=[0])
    resp = []
    output = {}
    for i in range(len(prediction_list)):
        date = "2023-10-09T01:37:00.000Z"
        output['price'] = prediction_list[i][0]
        output['time'] = 1
        resp.append(output)
    
    return resp
