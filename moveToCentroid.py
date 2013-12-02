import pySTL
from numpy import array

#Load a model from a file.
model = pySTL.STLmodel('text.stl')

#print model properties
print "Volume  " + str(model.get_volume())
c = model.get_centroid()
print "Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2])

#Write model to a file
#model.write_text_stl('outputText.stl')

#Translate the model so that the centroid is at the origin.
#model.translate(-c)

#Is it at the origin?
#c = model.get_centroid()
#print "Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2])


#Rotate the model 
#This is an identity rotation...does nothing.
R1 = pySTL.rotationAboutX(3.14159/2)
R2 = pySTL.rotationAboutY(3.14159/4)
R = R1.dot(R2)
model.rotate(R)

c = model.get_centroid()
print "Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2])

model.write_text_stl('textTranslated.stl')
