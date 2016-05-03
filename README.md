# MapFishSample

/!\ This repository is deprecated. See http://mapfish.org or http://mapfish.github.io/mapfish-website.


MapFishSample is a MapFish application. The goal of this sample application is twofold:

* provide a demo on http://demo.mapfish.org
* provide some sample code for application developers

## Install

MapFishSample is built and deployed using zc.buildout
(http://www.buildout.org/).

For now the only way to install MapFishSample is from its sources
(MapFishSample isn't distributed on <http://pypi.python.org>).

Get the sources:
`$ svn co http://svn.mapfish.org/svn/mapfish/sample/trunk/ MapFishSample`

Build the buildout environment:
```
$ cd MapFishSample
$ python bootstrap.py --distribute --version 1.5.2
```
Build and deploy the application:
`$ buildout/bin/buildout -c buildout_dev.cfg`

When buildout_dev.cfg is used on the buildout command line the application will
use http://demo.mapfish.org/mapfishsample/2.0/mapserv as the WMS URL. To use
a local mapserv use buildout_main.cfg. The latter is what we use when deploying
MapFishSample on demo.mapfish.org.

## Run

To run MapFishSample in the Paste HTTP Server use this:

`$ buildout/bin/paster serve --reload development.ini`

To run MapFishSample in Apache mod_wsgi look at the apache/README.txt file.
