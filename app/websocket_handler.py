import tornado.websocket

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Aberto")

    def on_close(self):
        print("Fechado")
    
    def check_origin(self, origin):
        return True