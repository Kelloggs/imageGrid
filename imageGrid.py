import Image
import ImageDraw
import ImageFont
import sys
import os

def usage():
	print "******************************************************************************"
	print "Usage:"
	print "python imageGrid NoX NoY [directoryNames]"
	print "______________________________________________________________________________"
	print "NoX: 			number of tiles in x direction"
	print "NoY: 			number of tiles in y direction"
	print "directoryNames: 	multiple directories containing images"
	print "directoryNames: 	multiple directories containing images"
	print "The number of files in the directories has to match pathDirectoryB"
	print "The directories must only contain image files (png, jpg)"
	print "******************************************************************************"

directories = []
filesLists = []
minLength = sys.maxint
xNum = 0
yNum = 0

#get parameters and check correct usage of script	
try:
	xNum = int(sys.argv[1])
	yNum = int(sys.argv[2])

	for i in range(3, len(sys.argv)):
		directories.append(sys.argv[i])
	
	for dir in directories:
		lst = os.listdir(dir)
		lst.sort()
		minLength = min(minLength, len(lst))
		filesLists.append(lst)

	#test grid
	if xNum * yNum < len(filesLists):
		raise Exception("To many files for given grid")

	#test output directory
	if os.path.exists("gridView"):
		raise Exception("Output directory 'gridView' already existing")
except Exception as e:
	print "ERROR: ", e.args
	usage()
	sys.exit(1)

#create output directory
os.mkdir("gridView")

#test final size of image
totalSize = [0, 0]
noImage = len(filesLists)
image = Image.open(directories[0] + "/" + filesLists[0][0])
totalSize = (image.size[0] * xNum, image.size[1] * yNum)
size = image.size

#initialize font and fontsize for text
font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-M.ttf", size[1] / 20)

for count in range(1, minLength):
	# initialize result image
	imResult = Image.new(mode="RGB", size=totalSize)

	for dirIndex in range(len(filesLists)):
		image = Image.open(directories[dirIndex] + "/" + filesLists[dirIndex][count])
	
		xoffset = size[0] * (dirIndex % xNum)
		yoffset = size[1] * ((dirIndex / xNum) % yNum)
		myBox = (xoffset, yoffset, xoffset + image.size[0], yoffset + image.size[1])
		imResult.paste(image, myBox)

		#draw text on images
		draw = ImageDraw.Draw(imResult)
		draw.text((xoffset, yoffset), directories[dirIndex], (60,60,60), font=font)

	#save result and output progress
	imResult.save(str("./gridView/%06d" % count) + ".png")
	i = (float(count) / float(minLength)) * 100.0
	sys.stdout.write("\r%d%% of input images processed" % i)
	sys.stdout.flush()


#that's it
print "\nFinished gridding " + str(count) + " files"

