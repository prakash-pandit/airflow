from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import dummyOperator

default_args = {
    schedule_interval = '0 7 * * *',
    start_date = datetime.strptime('2024-05-31', 'YYYY-MM-dd'),
    tags = ['test_dag'],
    catchup = True
}

dag = DAG(
    default_args = default_args,
)

start = dummyOperator(
    task_id = 'Start',
    dag = dag
)

end = DummyOperator(
    task_id = 'END',
    dag = dag
)

start >> end
from exampledag import examples_astronauts