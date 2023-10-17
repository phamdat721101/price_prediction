from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta, timezone
# from pydantic import BaseModel
import json
# from flask import Flask, jsonify, request

# from model import convert, predict
import pandas as pd
import numpy as np

app = FastAPI()


# pydantic models


class StockIn():
    ticker: any


class StockOut(StockIn):
    forecast: dict


# routes

@app.get("/signal")
async def signal():
    df = pd.read_csv('signal.csv')
    timestamp = np.array(df['timestamp'])
    price = np.array(df['price'])

    resp = []
    for i in range(len(price)):
        response_object = {"timestamp": timestamp[i], "price": price[i]}
        resp.append(response_object)

    return resp

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


# @app.post("/predict", status_code=200)
# def get_prediction():
#     # ticker = payload.ticker

#     prediction_list = predict("ticker")
#     resp = []
#     prediction_list = prediction_list.tolist()

#     result = datetime.today()
#     tz = timezone(timedelta(hours=7))
#     for i in range(len(prediction_list)):
#         result += timedelta(minutes=1)
#         response_object = {"timestamp": result.astimezone(tz), "price": prediction_list[i][0]}
#         resp.append(response_object)
    
#     df = pd.DataFrame(resp)
#     df.to_csv("signal.csv", sep=',', index=False, encoding='utf-8')

#     # if not prediction_list:
#     #     raise HTTPException(status_code=400, detail="Model not found.")

#     # response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
#     # return resp
#     return [{"timestamp": result.astimezone(tz), "price":1.234}]