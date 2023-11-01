from domain.autobuilder import AutoBuilder

class Autoservice():

    def create_auto():
        AutoBuilder \
        .with_marca(marcas) \
        .with_color(color) \
        .with_puertas(puertas) \
        .build()