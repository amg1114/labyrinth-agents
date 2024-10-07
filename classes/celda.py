class Celda:
    # Tipos de celda:
    # 'C' - Camino Libre
    # 'B' - Bloque (Obstaculo)
    # 'G' - Galleta
    # 'P' - Peggy
    # 'E' - Elmo 
    
    def __init__(self, tipo = 'C', costo = 1):
        self.costo = costo
        self.tipo = tipo
        
    def __str__(self):
        return self.tipo