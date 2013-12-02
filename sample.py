import pySTL
from numpy import array

#Load a model from a file.
model = pySTL.STLmodel('text.stl')

#print model properties
print "Volume  " + str(model.get_volume())
c = model.get_centroid()
print "Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2])


#Translate the model so that the centroid is at the origin.
model.translate(-c)
model.write_text_stl("torsoAtCentroid.stl")


#Rotate the model 90 degrees about the Y-axis
R2 = pySTL.rotationAboutY(-3.14159/2)

model.rotate(R2)

c = model.get_centroid()
print "Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2])

model.write_text_stl('torsoRAtCentroid.stl')

#Scale the model down by 100%
scale = 0.001
model.scale(scale)

model.write_text_stl('torsoRandSatCentroid.stl')

