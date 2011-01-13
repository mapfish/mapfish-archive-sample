from pylons import config
from mapfishsample import model
from mapfishsample.lib.base import render
from formalchemy import config as fa_config
from formalchemy import templates
from formalchemy import validators
from formalchemy import fields
from formalchemy import forms
from formalchemy import tables
from formalchemy.ext.fsblob import FileFieldRenderer
from formalchemy.ext.fsblob import ImageFieldRenderer

fa_config.encoding = 'utf-8'

class TemplateEngine(templates.TemplateEngine):
    def render(self, name, **kwargs):
        return render('/forms/%s.mako' % name, extra_vars=kwargs)
fa_config.engine = TemplateEngine()

class FieldSet(forms.FieldSet):
    pass

class Grid(tables.Grid):
    pass

## Initialize fieldsets

#Foo = FieldSet(model.Foo)
#Reflected = FieldSet(Reflected)

## Initialize grids

#FooGrid = Grid(model.Foo)
#ReflectedGrid = Grid(Reflected)

from geoformalchemy.base import GeometryFieldRenderer
from geoalchemy import geometry
FieldSet.default_renderers[geometry.Geometry] = GeometryFieldRenderer

Poi = FieldSet(model.Poi)
Poi.the_geom.set(options=[
    ('map_srid', 900913),
    ('base_layer', 'new OpenLayers.Layer.OSM("OSM")'),
    ('default_lon', 659202.486442),
    ('default_lat', 5710925.684904),
    ('zoom', 13),
    ])
