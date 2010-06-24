# 
# Copyright (C) 2007-2008  Camptocamp
#  
# This file is part of MapFish Server
#  
# MapFish is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# MapFish is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#  
# You should have received a copy of the GNU Lesser General Public License
# along with MapFish.  If not, see <http://www.gnu.org/licenses/>.
#

import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from geojson import FeatureCollection, dumps

from mapfish.plugins import pgrouting

from mapfishsample.lib.base import BaseController
from mapfishsample.model.meta import Session, engine
from mapfishsample.model.epfl import Node, Line

log = logging.getLogger(__name__)

class EpflController(BaseController):

    @jsonify
    def room(self):
        if 'query' in request.params:
            rooms = Session.query(Node).filter(Node.room.like(request.params['query'] + '%'))
            return {'results': [{'id': r.room, 'title': r.room} for r in rooms.order_by(Node.__table__.c.room)]}

    def routing(self):
        source_id = Session.query(Node).filter(Node.__table__.c.room == request.params['from'])[0].node_id
        target_id = Session.query(Node).filter(Node.__table__.c.room == request.params['to'])[0].node_id

        if 'disabled' in request.params and request.params['disabled'] == '1':
            """If a node is not suitable for disabled (type = '9.2'), it should not be taken into account for routing.
            Because pgrouting does not allow negative values as cost, we set the length to 'Infinity'.
            see also: http://pgrouting.postlbs.org/ticket/88
            """
            cost = "CASE WHEN type = '9.2' THEN 'Infinity'::float8 ELSE length::float8 END"
        else:
            cost = "length::float8"
            
        route = pgrouting.shortest_path(engine,
                                        "SELECT gid AS id, node1_id::int4 AS source, node2_id::int4 AS target, %(cost)s AS cost FROM lines2"%{'cost': cost},
                                        int(source_id), int(target_id)).fetchall()
        
        if route is None or len(route) <= 0:
            abort(400)
        
        source_f = Session.query(Node).filter(Node.node_id == route[0]['vertex_id']).first().toFeature()
        target_f = Session.query(Node).filter(Node.node_id == route[-1]['vertex_id']).first().toFeature()
        
        source_f.properties['_isSourceNode'] = True
        target_f.properties['_isTargetNode'] = True

        lines = [Session.query(Line).get(i['edge_id']) for i in route]
        result = FeatureCollection([line.toFeature() for line in lines if line is not None and line.geom is not None])

        result.features.extend([source_f, target_f])
        #length = sum([line.length for line in lines if line is not None])

        return dumps(result)
