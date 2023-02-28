from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from hello_world_operator import HelloWorldOperator


def helloWorld():
    print("Hello World")

# Cria uma DAG
with DAG(dag_id="hello_world_dag", # ID da DAG
         start_date=datetime(2021,1,1), # Data inicial(Usamos uma antiga para começar imediato)
         schedule_interval=None, # Frequencia do JOB
         catchup=False) as dag:
         
         # Cria uma TASK
         task1 = PythonOperator(
            task_id="hello_world",
            python_callable=helloWorld)

         task2 = HelloWorldOperator(task_id="primeiro-operator-task", name="hello_world_custom")

# Chama a task1 e depois a task2
task1 >> task2