import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from ds_convert_to_parquet_operator import ConvertToParquetOperator

URLS_IMDB = {
   'name_basics': 'name.basics.csv',
   'title_akas': 'title.akas.csv',
   'title_basics': 'title.basics.csv',
   'title_crew': 'title.crew.csv',
   'title_episode': 'title.episode.csv',
   'title_principals': 'title.principals.csv',
   'title_ratings': 'title.ratings.csv'
}


dag1 =  DAG(dag_id=f"ds_name_basics_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ConvertToParquetOperator(
   task_id=f"download_{URLS_IMDB['name_basics']}", url=URLS_IMDB['name_basics'],dag=dag1
)

trigger = TriggerDagRunOperator(
        task_id="trigger_bi_name_basics_dag",
        trigger_dag_id="bi_name_basics_dag", 
    )

# TASKS
download_task >> trigger

dag2 =  DAG(dag_id=f"ds_title_akas_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ConvertToParquetOperator(
   task_id=f"download_{URLS_IMDB['title_akas']}", url=URLS_IMDB['title_akas'],dag=dag2
)

trigger = TriggerDagRunOperator(
        task_id="trigger_bi_title_akas_dag",
        trigger_dag_id="bi_title_akas_dag", 
    )

# TASKS
download_task >> trigger


dag3 =  DAG(dag_id=f"ds_title_basics_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ConvertToParquetOperator(
   task_id=f"download_{URLS_IMDB['title_basics']}", url=URLS_IMDB['title_basics'],dag=dag3
)

trigger = TriggerDagRunOperator(
        task_id="trigger_bi_title_basics_dag",
        trigger_dag_id="bi_title_basics_dag", 
    )

# TASKS
download_task >> trigger

dag4 =  DAG(dag_id=f"ds_title_crew_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ConvertToParquetOperator(
   task_id=f"download_{URLS_IMDB['title_crew']}", url=URLS_IMDB['title_crew'],dag=dag4
)

trigger = TriggerDagRunOperator(
        task_id="trigger_bi_title_crew_dag",
        trigger_dag_id="bi_title_crew_dag", 
    )

# TASKS
download_task >> trigger

dag5 =  DAG(dag_id=f"ds_title_episode_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ConvertToParquetOperator(
   task_id=f"download_{URLS_IMDB['title_episode']}", url=URLS_IMDB['title_episode'],dag=dag5
)

trigger = TriggerDagRunOperator(
        task_id="trigger_bi_title_episode_dag",
        trigger_dag_id="bi_title_episode_dag", 
    )

# TASKS
download_task >> trigger

dag6 =  DAG(dag_id=f"ds_title_principals_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ConvertToParquetOperator(
   task_id=f"download_{URLS_IMDB['title_principals']}", url=URLS_IMDB['title_principals'],dag=dag6
)

trigger = TriggerDagRunOperator(
        task_id="trigger_bi_title_principals_dag",
        trigger_dag_id="bi_title_principals_dag", 
    )

# TASKS
download_task >> trigger

dag7 =  DAG(dag_id=f"ds_title_ratings_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ConvertToParquetOperator(
   task_id=f"download_{URLS_IMDB['title_ratings']}", url=URLS_IMDB['title_ratings'],dag=dag7
)

trigger = TriggerDagRunOperator(
        task_id="trigger_bi_title_ratings_dag",
        trigger_dag_id="bi_title_ratings_dag", 
    )

# TASKS
download_task >> trigger
