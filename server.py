import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.websocket

import json

from tornado.escape import json_decode


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        pass


class SendHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('sendBox.html')

    def post(self):
        pass


class RoomHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('room.html')

    def post(self):
        pass

class ResponseHandler(tornado.web.RequestHandler):
    def post(self):
        # data
        #
        print(json_decode(self.request.body))
        pass


application = tornado.web.Application(handlers=[(r"/", MainHandler),(r"/sendBox.html", SendHandler),(r"/room.html", RoomHandler),(r"/response", ResponseHandler)])
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
