"""Setup the MapFishSample application"""
import logging

from mapfishsample.config.environment import load_environment
from mapfishsample.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup mapfishsample here
    This method can be executed by calling:
    
    paster setup-app development.ini [--name=main_pylons]
    """
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables for the editing example (if they aren't there already)
    meta.metadata.create_all(bind=meta.engine)
