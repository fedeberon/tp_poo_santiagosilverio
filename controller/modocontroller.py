class AppHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, car):
        if self.next_handler:
            self.next_handler.handle_request(car)
        else:
            print("Solicitud no manejada.")
            