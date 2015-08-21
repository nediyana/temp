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


def q(input_filename, distances, items, counter, amplitudes, counterAmps, x_eyes, y_eyes, x_hits, y_hits):

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

	csv_reader = csv.reader(open(input_filename), delimiter = ',')

	for row in csv_reader:
		if row != []:
			if row[1] == "Condition":
				size = row[4]
				#print size
				amplitude = row[3]
				#print amplitude
				shape = row[2] + "-" + row[3] + "-" + row[4]
				if (shape not in conditionsHit):
					conditionsHit[shape] = 0
				elif shape not in conditionsHit:
					conditionsHit[shape] = 0

			elif row[1] == "TobiiEyePosition":
				if "circle" in shape and "separated" not in shape:
					x_eye = float(row[2])
					y_eye = float(row[3])


			elif row[1] == "ClickHit":
				if "circle" in shape and "separated" not in shape:
					x_hit = float(row[2])
					y_hit = float(row[3])

				
					if (size == "24") and (amplitude == "512"):	
						x_hits.append(x_hit)
						y_hits.append(y_hit)

						x_eyes.append(x_eye)
						y_eyes.append(y_eye)

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
    for filename in os.listdir('fitts_law_final_data/'):
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
        q("fitts_law_final_data/" + filename, overall, items, counter, amplitudes, counterAmps, x_eyes, y_eyes, x_hits, y_hits)

        overall = numpy.asarray(overall)
        overall = [k for k in overall if not (k == -1)]
        finallist = finallist + overall



        ##Plot gaze data in red, and actual click hits in blue
        ## from http://forums.udacity.com/questions/10012308/how-to-draw-two-graphs-in-one-scatterplot
       #  fig = plt.figure()
       #  ax = fig.add_subplot(111)
       #  print "len of x eyes"
       #  print len(x_eyes)
       #  print "len of x hits"
       #  print len(x_hits)
       #  print "overall"
       #  print overall
       #  print "max overall"
       #  print max(overall)

       #  ax.scatter(x_eyes, y_eyes, color ='red')
       #  ax.scatter(x_hits, y_hits, color = 'blue')
       
       # # # ax.scatter(x_post_eyes, y_post_eyes, color = 'green')
       
       #  plt.xlim(0, 1000)
       #  plt.ylim(0,1000)
       
       # 	print filename
       #  plt.show()

        print overall

    print "len of overall"
    print len(finallist)
    print "max overall"
    print max(finallist)


    # print overall
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = finallist
    numbins =  [0, 50, 100, 200, 300, 400, 500, 600, 800, 1000]
    ax.hist(x, numbins, color= 'green', alpha = 0.8)
    plt.show()

    print finallist
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

    print len(less100)
    print len(less200)
    print len(less300)
    print len(less400)
    print len(less500)
    print len(less1000)

    print float(float(len(less100))/float(len(finallist)))
    print float(float(len(less200))/float(len(finallist)))
    print float(float(len(less300))/float(len(finallist)))
    print float(float(len(less400))/float(len(finallist)))
    print float(float(len(less500))/float(len(finallist)))
    print float(float(len(less1000))/float(len(finallist)))


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


# 