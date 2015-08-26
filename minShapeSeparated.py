#!/usr/bin/python

# * * * * * * * * * * * * * * * * * * * *
# eye.py, part of Fitts's Law Assignment
# by Nediyana Daskalova
# modified April 17, 2015
# * * * * * * * * * * * * * * * * * * * *


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Here we go through each csv, and save the coordinates of where people were clicking, 
# and where they were lookin right before they hit the target.
# I look for the average distance between the eye coordinates and the hit coordinates,
# depending on size and amplitude.
# I also create a scatter plot of the coordinates of the hits, and the eye coodinates. 
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

import csv
import os
import math
import numpy 
import matplotlib.pyplot as plt

def q(input_filename, distances, items, counter, amplitudes, counterAmps, x_eyes, y_eyes, x_hits, y_hits, figure, width, amp):

	conditions = {}
	conditionsHit = {}
	timestamps = {}
	x_hit = 0
	x_eye = 0
	x_post_eye = 0
	y_eye = 0
	y_hit = 0
	y_post_eye = 0
	distance_x = 0
	distance_y = 0
	distance = 0
	distanceFromCenter = 0
	sequence = [0,5,1,6,2,7,3,8,4,0]
	checker = 0

	if amp == "512":
		circlesX = [756.0, 696.1073774384583, 544.4539334827342, 372.00000000000006, 259.43868907880744, 259.43868907880744, 371.9999999999999, 544.4539334827341, 696.1073774384583]	
		circlesY = [500.0, 664.553628079754, 752.1107847711253, 721.7025033688163, 587.5571566913712, 412.4428433086288, 278.2974966311838, 247.88921522887472, 335.44637192024584]
	elif amp == "384":
		circlesX = [692.0, 647.0805330788438, 533.3404501120507, 404.00000000000006, 319.5790168091056, 319.5790168091056, 403.9999999999999, 533.3404501120506, 647.0805330788437, 692.0]
		circlesY = [500.0, 623.4152210598155, 689.0830885783439, 666.2768775266122, 565.6678675185284, 434.3321324814716, 333.72312247338783, 310.91691142165604, 376.5847789401844, 499.99999999999994]
					
	elif amp == "256":
		circlesX = [628.0, 598.0536887192292, 522.226966741367, 436.0, 379.7193445394037, 379.7193445394037, 435.99999999999994, 522.226966741367, 598.0536887192292, 628.0]
		circlesY = [500.0, 582.2768140398771, 626.0553923855626, 610.8512516844082, 543.7785783456857, 456.22142165431444, 389.1487483155919, 373.94460761443736, 417.7231859601229, 499.99999999999994]
					

	csv_reader = csv.reader(open(input_filename), delimiter = ',')


	for row in csv_reader:
		if row != []:
			if row[1] == "Condition":
				shape_id = 0
				size = row[4]
				amplitude = row[3]
				shape = row[2] + "-" + row[3] + "-" + row[4]
				if figure in row[2]:
					checker = checker + 1
				else: 
					checker = 0

				# if (shape not in conditionsHit):
				# 	conditionsHit[shape] = 0
				# elif shape not in conditionsHit:
				# 	conditionsHit[shape] = 0

			elif row[1] == "TobiiEyePosition":
				if figure in shape and "separated" in shape:
					x_eye = float(row[2])
					y_eye = float(row[3])



			elif row[1] == "ClickHit":
				# print shape_id
				if figure in shape and "separated" in shape:

					x_hit = float(row[2])
					y_hit = float(row[3])



					if (size == width) and (amplitude == amp):	
						x_hits.append(x_hit)
						y_hits.append(y_hit)

						x_eyes.append(x_eye)
						y_eyes.append(y_eye)
						# print shape_id
						if shape_id > 8:
							shape_id = 0
						# print circlesX[sequence[shape_id]]
						#OFFSET with + 1 when this was not the first condition, which means that it starts from the second circle in the sequence, not the first. 
						#there is not offset if this is the first time the circle starts, so we start with [shape_id] instead of [shape_id+1]

						if checker == 2:
							distanceFromCenter = math.sqrt(pow((circlesX[sequence[shape_id]] - x_hit), 2) + pow((circlesY[sequence[shape_id]] - y_hit), 2) )
						else:
							distanceFromCenter = math.sqrt(pow((circlesX[sequence[shape_id+1]] - x_hit), 2) + pow((circlesY[sequence[shape_id+1]] - y_hit), 2) )
						# if distanceFromCenter > (width/2):
						# print input_filename
						# print x_hit, y_hit
						# print circlesX[shape_id], circlesY[shape_id]
						# print distanceFromCenter
						
						shape_id = shape_id + 1

						# print input_filename
						# print "x hit, y hit, x eye, y eye"
						# print x_hit
						# print y_hit
						# print x_eye
						# print y_eye

						# fig1 = plt.figure()
						# ax1 = fig1.add_subplot(111)
						# ax1.scatter(x_eyes, y_eyes, color ='red')
						# ax1.scatter(x_hits, y_hits, color = 'blue')
						# plt.xlim(0, 1000)
						# plt.ylim(0,1000)
						distance = math.sqrt(pow((x_eye - x_hit), 2) + pow((y_eye - y_hit), 2) )
						distances.append(distance)

						# print "distance is"
						# print distance

						# plt.show()

						#a = (x_eye, y_eye)
						#b = (x_hit, y_hit)

						# distance_x = x_hit - x_eye
						# distance_y = y_hit - y_eye
						# distance = math.sqrt((distance_x * distance_x) + (distance_y * distance_y))
						

						# print "distance is"
						# print distance
						# if distance > 1000:
						# 	print input_filename
						# distances.append(dst)


					else:
						distance = -1

				#x_post_eyes.append(x_post_eye)
				#y_post_eyes.append(y_post_eye)
				
				#This part is irrelevant for just distance: FROM HERE
				# if size in items:
				# 	items[size] = items[size] + distance
				# 	counter[size] = counter[size] + 1
				# else:
				# 	items[size] = distance
				# 	counter[size] = 1

				# if amplitude in amplitudes:
				# 	amplitudes[amplitude] = amplitudes[amplitude] + distance
				# 	counterAmps[amplitude] = counterAmps[amplitude] + 1

				# else:
				# 	amplitudes[amplitude] = distance
				# 	counterAmps[amplitude] = 1
				# UNTIL HERE

				# distances.append(distance)



	return (distances)

def main():

	finallist = []
	all_x_eyes = []
	all_y_eyes = []
	all_x_hits = []
	all_y_hits = []
	# for filename in os.listdir('lookingAtCenter/'):
	# for filename in os.listdir('random/'):

	# shapes = ["circle", "louisiana", "separated_circle", "michigan", "triangle", "cross", "watermelon", "tetris", "letter_o", "sign"]
	shapes = ["separated_circle"]
	widths = ["24", "64", "94"]
	amps = ["256", "384", "512"]
	temp = []

	minPercentage = 0

	# shape-amp-width = np.zeros((10,3,3)) # Make a 10 by 3 by 3 array

	for amp in amps:
		for width in widths: 
			for figure in shapes:
				finallist =[]
				print "F I G U R E is"

				print figure
				print "W I D T H is"
				print width

				print "A M P L I T U D E is"
				print amp
				for filename in os.listdir('good/'):

					checker = 0
					# print filename
					skip = False
					overall = []
					x_eyes = []
					y_eyes = []
					x_hits = []
					y_hits = []
					distances = []
					x_post_eyes = []
					y_post_eyes = []

					items = {}
					counter = {}
					amplitudes = {}
					counterAmps = {}
					less100 = []
					less200 = []
					less300 = []
					less400 = []
					less500 = []
					less1000=[]
					# print filename
					q("good/" + filename, overall, items, counter, amplitudes, counterAmps, x_eyes, y_eyes, x_hits, y_hits, figure, width, amp)

					# q("random/" + filename, overall, items, counter, amplitudes, counterAmps, x_eyes, y_eyes, x_hits, y_hits)

					# q("lookingAtCenter/" + filename, overall, items, counter, amplitudes, counterAmps, x_eyes, y_eyes, x_hits, y_hits)

					overall = numpy.asarray(overall)
					overall = [k for k in overall if not (k == -1)]
					finallist = finallist + overall

					# temp = temp + overall

					# all_x_eyes = all_x_eyes + x_eyes
					# all_y_eyes = all_y_eyes + y_eyes

					# all_x_eyes.append(x_eyes)
					# all_y_eyes.append(y_eyes)



					##Plot gaze data in red, and actual click hits in blue
					# ## from http://forums.udacity.com/questions/10012308/how-to-draw-two-graphs-in-one-scatterplot
					
					# fig = plt.figure()
					# ax = fig.add_subplot(111)
				   

					if amp == "512":
						circlesX = [756.0, 696.1073774384583, 544.4539334827342, 372.00000000000006, 259.43868907880744, 259.43868907880744, 371.9999999999999, 544.4539334827341, 696.1073774384583]
						circlesY = [500.0, 664.553628079754, 752.1107847711253, 721.7025033688163, 587.5571566913712, 412.4428433086288, 278.2974966311838, 247.88921522887472, 335.44637192024584]
					elif amp == "384":
						circlesX = [692.0, 647.0805330788438, 533.3404501120507, 404.00000000000006, 319.5790168091056, 319.5790168091056, 403.9999999999999, 533.3404501120506, 647.0805330788437, 692.0]
						circlesY = [500.0, 623.4152210598155, 689.0830885783439, 666.2768775266122, 565.6678675185284, 434.3321324814716, 333.72312247338783, 310.91691142165604, 376.5847789401844, 499.99999999999994]
					
					elif amp == "256":
						circlesX = [628.0, 598.0536887192292, 522.226966741367, 436.0, 379.7193445394037, 379.7193445394037, 435.99999999999994, 522.226966741367, 598.0536887192292, 628.0]
						circlesY = [500.0, 582.2768140398771, 626.0553923855626, 610.8512516844082, 543.7785783456857, 456.22142165431444, 389.1487483155919, 373.94460761443736, 417.7231859601229, 499.99999999999994]
					
				
					# ax.scatter(x_eyes, y_eyes, color ='red', s=25)
					# ax.scatter(x_hits, y_hits, color = 'blue', s=25)
					#s is the radius i want them to be to the power of two; but i am not sure if 512-24 means that the diameter of those circles was 24 or if it was the radius. for now it is set as the radius, so 24 * 24 = 576
					# ax.scatter(circlesX, circlesY, color = 'grey', s=pow((int(width))/2,2), alpha=0.2)
				   
					# plt.xlim(0,1000)
					# plt.ylim(0,1000)
				   
				   	# print filename
					# plt.show()


					all_x_eyes.append(x_eyes)
					all_y_eyes.append(y_eyes)
					all_x_hits.append(x_hits)
					all_y_hits.append(y_hits)

					# print "x hits"
					# print all_x_hits
					# print "y hits"
					# print all_y_hits
					# print "x eyes"
					# print all_x_eyes
					# print "y eyes"
					# print all_y_eyes

				# print "len of overall"
				# print len(finallist)
				# print "max overall"
				# print max(finallist)


				# fig = plt.figure()
				# ax = fig.add_subplot(111)
				# x = finallist
				# numbins =  [0, 50, 100, 200, 300, 400, 500, 600, 800, 1000]
				# ax.hist(x, numbins, color= 'green', alpha = 0.8)
				# plt.show()

				for y in finallist:
					if y < 100:
						less100.append(y)
					elif y < 200:
						less200.append(y)
					elif y < 300:
						less300.append(y)
					elif y < 400:
						less400.append(y)
					elif y < 500:
						less500.append(y)
					elif y < 1000:
				 		less1000.append(y)

				# print len(less100)
				# print len(less200)
				# print len(less300)
				# print len(less400)
				# print len(less500)
				# print len(less1000)

				print float(float(len(less100))/float(len(finallist)))
				if float(float(len(less100))/float(len(finallist))) > minPercentage:
					minPercentage = float(float(len(less100))/float(len(finallist)))
					minFilename = filename
					minAmp = amp
					minWidth = width
					minShape = figure
					# print filename
				# print float(float(len(less200))/float(len(finallist)))
				# print float(float(len(less300))/float(len(finallist)))
				# print float(float(len(less400))/float(len(finallist)))
				# print float(float(len(less500))/float(len(finallist)))
				# print float(float(len(less1000))/float(len(finallist)))




	print " MIN AMPS"
	print minAmp
	print "MIN WIDTH"
	print minWidth
	print "MIN SHAPE"
	print minShape
	print "percentage less than 100px"
	print minPercentage



	# print "DOOOOONE"

	# print "PRE HIT"
	# print "x eyes"
	# print x_eyes
	# print "y eyes"
	# print y_eyes

	# print all_x_eyes
	# print all_y_eyes

	# print all_y_eyes[44]
'''
		x_eyes = numpy.asarray(x_eyes)
		y_eyes = numpy.asarray(y_eyes)

		averageDistances = numpy.mean(overall)
		stdDistances = numpy.std(overall)

		print "mean"
		print averageDistances
		print "standard deviation"
		print stdDistances

		print "size"
		for k, v in items.iteritems():
			items[k]  = float(v)/float(counter[k])

		for k, v in items.iteritems():
			print str(k) + "," + str(v)

		print "amplitudes"
		for k, v in amplitudes.iteritems():
			amplitudes[k]  = float(v)/float(counterAmps[k])

		for k, v in amplitudes.iteritems():
			print str(k) + "," + str(v)

		print filename
'''
if __name__ == '__main__':
	main()


