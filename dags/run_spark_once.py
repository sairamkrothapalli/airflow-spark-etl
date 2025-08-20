from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

# This DAG runs your Spark job once on demand (no schedule)
with DAG(
    dag_id="run_spark_once",
    start_date=datetime(2025, 7, 30),
    schedule_interval=None,
    catchup=False,
    description="Run a one-off Spark job via SparkSubmitOperator",
    tags=["spark", "etl"],
) as dag:

    run_spark = SparkSubmitOperator(
        task_id="spark_submit_etl",
        application="/opt/etl/etl_pipeline.py",  # <- your job inside container
        conn_id="spark_default",                  # configured via env in docker-compose
        # optional submit conf:
        application_args=[],
        jars="",
        packages="",
        executor_cores=1,
        executor_memory="1g",
        driver_memory="1g",
        verbose=True,
    )