"""The application's model objects"""

from sqlalchemy import Column, types

from geoalchemy import GeometryColumn, Point

from mapfish.sqlalchemygeom import GeometryTableMixIn
from mapfishsample.model.meta import Session, Base


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

    global Poi
    class Poi(Base, GeometryTableMixIn):
        __tablename__ = 'poi_osm'
        __table_args__ = {
            "autoload": True,
            "autoload_with": engine
        }
        the_geom = GeometryColumn(Point(srid=900913))
