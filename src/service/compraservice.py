from controller.modocontroller import AppHandler
from domain.solicitudmarca import solicitud
from view.modoview import modo

class Compraservice(AppHandler):
    def handle_request(self, app):
        if app.lower() ==  "Compra":
                marca = solicitud.main()
                print(marca)
        elif self.next_handler:
            self.next_handler.handle_request(app)
        else:
            print("Solicitud no manejada.")