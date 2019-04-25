# This is the mains script to trigger all subsequent processes where needed

import fire
import logging

from models import source, dest

# etl stuff here

log_filename = 'perf_log.txt'
logging.basicConfig(filename=log_filename, level=logging.INFO)

# declare classes representing the command line interface
class perfTest(object):

    class CreateDatabase(object):

        def dest(self):
            dest.CreateDatabase()

    class RunProcessingStage(object):

        def table_hash_process(self):
            source_to_dest.RunProcessingStage()

# Python Fire looks at the PMI class and builds a command line interface
if __name__ == "__main__":
    fire.Fire(perfTest)

