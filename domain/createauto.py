from domain.autobuilder import AutoBuilder

class createauto():
        def main():
                Auto = AutoBuilder().with_marca(input("¿De que marca es el auto? : ")).with_color(input("¿De que color es el auto? : ")).with_puertas(input("¿Cuantas puertas tiene el auto? : ")).build()
                print(Auto)