# initialisation script for source to dest hashing process etl

import bonobo
import models.source
import models.dest

from . import hash_etl

def RunHash(source_session_factory, dest_session_factory, etl):

    # use session factories to get the sessions needed for this etl
    db_sessions = {
        "source_session": "source_session_factory()",
        "dest_session": "dest_session_factory()",
    }

    # ask etl for its graph of functions to run
    graph = etl.GetGraph()

    # then run the etl
    bonobo.run(graph, services=db_sessions)

    # tidy up sessions in this etl
    for session in db_sessions.values():
        session.commit()
        session.close()

def RunHashingStage():
    """Hash specified columns from source table, bring in email value and move to dest table"""

    # Get session factories for connecting to the database
    source_session_factory  = models.source.GetSession()
    dest_session_factory = models.dest.GetSession()
        
    # run the etl
    RunHash(source_session_factory, dest_session_factory, hash_etl)
