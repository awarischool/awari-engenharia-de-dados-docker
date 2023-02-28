import requests
import os
import pandas as pd
from io import StringIO, BytesIO
from airflow.models import Variable

from datetime import datetime

from airflow.models.baseoperator import BaseOperator
from custom_s3_hook import CustomS3Hook
from airflow.providers.postgres.hooks.postgres import PostgresHook

class BIPgOperator(BaseOperator):
    def __init__(self, url: str, tablename: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.url = url
        self.tablename = tablename
        self.custom_s3 = CustomS3Hook(bucket=Variable.get("AWS_BUCKET"))
        self.pg_hook = PostgresHook(postgres_conn_id="pg_awari")
        self.pg_conn = self.pg_hook.get_conn()
        self.engine = self.pg_hook.get_sqlalchemy_engine()
        self.current_time = datetime.now()
        self.current_date = self.current_time .strftime("%Y-%m-%d")

    def execute(self, context):
        self.process_to_pg()
        return self.url

    def process_to_pg(self):
        print("Fazendo download do arquivo: " + self.url)
        
        csv = self.custom_s3.get_object(key=f"datalake/{self.url}")
        df = pd.read_csv(csv, header=0)
        df.to_sql(self.tablename, con=self.engine, if_exists='replace', index=False)


        

