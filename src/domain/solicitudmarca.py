from service.toyotaservice import Toyotaservice
from service.peugeotservice import Peugeotservice
from service.nissanservice import Nissanservice
from controller.autocontroller import CarHandler
from view.marcaview import marca

class solicitud():
    def main():
        marca
         
        toyota_service = Toyotaservice()
        peugeot_service = Peugeotservice()
        nissan_service = Nissanservice()

        car_handler = CarHandler(toyota_service)  
        toyota_service.set_next_handler(peugeot_service)
        peugeot_service.set_next_handler(nissan_service)   

        car_handler.handle_request(marca)