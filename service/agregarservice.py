from controller.modocontroller import AppHandler
from domain.createauto import createauto


class Agrega(AppHandler):
    def handle_request(self, modo):
        if modo == "agregar":
                marca = createauto.main()
                print(marca)