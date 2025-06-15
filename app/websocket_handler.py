import tornado.websocket

connected_clients = set()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        connected_clients.add(self)
        print("Aberto")

    def on_close(self):
        connected_clients.remove(self)
        print("Fechado")
    
    def check_origin(self, origin):
        return True