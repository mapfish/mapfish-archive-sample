#!/bin/bash

set -e

export DBNAME="v2.0_mapfishsample"
export DBUSER="www-data"
export PG_VERSION="8.3"


#
# Unless you know what you're doing do not modify anything
# beyond this comment.
#

dbname=${DBNAME}
dbuser=${DBUSER}
pg_version=${PG_VERSION}
dirname=$(dirname $0)

# do not add the .shp extension for the shapefile name
shapefiles="poi_osm"

usage() {
    echo "Usage: $0 [-p|--populate] [-d|--drop]"
    exit 1
}

import_shapefile() {
    shapefile=$1
    echo ${shapefile}
    if [[ -f ${shapefile}.shp ]]; then
        shp2pgsql -s 900913 -I -W UTF8 ${shapefile}.shp public.${shapefile} | psql -d ${dbname}
    fi
}

# check options
while getopts "dp" opt; do
    case $opt in
    d) drop=1 ;;
    p) populate=1 ;;
    esac
done

if [[ -n ${drop} ]]; then
    dropdb ${dbname}
fi

createdb -E unicode ${dbname}
createlang plpgsql ${dbname}

psql -d ${dbname} < "/usr/share/postgresql-${pg_version}-postgis/lwpostgis.sql"
psql -d ${dbname} < "/usr/share/postgresql-${pg_version}-postgis/spatial_ref_sys.sql"

psql -c "GRANT ALL ON DATABASE \"${dbname}\" TO \"${dbuser}\";"
psql -d ${dbname} -c "GRANT ALL ON TABLE geometry_columns TO \"${dbuser}\";"
psql -d ${dbname} -c "GRANT ALL ON TABLE spatial_ref_sys TO \"${dbuser}\";"

if [[ -n ${populate} ]]; then
    for shapefile in ${shapefiles}; do
	import_shapefile "${shapefile}"
    done
fi

exit 0
