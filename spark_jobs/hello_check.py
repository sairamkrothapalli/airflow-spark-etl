from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="hello_check",
    start_date=datetime(2025, 7, 30),
    schedule=None,      # <- modern param name
    catchup=False,
    description="Sanity check DAG",
) as dag:
    EmptyOperator(task_id="ping")