class rectangle():
   def __init__( self,l,w):
     self.length= l
     self.width=w

   def rectangle_area(self):
    return self.length*self.width

newRectangle = rectangle(12,10)
print("dimension of rectangle - length : %d width: %d " % (newRectangle.length,newRectangle.width))
print("area of rectangle:",newRectangle.rectangle_area())
