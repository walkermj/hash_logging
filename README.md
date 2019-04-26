# hash_logging

## Synopsis

This is a template set up to test the performance of hashing and change push processes for a million records using SQLAlchemy ORM and postgres. 

## Setup

To begin with ensure that all python libraries contained within `requirements.txt` are installed in the environment you will be running this or within a venv.

  1) Source data to test this process is created by running [fake2db](https://github.com/emirozer/fake2db) with the following command: 
  
  * `fake2db --rows 1000000 --host localhost --port 5432 --db postgresql --user <postgres_username> --name perf_test`

 
 2) Then use [sqlaodegen](https://pypi.org/project/sqlacodegen/) to generate the declarative classes for the tables created by fake2db and deposit in `/models` folder

 
 3) Run the following command to create the output tables for this process within the postgres db:
  
  * `python3 perf_test.py CreateDatabase dest`

