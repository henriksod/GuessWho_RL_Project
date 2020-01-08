#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pandas as pd

class DataHandler:

	# TODO: Column values shall be mapped to corresponding integers
	# for RL algorithm to be more flexible. This mapping shall
	# be done in the DataHandler.

	numFigures = 0
	df = []

	def __init__(self, filename):
		with open(filename, 'r') as f:
			datastore = json.load(f)

		# initialize list of lists 
		data = []
		self.numFigures = datastore["meta"]["numFigures"]
		for i in range(0,self.numFigures):
			figure = datastore["figures"][i]
			data += [[figure["name"],
					  figure["gender"],
					  figure["eyeColor"],
					  figure["skinColor"],
					  figure["hairType"],
					  figure["hairColor"],
					  figure["hasBeard"],
					  figure["hasMoustache"],
					  figure["hasGlasses"],
					  figure["noseSize"],
					  figure["lipColor"],
					  figure["hasEarrings"],
					  figure["hasHat"]]]
  
		# Create the pandas DataFrame 
		self.df = pd.DataFrame(data, columns = ["name","gender","eyeColor",
				"skinColor","hairType","hairColor","hasBeard","hasMoustache",
				"hasGlasses","noseSize","lipColor","hasEarrings","hasHat"]) 
		  
		# print dataframe. 
		print "Loaded data from JSON file:"
		print self.df 

	def getData(self):
		return self.df
