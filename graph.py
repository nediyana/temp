#!/usr/bin/python

import csv
import os
import math
import numpy 
import matplotlib.pyplot as plt

def main():
	x_eyes = [291.4, 723.7, 391.9, 538.4, 577.9, 378.5, 707.1, 310.3, 768.6, 328.4]
	y_eyes = [426.7, 737.0, 292.1, 834.2, 330.1, 773.4, 465.9, 591.7, 549.0, 392.9]

	x_hits = [269.5, 697.5, 365.5, 540.5, 543.5, 379.5, 696.5, 263.5, 766.5, 253.5]

	y_hits = [413.0, 666.0, 285.0, 751.0, 246.0, 720.0, 332.0, 585.0, 494.0, 417.0]	

	x_post_eyes = [287.4, 722.5, 359.4, 534.0, 564.0, 431.3, 711.1, 274.3, 742.6, 325.8]
	y_post_eyes = [439.4, 744.6, 210.4, 821.2, 329.0, 750.6, 456.3, 467.5, 571.9, 354.8]


		#Plot gaze data in red, and actual click hits in blue
		# from http://forums.udacity.com/questions/10012308/how-to-draw-two-graphs-in-one-scatterplot
	fig = plt.figure()
	ax = fig.add_subplot(111)


	ax.scatter(x_eyes, y_eyes, color ='red')
	ax.scatter(x_hits, y_hits, color = 'blue')
	ax.scatter(x_post_eyes, y_post_eyes, color = "green")
		  
	plt.xlim(0, 1000)
	plt.ylim(0,1000)
	   
	plt.show()


if __name__ == '__main__':
	main()


# 