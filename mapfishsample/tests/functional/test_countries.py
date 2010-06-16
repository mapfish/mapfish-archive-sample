from mapfishsample.tests import *

class TestCountriesController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='countries', action='index'))
