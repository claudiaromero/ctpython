#!/usr/bin/python -tt
############ EJEMPLO 2 ############ 
 
#SO SO SOLUTION
 
def area(x1, y1, x2, y2):
  return abs(x1-x2) * abs(y1-y2)
 
 
def testArea1():
 
# punto1
  x1=10
  y1=10
# punto2  
  x2=5
  y2=8
 
  print "el area es: "+str(area(x1,x2,y1,y2))
 
 
#llamado a 
testArea1()
 
 
#! BETER SOLUTION
 
def area(dot1, dot2):
  return abs(dot1[0]-dot2[0]) * abs(dot1[1]-dot2[1])
 
def testAreaDot():
  dot1=(10,10)
  dot2=( 5, 8)
  print "el area es: "+str(area(dot1,dot2))
  
testAreaDot()
 
 
 
 
 
 
 
#CLASS STYLE SOLUTION
 
class point:
  '''
  define euclidean point
  '''    
  def __init__(self,x,y):
        self.x = x
        self.y = y
 
def areaClass(dot1, dot2):
  return abs(dot1.x-dot2.x) * abs(dot1.y-dot2.y)
 
 
 
 
def testArea():
  dot1=point(10,10)
  dot2=point( 5, 8)
 
  print "el area usando clases es: "+str(areaClass(dot1,dot2))
 
 
#call test
testArea()
 
