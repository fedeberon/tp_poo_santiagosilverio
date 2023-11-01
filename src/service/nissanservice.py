from controller.autocontroller import CarHandler

class Nissanservice(CarHandler):
    def handle_request(self, car):
        if car.lower() == "nissan":
            tipo = (input("que tipo de vehiculo (auto/camioneta) : ")) 
            if tipo == "auto":
                print ("Redircionandolo al servicio de nissan encargado de la venta de autos...")
            elif tipo == "camioneta":
                print ("Redircionandolo al servicio de nissan encargado de la venta de camionetas...")      
        elif self.next_handler:
            self.next_handler.handle_request(car)
        else:
            print("Solicitud no manejada.")