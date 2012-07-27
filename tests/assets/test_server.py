#!/usr/bin/env python

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

serv = HTTPServer(("", 8400), SimpleHTTPRequestHandler)
print "server start on port 8400"
serv.serve_forever()
