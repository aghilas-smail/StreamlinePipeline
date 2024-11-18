from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airscholar', 
    'start_date': datetime(2024, 11, 14)
}

def stream_data():
    import json
    import requests
    
    res = requests.get("https://randomuser.me/api/")
    print(res.json())

# with DAG('user_automation', 
#          default_args=default_args,
#          schedule_interval='@daily',
#          # Le catchup signifie on prend pas en consédiration les exécutions manquantes 
#          catchup=False) as dag:

stream_data()