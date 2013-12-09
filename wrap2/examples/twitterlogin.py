"""
We are running our http server which will host the twitter app.
After authentication, we get some twitter stream.
"""

import sys
from wrap2 import Twitter
import urlparse
import BaseHTTPServer
import webbrowser
from pprint import pprint
from itertools import islice


REDIRECT_URL = 'http://127.0.0.1:8080/'

network = Twitter('TOKEN',
                  'SECRET')

RUNNING = False
TW_REQUEST_TOKEN = None


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """Request Handler for Test HTTP Server"""

    def do_GET(self):
        global RUNNING
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        result = urlparse.parse_qs(
            urlparse.urlparse(self.path).query)

        oauth_verifier = result.get('oauth_verifier')

        if oauth_verifier is None:
            self.wfile.write("Authentication failed")
            sys.exit(1)

        oauth_verifier = oauth_verifier[0]

        (id, access_token, name, profile_link) = network.on_authorization_callback(REDIRECT_URL, oauth_verifier,
                                                                                   TW_REQUEST_TOKEN)

        print 'Great success!'
        print 'ID ', id
        print 'ACCESS_TOKEN', access_token
        print 'NAME ', name
        print 'PROFILE ', profile_link

        # Posting is annoying
        #post = network.post(access_token, "It works using wrap2!")
        #pprint(post)

        print
        print 'Some recent #wheniwaslittle tweets:'

        for s in islice(network.get(access_token, '#wheniwaslittle'), 2):
            pprint(s)

        RUNNING = False

if __name__ == '__main__':
    RUNNING = True
    url, (key, secret) = network.get_authorization_url(REDIRECT_URL)

    TW_REQUEST_TOKEN = (key, secret)
    webbrowser.open(url)
    httpd = BaseHTTPServer.HTTPServer(('127.0.0.1', 8080),
                                      RequestHandler)
    while RUNNING:
        httpd.handle_request()
