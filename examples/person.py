"""
Este modulo de ejemplo muestra varios tipos de documentaicon disponibles
con pydoc. Para generar la documentacion en html usar:

    pydoc -w foo

"""

class Persona(object):
    """
    Esta clase encapsula las propiedades de un bailarin, que 
    aveces sabe bailar tango y aveces no, por defecto ninguna 
    persona sabe bailar tango.
    """

    nombre=""
    sabeBailarTango=False
    
    def __init__(self, nombre, sabeBailarTango):
        self.nombre = nombre
        self.sabeBailarTango=sabeBailarTango
        
    def bailarTango(self):
      
      if self.sabeBailarTango :
        porPantalla ("soy "+self.nombre+" y estoy bailando a lo loco, unas milogas pebeta!!!!")
      else:
        porPantalla ("soy "+self.nombre+" y tengo que ir a la Viruta a tomar unas clases")
    

def porPantalla(mensaje):
    """
    Imprime mesaje por pantalla
    """
    print mensaje

if __name__ == '__main__':
    johnDoe   = Persona('John Doe', True)
    pepeMonge = Persona('Pepe Monge', False)
    
    johnDoe.bailarTango()
    pepeMonge.bailarTango()
    
    
