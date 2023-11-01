from controller.autocontroller import CarHandler

class Toyotaservice(CarHandler):
    def handle_request(self, car):
        if car.lower() == "toyota":
            tipo = (input("que tipo de vehiculo (auto/camioneta) : ")) 
            if tipo == "auto":
                print ("Redircionandolo al servicio de toyota encargado de la venta de autos...")
            elif tipo == "camioneta":
                print ("Redircionandolo al servicio de toyota encargado de la venta de camionetas...")      
        elif self.next_handler:
            self.next_handler.handle_request(car)
        else:
            print("Solicitud no manejada.")
