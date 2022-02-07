FROM  apache/airflow:2.2.3

COPY panel_artec_scan.obj /tmp/

USER root

RUN sudo apt-get update && apt-get install -y cloudcompare

RUN sudo apt-get update && apt-get install -y xvfb

USER airflow