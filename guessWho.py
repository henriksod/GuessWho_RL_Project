#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random as rand

class GuessWho:

	playerTurn = 0
	faceUpFigures = []
	playerFigures = []

	def __init__(self, dataHandler):
		# Player 1 = 0
		# Player 2 = 1
		playerTurn = 0

		# Access player 1:
		#    faceUpFigures[0]
		# Access player 2:
		#    faceUpFigures[1]
		indices = range(0,dataHandler.numFigures)
		faceUpFigures = indices + indices

		# Access player 1:
		#    playerFigures[0]
		# Access player 2:
		#    playerFigures[1]
		playerFigures = [0,0]
		while playerFigures[0] == playerFigures[1]:
			playerFigures = [rand.randInt(0,dataHandler.numFigures-1),
							 rand.randInt(0,dataHandler.numFigures-1)]


	def playTurn(self,question):
		# Question is a tuple consisting of:
		#    (COLUMN_INDEX,COLUMN_VALUE)
		# Column values shall be mapped to corresponding integers
		# for RL algorithm to be more flexible. This mapping shall
		# be done in the DataHandler.
		data = dataHandler.getData()

		# TODO: Return true if correct, otherwise false and update game

		if playerTurn == 0:
			playerTurn = 1
		else:
			playerTurn = 0