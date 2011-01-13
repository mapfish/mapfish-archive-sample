import logging

from pylons import request, response, config, tmpl_context as c
from pylons.controllers.util import abort
from pylons.i18n import set_lang

from mapfishsample.lib.base import BaseController, render

log = logging.getLogger(__name__)

class EntryController(BaseController):

    def __before__(self):
        c.debug = "debug" in request.params
        c.lang = str(request.params.get("lang", config.get("default_lang")))
        set_lang(c.lang, fallback=True)

    def index(self):
        return render("index.html")

    def apiloader(self):
        return render("apiloader.js")

    def apihelp(self):
        return render("apihelp.html")
