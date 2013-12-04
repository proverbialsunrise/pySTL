#!/usr/bin/python

import pySTL
import argparse


parser = argparse.ArgumentParser(description='Process a given STL file and perform rotation, translation, and scaling on it.  Actions happen in the order given here.  Scaling, then translation, then rotation. If selected, centroid translation happens last.')

parser.add_argument('-i', '--infile', action="store", help='input STL file', required=True)

parser.add_argument('-o', '--outfile', action="store", help='output STL file including the extension.  If none is given, processing is performed in place and the input file is replaced by the edited version', default="SECRET")

parser.add_argument('-s', '--scale', action="store", help='scaling factor for output STL', type=float, default=1.0)


parser.add_argument('-t', '--translate', action="store", help='translate the STL file: provide three numeric values for x, y, and z translation  e.g. --translate 10.1 -14.2 15', nargs=3, type=float, default=[])

parser.add_argument('-r', '--rotate', action="store", help='rotate the STL file: provide 3 angles for 3-1-3 body-fixed Euler angle rotations in radians', nargs=3, type=float, default=[]) 

parser.add_argument('-c', '--centroid', action="store_true", help='move the STL file so that the origin is the centroid after performing all other operations', default=False)
parser.add_argument('-v', '--verbose', action="store_true", help='print out operations', default=False)

args = parser.parse_args()
 
if args.verbose:
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to
        # stuff everything to be printed into a single string
        for arg in args:
           print arg,
        print
else:   
    verboseprint = lambda *a: None      # do-nothing function



model = pySTL.STLmodel(args.infile)

if args.scale != 1:
    verboseprint("Scaling model by factor: ", args.scale)
    model.scale(args.scale)


translation = args.translate
if len(translation) == 3:
    verboseprint("Performing translation: deltaX = ", str(translation[0]), ", deltaY = ", str(translation[1]), ", deltaZ = ", str(translation[2]))
    model.translate(translation)

eulerAngles = args.rotate
if len(eulerAngles) == 3:
    verboseprint('Performing Rotation')
    R1 = pySTL.rotationAboutZ(eulerAngles[0])
    R2 = pySTL.rotationAboutX(eulerAngles[1])
    R3 = pySTL.rotationAboutZ(eulerAngles[2])
    #For body-fixed, pre-multiply.   
    R = R3.dot(R2.dot(R1))
    verboseprint("Rotation Matrix: \n", R)
    model.rotate(R)


if args.centroid:
    verboseprint("Moving model to centroid")
    c = model.get_centroid()
    model.translate(-c)
   

if args.outfile == "SECRET":
    outfile = args.infile
else:
    outfile = args.outfile

model.write_text_stl(outfile)
