import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id="cratedb_table_export",
    start_date=datetime.datetime(2021, 11, 11),
    schedule_interval="@hourly",
    catchup=False,
) as dag:
    PostgresOperator(
        task_id="copy_to",
        postgres_conn_id="cratedb_connection",
        sql="""
           COPY telegraf.metrics TO DIRECTORY 's3://ACCESS_KEY:SECRET_KEY@crate-astro-tutorial/data';
          """,
    )