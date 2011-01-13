from mapfishsample.tests import *

class TestPoisController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='pois'))
        # Test response...
