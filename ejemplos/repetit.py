#!/bin/python -tt
 
import glob 
import os
 
#vamos a un lugar donde no rompamos nada
os.chdir("/tmp")
 
 
#crear 10 archivos con el nombre 1.txt, 2.txt... 
for element in range(10):
  bashCommand="touch "+str(element)+".txt"
  os.system(bashCommand)
 
 
for myFile in: glob.glob("/tmp/*"): 
  print "archivo: "+str(myFile)
