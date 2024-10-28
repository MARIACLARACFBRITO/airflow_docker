from airflow import DAG
import pandas as pd
from datetime import datetime
import pendulum
from pymongo import MongoClient    #criar dockerfile para garantir que seja instalado o pymongo
from airflow.operators.python import PythonOperator
import os


def alimenta_bd():
    label = pd.read_csv('/data/Checkpoint5e6profTiago.csv')
    data_to_insert = label.to_dict(orient='records')
    client = MongoClient('mongodb://mongodb:27017/')
    db = client['banco_fiap']
    collection = db['info_cliente']
    collection.insert_many(data_to_insert)


default_args={
    'owner':'Maria Clara',
    'start_date':pendulum.datetime(2024,10,23),
    'retries':2,
}
with DAG('mongo_db',default_args=default_args) as dag:

    task_insert_data=PythonOperator(
        task_id='insert_mongodb',
        python_callable=alimenta_bd
    )




