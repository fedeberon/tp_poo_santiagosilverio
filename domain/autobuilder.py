from domain.auto import AutoModel

class AutoBuilder:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AutoBuilder, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.marca = ""
        self.color = ""
        self.puertas = 0

    def with_marca(self, marca):
        self.marca = marca
        return self

    def with_color(self, color):
        self.color = color
        return self

    def with_puertas(self, puertas):
        self.puertas = puertas
        return self

    def build(self):
        return AutoModel(self.marca, self.color, self.puertas)
