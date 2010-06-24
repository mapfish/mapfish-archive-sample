"""Setup the MapFishSample application"""
import logging

import pylons

from mapfishsample.config.environment import load_environment
from mapfishsample.model.meta import Session, Base

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup mapfishsample here
    This method can be executed by calling:
    
    paster setup-app development.ini [--name=main_pylons]
    """
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables for the editing example (if they aren't there already)
    Base.metadata.create_all(bind=Session.bind)
