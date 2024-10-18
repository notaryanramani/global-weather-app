from apis.utils import download_data, start_kafka_server
from kafka import KafkaConsumer
import streamlit as st
import requests
import matplotlib.pyplot as plt
import json
import pandas as pd

decoder = lambda x: json.loads(x.decode('utf-8'))

def start():
    download_data()
    start_kafka_server()

def init_consumer():
    consumer = KafkaConsumer(
        'global_weather',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=decoder
    )
    return consumer

if 'started' not in st.session_state:
    start()
    st.session_state['started'] = True

if 'consumer' not in st.session_state:   
    st.session_state['consumer'] = init_consumer()

if 'temp_array' not in st.session_state:
    st.session_state['temp_array'] = []


st.title("Global Weather Data")

producer_button = st.button("Produce data")
if producer_button:
    requests.post("http://localhost:5001/produce")

placeholder = st.empty()

start_button = st.button("Consume data")
if start_button:
    consumer = st.session_state['consumer']
    for message in consumer:
        data = json.loads(message.value)
        temp = data["temperature_celsius"]
        st.session_state['temp_array'].append(temp)
        data = pd.DataFrame(st.session_state['temp_array'], columns=["Temperature"])
        placeholder.line_chart(data)
