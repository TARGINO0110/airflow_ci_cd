from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime

# Defina o nome da sua DAG e a descrição
dag = DAG(
    dag_id = "unifametro_trabalho",
    start_date=datetime(2023, 9, 2),
    schedule_interval=None, 
    catchup=False,
)

# Operador para extrair dados
def extract_data():
    return {"dados": [1, 2, 3, 4, 5]}

extract_operator = PythonOperator(
    task_id="extract_data",
    python_callable=extract_data,
    dag=dag,
)

# Operador para transformar dados
def transform_data(**kwargs):
    ti = kwargs['ti']
    extracted_data = ti.xcom_pull(task_ids="extract_data")
    transformed_data = [x * 2 for x in extracted_data['dados']]
    return {"dados_transformados": transformed_data}

transform_operator = PythonOperator(
    task_id="transform_data",
    provide_context=True,
    python_callable=transform_data,
    dag=dag,
)

# Operador para carregar dados
def load_data(**kwargs):
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids="transform_data")
    print("Dados carregados:", transformed_data['dados_transformados'])
    print("Equipe: Luciano Pereira Targino, Samuel Porto, Raylson Brauna, Felipe Holanda")

load_operator = PythonOperator(
    task_id="load_data",
    provide_context=True,
    python_callable=load_data,
    dag=dag,
)

# Operador de término
end_operator = DummyOperator(task_id="end", dag=dag)

# Defina a ordem das tarefas
extract_operator >> transform_operator >> load_operator >> end_operator
