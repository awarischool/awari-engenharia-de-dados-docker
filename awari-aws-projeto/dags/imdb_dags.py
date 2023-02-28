import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from imdb_download_from_source_operator import ImdbDownloadFromSourceOperator

URLS_IMDB = {
   'name_basics': 'https://datasets.imdbws.com/name.basics.tsv.gz',
   'title_akas': 'https://datasets.imdbws.com/title.akas.tsv.gz',
   'title_basics': 'https://datasets.imdbws.com/title.basics.tsv.gz',
   'title_crew': 'https://datasets.imdbws.com/title.crew.tsv.gz',
   'title_episode': 'https://datasets.imdbws.com/title.episode.tsv.gz',
   'title_principals': 'https://datasets.imdbws.com/title.principals.tsv.gz',
   'title_ratings': 'https://datasets.imdbws.com/title.ratings.tsv.gz'
}


dag1 =  DAG(dag_id=f"ingest_name_basics_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ImdbDownloadFromSourceOperator(
   task_id=f"download_{os.path.basename(URLS_IMDB['name_basics'])}", url=URLS_IMDB['name_basics'],dag=dag1
)

trigger = TriggerDagRunOperator(
        task_id="trigger_ds_name_basics_dag",
        trigger_dag_id="ds_name_basics_dag", 
    )

# TASKS
download_task >> trigger

dag2 =  DAG(dag_id=f"ingest_title_akas_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ImdbDownloadFromSourceOperator(
   task_id=f"download_{os.path.basename(URLS_IMDB['title_akas'])}", url=URLS_IMDB['title_akas'],dag=dag2
)

trigger = TriggerDagRunOperator(
        task_id="trigger_ds_title_akas_dag",
        trigger_dag_id="ds_title_akas_dag", 
    )

# TASKS
download_task >> trigger

dag3 =  DAG(dag_id=f"ingest_title_basics_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ImdbDownloadFromSourceOperator(
   task_id=f"download_{os.path.basename(URLS_IMDB['title_basics'])}", url=URLS_IMDB['title_basics'],dag=dag3
)

trigger = TriggerDagRunOperator(
        task_id="trigger_ds_title_basics_dag",
        trigger_dag_id="ds_title_basics_dag", 
    )

# TASKS
download_task >> trigger

dag4 =  DAG(dag_id=f"ingest_title_crew_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ImdbDownloadFromSourceOperator(
   task_id=f"download_{os.path.basename(URLS_IMDB['title_crew'])}", url=URLS_IMDB['title_crew'],dag=dag4
)

trigger = TriggerDagRunOperator(
        task_id="trigger_ds_title_crew_dag",
        trigger_dag_id="ds_title_crew_dag", 
    )

# TASKS
download_task >> trigger

dag5 =  DAG(dag_id=f"ingest_title_episode_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ImdbDownloadFromSourceOperator(
   task_id=f"download_{os.path.basename(URLS_IMDB['title_episode'])}", url=URLS_IMDB['title_episode'],dag=dag5
)

trigger = TriggerDagRunOperator(
        task_id="trigger_ds_title_episode_dag",
        trigger_dag_id="ds_title_episode_dag", 
    )

# TASKS
download_task >> trigger

dag6 =  DAG(dag_id=f"ingest_title_principals_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ImdbDownloadFromSourceOperator(
   task_id=f"download_{os.path.basename(URLS_IMDB['title_principals'])}", url=URLS_IMDB['title_principals'],dag=dag6
)

trigger = TriggerDagRunOperator(
        task_id="trigger_ds_title_principals_dag",
        trigger_dag_id="ds_title_principals_dag", 
    )

# TASKS
download_task >> trigger

dag7 =  DAG(dag_id=f"ingest_title_ratings_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = ImdbDownloadFromSourceOperator(
   task_id=f"download_{os.path.basename(URLS_IMDB['title_ratings'])}", url=URLS_IMDB['title_ratings'],dag=dag7
)

trigger = TriggerDagRunOperator(
        task_id="trigger_ds_title_ratings_dag",
        trigger_dag_id="ds_title_ratings_dag", 
    )

# TASKS
download_task >> trigger
