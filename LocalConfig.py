from string import Template

databaseStringTemplate = 'postgresql+psycopg2://$username:$password@$server:$port/$database'


perftest_db_details = {"server": "127.0.0.1",
                     "port": "5432",
                     "username": "michaelwalker",
                     # "password": "password",
                     "database": "perf_test"
                     }

perftest_db_connection_string = Template(databaseStringTemplate).safe_substitute(perftest_db_details)

