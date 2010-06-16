# 
# Copyright (C) 2007-2008  Camptocamp
#  
# This file is part of MapFish Server
#  
# MapFish Server is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# MapFish Server is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#  
# You should have received a copy of the GNU Lesser General Public License
# along with MapFish Server.  If not, see <http://www.gnu.org/licenses/>.
#

"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects.sqlite.base import SQLiteDialect
from sqlalchemy.interfaces import PoolListener

from geojson import Feature

from mapfishsample.model import meta

from mapfishsample.model.lines import Line
from mapfishsample.model.points import Point
from mapfishsample.model.polygons import Polygon

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    sm = orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)

    meta.engine = engine
    meta.Session = orm.scoped_session(sm)
    
    if isinstance(engine.dialect, SQLiteDialect):
        """If Spatialite is used as database, we have to make sure that
        every database connection created in the SQLAlchemy connection pool
        loads the Spatialite extension, before the connection is used.
        """
        class SpatialiteConnectionListener(PoolListener):
            def connect(self, dbapi_con, con_record):
                dbapi_con.enable_load_extension(True)
                dbapi_con.execute("select load_extension('/usr/local/lib/libspatialite.so')")
                dbapi_con.enable_load_extension(False)
                
        engine.pool.add_listener(SpatialiteConnectionListener()) 
        
