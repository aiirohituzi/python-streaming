import cherrypy
import os
from cherrypy.lib.static import serve_file

class Download:

    @cherrypy.expose
    def index(self, file_):
        tgt = os.path.abspath(os.path.join('./music', file_))
        return """
<audio controls>
  <source src="%s" type="audio/ogg">
  <source src="%s" type="audio/mpeg">
  Your browser does not support the audio tag.
</audio>
           """ % (serve_file(tgt, "application/x-download", "attachment"),)

if __name__ == '__main__':
    cherrypy.quickstart(Download())