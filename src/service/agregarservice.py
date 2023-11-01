from controller.modocontroller import AppHandler
from domain.createauto import createauto
from view.modoview import modo

class Agregarservice(AppHandler):
    def handle_request(self, app):
        if app.lower() == "Agregar":
                marca = createauto.main()
                print(marca)
        elif self.next_handler:
            self.next_handler.handle_request(app)
        else:
            print("Solicitud no manejada.")