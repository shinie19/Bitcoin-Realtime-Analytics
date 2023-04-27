from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from kafka import KafkaProducer
import requests
import json
import re

KAFKA_HOST_IP = "kafka"
KAFKA_PORT = "9092"
TOPIC = "coin_data"


def serializer(message):
    return json.dumps(message).encode('utf-8')


dag = DAG(
    dag_id='coin_price_crawling',
    # schedule_interval=None,
    schedule_interval='*/1 * * * *',
    start_date=datetime(2023, 4, 24),
    catchup=False,
    tags=['production'])


# Create Message sample
def generate_message():
    coins = ["BTC", "ETH", "BNB", "SOL", "XRP"]
    coin_data = []
    for coin in coins:
        res = requests.get(f'https://www.binance.com/en/trade/{coin}_USDT')
        coin_price = float(re.findall(
            rf'\d+.\d+ | {coin}USDT', res.text)[0].split(" ")[0])
        now = datetime.now()
        id = now.strftime('%Y%m%d%H%M%S%f')
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        # coin_data.append(
        #     {'id': id, 'Symbol': coin, 'Price': coin_price, 'Update_at': dt_string})

        coin_data.append({
            "schema": {
                "name": "coin_data",
                "type": "struct",
                "fields": [
                    {"field": "id", "type": "string"},
                    {"field": "Symbol", "type": "string"},
                    {"field": "Price", "type": "float"},
                    {"field": "Update_at", "type": "string"}
                ]
            },
            "payload": {
                "id": id,
                "Symbol": coin,
                "Price": coin_price,
                "Update_at": dt_string
            }
        })
        res.close()

    return coin_data


def demo_func():
    producer = KafkaProducer(
        bootstrap_servers=[f'{KAFKA_HOST_IP}:{KAFKA_PORT}'], value_serializer=serializer)

    messages = generate_message()
    for item in messages:
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(item)}')
        producer.send(TOPIC, value=item)


producer_task = PythonOperator(
    task_id="producer",
    provide_context=True,
    python_callable=demo_func,
    dag=dag
)

producer_task
