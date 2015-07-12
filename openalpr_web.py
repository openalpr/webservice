from openalpr import Alpr

import json
import tornado.ioloop
import tornado.web

alpr = Alpr("eu", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
alpr.set_top_n(20)



class MainHandler(tornado.web.RequestHandler):
    def post(self):

        if 'image' not in self.request.files:
            self.finish('Image parameter not provided')

        fileinfo = self.request.files['image'][0]
        jpeg_bytes = fileinfo['body']

        if len(jpeg_bytes) <= 0:
            return False

        results = alpr.recognize_array(jpeg_bytes)

        self.finish(json.dumps(results))



application = tornado.web.Application([
    (r"/alpr", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()