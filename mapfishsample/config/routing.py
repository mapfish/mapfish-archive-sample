"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('/', controller='entry', action='index')
    map.connect('/apiloader.js', controller='entry', action='apiloader')
    map.connect('/apihelp.html', controller='entry', action='apihelp')

    # FormAlchemy/GeoFormAlchemy routes
    map.connect('fa_static', '/admin/_static/{path_info:.*}', controller='admin', action='static')
    map.connect('admin', '/admin', controller='admin', action='models')
    map.connect('formatted_admin', '/admin.json', controller='admin', action='models', format='json')
    map.resource('model', 'models', path_prefix='/admin/{model_name}', controller='admin')

    # POI ws routes
    map.connect("/pois/count", controller="pois", action="count")
    map.resource("poi", "pois")

    # Uncomment this line if you need the OGC proxy in your application
    #map.connect('/ogcproxy', controller='ogcproxy', action='index')

    # TileCache route
    map.connect('/tilecache{path:.*?}', controller='tilecache', action='tilecache')

    return map
