# script to pull data from source table, contactenate/hash a subset of datapoints and deposit into dest table

import bonobo
import hashlib
from bonobo.config import use, Service
from bonobo.constants import NOT_MODIFIED
from models.source.source_tbls import DetailedRegistration
from models.dest.hash_log_tbl import HashLogTable

@use('source_session')
def ExtractData(source_session):
    """Retrieve values to hash from detailed_registration table"""

    # pull top 100 records
    whole_table = source_session.query(DetailedRegistration).limit(100)
    for data_record in whole_table:
        yield data_record

@use('dest_session')
def MapData(data_record, dest_session):
    """Map data to hash_log table"""

    # add records to hash_log table
    record_row = HashLogTable(
        hash_value = data_record.id,
        email = data_record.email
    )
    return record_row

@use('dest_session')
def LoadData(data_record, dest_session):
    """Load data to hash_log table"""

    dest_session.add(record_row)

    yield NOT_MODIFIED

def GetGraph():
    graph = bonobo.Graph()
    graph.add_chain(ExtractData)
    graph.add_chain(LoadData, _input=None)
    graph.add_chain(MapData, _input=ExtractData, _output=LoadData)
