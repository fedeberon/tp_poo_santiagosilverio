from service.compraservice import Compra
from service.agregarservice import Agrega
from controller.modocontroller import AppHandler
from view.modoview import modo

class mododeuso():
    def main():
        modo

        agregar = Agrega()
        compra = Compra()


        app_handler = AppHandler(agregar)  
        agregar.set_next_handler(compra)
 

        app_handler.handle_request()