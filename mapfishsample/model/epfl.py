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

from geoalchemy import GeometryColumn, Geometry

from mapfish.sqlalchemygeom import GeometryTableMixIn
from mapfishsample.model.meta import Session, Base

from geojson import Feature
from shapely.wkb import loads

class Node(Base, GeometryTableMixIn):
    __tablename__ = 'nodes2'
    __table_args__ = {
            'autoload' : True,
            'autoload_with' : Session.bind
        }
    
    geom = GeometryColumn(Geometry(dimension=2, srid=4326))
    
    def toFeature(self):
        geometry = loads(str(self.geom.geom_wkb))
        return Feature(id=int(self.node_id), geometry=geometry,
            properties={'room': str(self.room), 'floor': str(self.level)})



class Line(Base, GeometryTableMixIn):
    __tablename__ = 'lines2'
    __table_args__ = {
            'autoload' : True,
            'autoload_with' : engine
        }
    
    geom = GeometryColumn(Geometry(dimension=2, srid=4326))
    
    def toFeature(self):
        geometry = loads(str(self.geom.geom_wkb))
        return Feature(id=int(self.gid), geometry=geometry,
            properties={'distance': float(self.length)})

