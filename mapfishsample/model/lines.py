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

from sqlalchemy import Column, types
from sqlalchemy.schema import Sequence

from geoalchemy import GeometryColumn, LineString, GeometryDDL

from mapfish.sqlalchemygeom import GeometryTableMixIn
from mapfishsample.model.meta import Base

# dimension information array for Oracle
diminfo = "MDSYS.SDO_DIM_ARRAY("\
            "MDSYS.SDO_DIM_ELEMENT('LONGITUDE', -180, 180, 0.000000005),"\
            "MDSYS.SDO_DIM_ELEMENT('LATITUDE', -90, 90, 0.000000005)"\
            ")"

class Line(Base, GeometryTableMixIn):
    __tablename__ = 'lines_tab'
    
    id = Column(types.Integer, Sequence('lines_tab_id_seq'), primary_key=True)
    name = Column(types.String(30), default = 'foo')
    the_geom = GeometryColumn(LineString(dimension=2, srid=4326, diminfo=diminfo))

GeometryDDL(Line.__table__)
