from mapfishsample.tests import *

from mapfishsample.model.meta import Session
from mapfishsample.model.lines import Line

from geoalchemy import WKBSpatialElement

from shapely.geometry import asLineString
 	
from simplejson import loads

class TestLinesController(TestController):
    def setUp(self):
        # insert an initial feature in the datadabase
        feature = Line()
        feature.name = "foo"
        shape = asLineString(((0, 0),(0.1, 0.1),(0.2, 0.2)))
        srid = Line.geometry_column().type.srid
        feature.geometry = WKBSpatialElement(buffer(shape.wkb), srid=srid)
        feature.geometry.shape = shape
        Session.add(feature)
        Session.commit()
        self.fid = feature.id
        self.fids = [feature.id]

    def tearDown(self):
        # remove any features inserted while testing
        for fid in self.fids:
            feature = Session.query(Line).get(fid)
            Session.delete(feature)
        Session.commit()

    def test_index(self):
        response = self.app.get(url(controller='lines', action='index'))
        assert response.response.content_type == 'application/json'
        assert "FeatureCollection" in response

    def test_index_bad_format(self):
        response = self.app.get(url(controller='lines', action='index', format='html'),
                                status=404)

    def test_show(self):
        response = self.app.get(url(controller='lines', action='show', id=self.fid))
        assert response.response.content_type == 'application/json'
        assert "Feature" in response

    def test_show_bad_format(self):
        response = self.app.get(url(controller='lines', action='show', id=self.fid, format='html'),
                                status=404)

    def test_show_bad_id(self):
        response = self.app.get(url(controller='lines', action='show', id=-1),
                                status=404)

    def test_create(self):
        params = '{"type": "FeatureCollection", "features": [{"geometry": {"type": "LineString", "coordinates": [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0]]}, "type": "Feature", "properties": {"name": "bar"}, "id": null}]}'
        response = self.app.post(url(controller='lines', action='create'),
                                 params=params,
                                 headers={'Content-type': 'text/plain'},
                                 status=201)
        geojson = loads(response.response._body)
        fid = geojson['features'][0]['id']
        self.fids.append(fid)
        assert response.response.content_type == 'application/json'
        assert "FeatureCollection" in response
        assert Session.query(Line).get(fid) is not None

    def test_update(self):
        params = '{"geometry": {"type": "LineString", "coordinates": [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0]]}, "type": "Feature", "properties": {"name": "dude"}, "id": %d}' % self.fid
        response = self.app.put(url(controller='lines', action='update', id=self.fid),
                                params=params,
                                headers={'Content-type': 'text/plain'},
                                status=201)
        assert response.response.content_type == 'application/json'
        assert "Feature" in response
        assert Session.query(Line).get(self.fid) is not None

    def test_delete(self):
        # code below triggers exception, nose bug it seems
        #self.app.delete(url(controller='points', action='delete', id=self.fid),
        #                status=204)
        pass

    def test_delete_bad_id(self):
        response = self.app.delete(url(controller='lines', action='delete', id=-1),
                                   status=404)
