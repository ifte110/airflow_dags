import os
from airflow import DAG
from datetime import datetime, timedelta, timezone
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

def mesh_to_cloud():
    os.system('xvfb-run CloudCompare -SILENT -AUTO_SAVE OFF -O /tmp/panel_artec_scan.obj -SAMPLE_MESH POINTS 100 -SAVE_CLOUDS FILE /tmp/output.bin')

def cloud_ss():
    os.system('xvfb-run CloudCompare -SILENT -AUTO_SAVE OFF -O /tmp/output.bin -SS SPATIAL 0.1 -SAVE_CLOUDS FILE /airflow/xcom/return.json')


with DAG(
    'simple-cc-workflow',
    default_args=default_args,
    description= 'Simple dag script',
    start_date=datetime(2022, 1, 1),
    catchup=False,

) as dag:
 
 task_1 = PythonOperator(
     task_id='task_1',
     provide_context=True,
     python_callable=mesh_to_cloud,
     dag=dag,

 )

 task_2 = PythonOperator(
     task_id='task_2',
     do_xcom_push=True,
     python_callable=cloud_ss,
     dag=dag

 )

 task_1>>task_2
