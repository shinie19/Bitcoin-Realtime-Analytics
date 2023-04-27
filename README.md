# Bitcoin Real-time Analytic with Airflow - Kafka - ClickHouse - Grafana
[![Airflow](https://img.shields.io/badge/Airflow-2.5.3-green)](https://airflow.apache.org/docs/)
[![Kafka](https://img.shields.io/badge/Kafka-7.0.9-blue)](https://kafka.apache.org/documentation/)
[![ClickHouse](https://img.shields.io/badge/ClickHouse-21.3.20-yellow)](https://clickhouse.com/docs/en/intro)
[![Posgresql](https://img.shields.io/badge/PosgreSQL-15.2-blue)](https://www.postgresql.org/)
[![Grafana](https://img.shields.io/badge/Grafana-9.5.1-orange)](https://grafana.com/docs/)

Project Bitcoin Realtime Analytic is a data analysis project that focuses on real-time Bitcoin analytics, utilizing modern tools and techniques such as Airflow, Kafka, Clickhouse, and Grafana.

Specifically, Bitcoin price and transaction data are collected using Kafka, then stored and processed using Clickhouse to ensure consistency and high performance. Airflow is used to schedule automated data processing tasks and manage the data processing pipeline. Finally, Grafana is used to visualize the data and provide reports to users.

## Screenshots

**View System**

![Screenshot 2023-04-27 155804](https://user-images.githubusercontent.com/57434654/234899987-4da121ad-92a3-4d2c-9c46-8c82a66669ee.png)

## Contents
- [Screenshots](#screenshots)
- [Example](#example)
    - [1. Install docker, docker-compose](https://github.com/apot-group/real-time-analytic#1-install-docker-and-docker-compose)
    - [2. Pull git repo](https://github.com/apot-group/real-time-analytic#2-pull-git-repo)
    - [3. Start Server](https://github.com/apot-group/real-time-analytic#3-start-server)
- [Contact Us](#contact-us)

## Example

### 1. Install Docker and Docker-compose

<a href="https://www.docker.com">https://www.docker.com/</a>

### 2. Pull git repo
```bash 
git clone https://github.com/apot-group/real-time-analytic.git
```

### 3. Start Server
```bash 
cd Bitcoin-Realtime-Analytics && docker-compose up -d
```

| Service               | URL                              | User/Password                                 |
| :-------------------: | :------------------------------: | :-------------------------------------------: |
| Airflow               | http://localhost:8080/           | admin/admin                                   |
| ClickHouse            | http://localhost:8123/           | default/''                                    |
| Grafana               | http://localhost:3000/           | admin/admin                                   |

### 3. Create Dashboard sample from ClickHouse streaming
 - Airflow DAG at airflow/dags/coin_crawling.py each one min sent message to Kafka 'coin_data' topic with data of list coin ['BTC', 'ETH', 'BNB', 'SOL', 'XRP'] the structure of data message like below.
```
   {
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
                "id": '202304250000000',
                "Symbol": 'BTC',
                "Price": 289689,
                "Update_at": '2023-04-25 00:00:00'
         }
    }
```

 - ClickHouse automatically load data from kafka ```kafka:9092```, choice ```coin_data``` topic and config data result table
 
![image](https://user-images.githubusercontent.com/57434654/234906786-f55d2f5d-41bb-4cb8-996f-7a299c547e09.png)

 - From Grafana add ClickHouse data source ```clickhouse:8123```. 
 - Create Chart and Dashboard on Grafana from ```coin_data``` table in ```coin_price_db``` database.
 - DONE ✨

## Contact me
- Email: info.nguyenngocanh@gmail.com - Anh Nguyen
