#!/usr/bin/python -tt
"""
Este modulo de ejemplo muestra varios tipos de documentaicon disponibles
con pydoc. Para generar la documentacion en html usar:

    pydoc -w foo

"""

class Person:
    """
    Esta clase encapsula las propiedades de un bailarin, que 
    aveces sabe bailar tango y aveces no, por defecto ninguna 
    persona sabe bailar tango.
    """

    def __init__(self, name, danceTango):
        self.name = name
        self.danceTango=danceTango
        
    def dancingTango(self):
      
      if self.danceTango :
        toScreen ("soy "+self.name+" y estoy bailando a lo loco, unas milogas pebeta!!!!")
      else:
        toScreen ("soy "+self.name+" y tengo que ir a la Viruta a tomar unas clases")
    

def toScreen(mensaje):
    """
    Imprime mesaje por pantalla
    """
    print mensaje

if __name__ == '__main__':
    johnDoe   = Person('John Doe', True)
    pepeMonge = Person('Pepe Monge', False)
    
    johnDoe.dancingTango()
    pepeMonge.dancingTango()
#    
#    
