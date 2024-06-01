from datetime import datetime
from airflow import DAG

default_args = {
    schedule_interval = '0 7 * * *',
    start_date = datetime.strptime('2024-05-31', 'YYYY-MM-dd'),
    tags = ['test_dag'],
    catchup = True
}

dag = DAG(
    default_args = default_args,
)

from exampledag import examples_astronauts