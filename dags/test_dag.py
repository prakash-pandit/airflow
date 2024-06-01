default_args = {
    schedule_interval = '0 7 * * *',
    tags = ['test_dag']
}

from exampledag import examples_astronauts