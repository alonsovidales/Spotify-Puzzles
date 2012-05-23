#!/usr/bin/env python
""" lottery.py: This code is a proof of code for Spotify, @see http://www.spotify.com/es/jobs/tech/ticket-lottery/ """

from math import *

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-02-28"

class Lottery:
	"""
	This class will be used to calculate the number of possibilities that you
	have to get a brodway ticket
	"""
	__candidates = 0
	__winners = 0
	__ticketsByWinner = 0
	__peopleInGroup = 0

	def __binomialCoef(self, inN, inK):
		"""
		Faster implementation of the binomial coeficient algorithm

		@param int <inN>: The number of elemenst
		@param int <inK>: Set of elements on N

		@return float: the result of the binomial coeffient
		"""
		if 0 <= inK <= inN:
			ntok = 1
			for t in xrange(min(inK, inN - inK)):
				ntok = ntok * (inN - t) // (t + 1)
	
			return ntok

		return 0

	def __hipergeometricalDist(self, n, m, d, k):
		"""
		Hipergeometrical distribution:
		@param int <n>:  is the population size
		@param int <m>: is the number of success states in the population
		@param int <d>: is the number of draws
		@param int <k>: is the number of successes
	
		@return <float>: The probability
		"""
		return (self.__binomialCoef(m, k) * self.__binomialCoef(n - m, d - k)) / float(self.__binomialCoef(n, d))
		

	def getProbability(self):
		"""
		Return the probability for the given line

		@return <float>: The total probability
		"""
		# I'll need all this tickets or more
		minNumOfTickets = int(ceil(float(self.__peopleInGroup) / self.__ticketsByWinner))

		# Check and sum the probability for each possible number of tickets
		probToGetTicket = 0.0
		for count in range(minNumOfTickets, self.__peopleInGroup + 1):
			probToGetTicket += self.__hipergeometricalDist(
				self.__candidates,
				self.__peopleInGroup,
				self.__winners,
				count)

		return '%0.10f' % probToGetTicket

	def __init__(self, inInfo):
		""" This constructor recieve the info and store it to be used """
		parts = inInfo.split()
		self.__candidates = int(parts[0])
		self.__winners = int(parts[1])
		self.__ticketsByWinner = int(parts[2])
		self.__peopleInGroup = int(parts[3])

# Get the input from the stdin, and put the solution at the stdout
#lottery = Lottery(raw_input())
#print(lottery.getProbability())

# Used to test with multiple lines file
while True:
	try:
		lottery = Lottery(raw_input())
		print(lottery.getProbability())
	except (EOFError):
		break #end of file reached