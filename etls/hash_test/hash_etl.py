# script to pull data from source table, contactenate/hash a subset of datapoints and deposit into dest table

import bonobo
import hashlib
from bonobo.config import use, Service
from bonobo.constants import NOT_MODIFIED
from models.source.source_tbls import DetailedRegistration
from models.dest.hash_log_tbl import HashLogTable

#define hash algorithm to be used 
h =  hashlib.md5

@use('source_session')
def ExtractData(source_session):
    """Retrieve values to hash from detailed_registration table"""

    # pull records
    whole_table = source_session.query(DetailedRegistration).order_by(DetailedRegistration.id).limit(1000000)
    for data_record in whole_table:
        yield data_record

@use('dest_session')
def MapData(data_record, dest_session):
    """Map data to hash_log table"""

# add records to hash_log table
    record_row = HashLogTable(
        hash_value = h(str(data_record.email+data_record.lastname+data_record.adress).encode()).hexdigest(),
        email = data_record.email
    )
    return record_row

@use('dest_session')
def LoadData(record_row, dest_session):
    """Load data to hash_log table if hash_value does not already exist in table"""

    record_exists = dest_session.query(HashLogTable).filter_by(hash_value=record_row.hash_value).first()
    if not record_exists:
        dest_session.add(record_row)

    yield NOT_MODIFIED

def GetGraph():
    graph = bonobo.Graph()
    graph.add_chain(ExtractData)
    graph.add_chain(LoadData, _input=None)
    graph.add_chain(MapData, _input=ExtractData, _output=LoadData)

    return graph
