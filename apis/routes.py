from flask import Flask, request, jsonify
from kafka import KafkaProducer
import pandas as pd
import time
import json


app = Flask(__name__)

encoder = lambda x: json.dumps(x).encode('utf-8') 


@app.route("/produce", methods=["POST"])
def produce():
    producer = KafkaProducer(bootstrap_servers="localhost:9092", value_serializer=encoder)
    df = pd.read_csv("data/GlobalWeatherRepository.csv")
    for _, row in df.iterrows():
        producer.send("global_weather", value=row.to_json())
        time.sleep(1)
    producer.flush()
    return jsonify({"message": "Data sent to Kafka"})





