import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from bi_pg_operator import BIPgOperator

URLS_IMDB = {
   'name_basics': 'name.basics.csv',
   'title_akas': 'title.akas.csv',
   'title_basics': 'title.basics.csv',
   'title_crew': 'title.crew.csv',
   'title_episode': 'title.episode.csv',
   'title_principals': 'title.principals.csv',
   'title_ratings': 'title.ratings.csv'
}


dag1 =  DAG(dag_id=f"bi_name_basics_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = BIPgOperator(
   task_id=f"download_{URLS_IMDB['name_basics']}", url=URLS_IMDB['name_basics'], tablename='name_basics', dag=dag1
)

# TASKS
download_task


dag2 =  DAG(dag_id=f"bi_title_akas_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = BIPgOperator(
   task_id=f"download_{URLS_IMDB['title_akas']}", url=URLS_IMDB['title_akas'], tablename='title_akas',dag=dag2
)

# TASKS
download_task


dag3 =  DAG(dag_id=f"bi_title_basics_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = BIPgOperator(
   task_id=f"download_{URLS_IMDB['title_basics']}", url=URLS_IMDB['title_basics'], tablename='title_basics',dag=dag3
)

# TASKS
download_task

dag4 =  DAG(dag_id=f"bi_title_crew_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = BIPgOperator(
   task_id=f"download_{URLS_IMDB['title_crew']}", url=URLS_IMDB['title_crew'], tablename='title_crew',dag=dag4
)

# TASKS
download_task

dag5 =  DAG(dag_id=f"bi_title_episode_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = BIPgOperator(
   task_id=f"download_{URLS_IMDB['title_episode']}", url=URLS_IMDB['title_episode'], tablename='title_episode',dag=dag5
)

# TASKS
download_task

dag6 =  DAG(dag_id=f"bi_title_principals_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = BIPgOperator(
   task_id=f"download_{URLS_IMDB['title_principals']}", url=URLS_IMDB['title_principals'], tablename='title_principals',dag=dag6
)

# TASKS
download_task

dag7 =  DAG(dag_id=f"bi_title_ratings_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = BIPgOperator(
   task_id=f"download_{URLS_IMDB['title_ratings']}", url=URLS_IMDB['title_ratings'], tablename='title_ratings',dag=dag7
)

# TASKS
download_task
