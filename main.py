from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
import json
from flask import Flask, jsonify, request

from model import convert, predict

app = Flask(__name__)


# pydantic models


class StockIn(BaseModel):
    ticker: str


class StockOut(StockIn):
    forecast: dict


# routes


@app.route("/ping", methods=['GET'])
async def pong():
    return jsonify({"ping": "pong!"})


@app.route("/predict", methods=['POST'])
def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = predict(ticker)
    resp = []
    prediction_list = prediction_list.tolist()

    result = datetime.today()
    tz = timezone(timedelta(hours=7))
    for i in range(len(prediction_list)):
        result += timedelta(minutes=1)
        response_object = {"timestamp": result.astimezone(tz), "price": prediction_list[i][0]}
        resp.append(response_object)

    # if not prediction_list:
    #     raise HTTPException(status_code=400, detail="Model not found.")

    # response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return resp

if __name__ == '__main__':
   app.run(port=5000)
