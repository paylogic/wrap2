"""
We are running our http server which will host the facebook app.
After authentication, we get some posts stream.
"""

from wrap2 import Facebook
import urlparse
import BaseHTTPServer
import sys
import webbrowser

REDIRECT_URL = 'http://127.0.0.1:8080/'

network = Facebook(
    'APP_ID',
    'SECRET_KEY')

RUNNING = False


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """Request Handler for Test HTTP Server"""

    def do_GET(self):
        global RUNNING
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        code = urlparse.parse_qs(
            urlparse.urlparse(self.path).query).get('code')
        code = code[0] if code else None

        if code is None:
            self.wfile.write("Authentication failed")
            sys.exit(1)

        (id, access_token, name, profile_link) = network.on_authorization_callback(REDIRECT_URL, code)

        print 'Great success!'
        print 'ID ', id
        print 'ACCESS_TOKEN', access_token
        print 'NAME ', name
        print 'PROFILE ', profile_link

        #test posting to wall is not common need, uncomment if you really need it
        #post = network.post(access_token, "It works using wrap2!")
        #print repr(post)

        post = network.get(
            dict(ids=[427253624008306, 508970319133530, 234136563383608, 764427356]),
            access_token=access_token,
            count=20
        )

        print 'Get stream results:'
        print repr(post)

        RUNNING = False

if __name__ == '__main__':
    RUNNING = True
    url = network.get_authorization_url(
        REDIRECT_URL,
        scope=['publish_actions', 'publish_stream', 'read_stream'])[0]

    webbrowser.open(url)
    httpd = BaseHTTPServer.HTTPServer(('127.0.0.1', 8080),
                                      RequestHandler)
    while RUNNING:
        httpd.handle_request()
