from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta, timezone
# from pydantic import BaseModel
import json
# from flask import Flask, jsonify, request

# from model import convert, predict

app = FastAPI()


# pydantic models


class StockIn():
    ticker: any


class StockOut(StockIn):
    forecast: dict


# routes


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.post("/predict", status_code=200)
def get_prediction():
    # ticker = payload.ticker

    # prediction_list = predict("ticker")
    # resp = []
    # prediction_list = prediction_list.tolist()

    result = datetime.today()
    tz = timezone(timedelta(hours=7))
    # for i in range(len(prediction_list)):
    #     result += timedelta(minutes=1)
    #     response_object = {"timestamp": result.astimezone(tz), "price": prediction_list[i][0]}
    #     resp.append(response_object)

    # if not prediction_list:
    #     raise HTTPException(status_code=400, detail="Model not found.")

    # response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    # return 
    return [{"timestamp": result.astimezone(tz), "price":1.234}]