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

from sqlalchemy import types, Column

from geoalchemy import GeometryColumn, Geometry

from mapfish.sqlalchemygeom import GeometryTableMixIn
from mapfishsample.model.meta import engine, Base


class Country(Base, GeometryTableMixIn):
    __tablename__ = 'world_factbk_simplified'
    __table_args__ = {
            'autoload' : True,
            'autoload_with' : engine
        }
    
    # force SQLAlchemy not to use Decimals, see https://trac.mapfish.org/trac/mapfish/ticket/185
    birth_rt = Column(types.Numeric(asdecimal=False))
    death_rt = Column(types.Numeric(asdecimal=False))
    fertility = Column(types.Numeric(asdecimal=False))
    
    simplify = GeometryColumn(Geometry(dimension=2, srid=4326))

