from controller.modocontroller import AppHandler
from domain.solicitudmarca import solicitud

class Compra(AppHandler):
    def handle_request(self, modo):
        if modo == "comprar":
                marca = solicitud.main()
                print(marca)