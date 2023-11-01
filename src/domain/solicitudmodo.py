from service.compraservice import Compraservice
from service.agregarservice import Agregarservice
from controller.modocontroller import AppHandler
from view.modoview import modo

class mododeuso():
    def main():
        modo

        Agregar = Agregarservice()
        Compra = Compraservice()


        app_handler = AppHandler(Agregar)  
        Agregar.set_next_handler(Compra)
 

        app_handler.handle_request(modo)