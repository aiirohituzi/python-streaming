import cherrypy
import os
from cherrypy.lib.static import serve_file

class Download:

    @cherrypy.expose
    def index(self, file_):
        tgt = os.path.abspath(os.path.join('./music', file_))
        return (serve_file(tgt, "application/x-download", "attachment"))

if __name__ == '__main__':
    cherrypy.quickstart(Download())