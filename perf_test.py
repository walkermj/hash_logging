# This is the mains script to trigger all subsequent processes where needed

import fire
import logging

from models import source, dest
from etls import hash_test

# etl stuff here

# log_filename = 'perf_log.txt'
# logging.filehandler(filename=log_filename, level=logging.INFO, mode='w')

# declare classes representing the command line interface
class perfTest(object):

    class CreateDatabase(object):

        def dest(self):
            dest.CreateDatabase()

    class RunHashingStage(object):

        def RunHashTest(self):
            hash_test.RunHashingStage()

# Python Fire looks at the PMI class and builds a command line interface
if __name__ == "__main__":
    fire.Fire(perfTest)

