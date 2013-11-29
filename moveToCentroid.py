import pySTL

#Load a model from a file.
model = STLmodel('text.stl')

#print model properties
print "Volume  " + str(model.get_volume())
c = model.get_centroid()
print "Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2])

#Write model to a file
model.write_text_stl('outputText.stl')

#Translate the model so that the centroid is at the origin.
model.translate(-c)

#Is it at the origin?
c = model.get_centroid()
print "Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2])


#Rotate the model 
#This is an identity rotation...does nothing.
R = array([1, 0, 0, 0, 1, 0, 0, 0, 1]).reshape((3,3))
model.rotate(R)

c = model.get_centroid()
print "Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2])

model.write_text_stl('textTranslated.stl')
