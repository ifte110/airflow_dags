from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "test-0405203122",
}

dag = DAG(
    "test-0405203122",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.7.0 pipeline editor using `test.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: C:\Users\HP\Documents\Elyra Project/hello_world.py
op_a803236c_50c7_4f68_80af_890afc95f650 = KubernetesPodOperator(
    name="hello_world",
    namespace="airflow",
    image="ifte110/cloudcompare-simple-artifact:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.7.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.7.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://localhost:9000 --cos-bucket my-bucket --cos-directory 'test-0405203122' --cos-dependencies-archive 'hello_world-a803236c-50c7-4f68-80af-890afc95f650.tar.gz' --file 'C:\Users\HP\Documents\Elyra Project/hello_world.py' "
    ],
    task_id="hello_world",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "ouFAd4TlQySlgTl97Y7L",
        "AWS_SECRET_ACCESS_KEY": "TfzOzASVgjgSoRlO1xNQACoAiB16uWmQT7O9s786",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "test-0405203122-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_a803236c_50c7_4f68_80af_890afc95f650.image_pull_policy = "IfNotPresent"


# Operator source: C:\Users\HP\Documents\Elyra Project/knock_knock.py
op_191d79bb_37cc_4abb_9c1e_0e405adb99b5 = KubernetesPodOperator(
    name="knock_knock",
    namespace="airflow",
    image="ifte110/cloudcompare-simple-artifact:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.7.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.7.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://localhost:9000 --cos-bucket my-bucket --cos-directory 'test-0405203122' --cos-dependencies-archive 'knock_knock-191d79bb-37cc-4abb-9c1e-0e405adb99b5.tar.gz' --file 'C:\Users\HP\Documents\Elyra Project/knock_knock.py' "
    ],
    task_id="knock_knock",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "ouFAd4TlQySlgTl97Y7L",
        "AWS_SECRET_ACCESS_KEY": "TfzOzASVgjgSoRlO1xNQACoAiB16uWmQT7O9s786",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "test-0405203122-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_191d79bb_37cc_4abb_9c1e_0e405adb99b5.image_pull_policy = "IfNotPresent"

op_191d79bb_37cc_4abb_9c1e_0e405adb99b5 << op_a803236c_50c7_4f68_80af_890afc95f650
