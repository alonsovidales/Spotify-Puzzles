""" bestbefore.py: This code is a proof of code for Spotify, @see http://www.spotify.com/es/jobs/tech/best-before/ """

from datetime import *

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-02-27"

class Bestbefore:
	"""
	This class will be used to calculate the best match date
	"""

	__dateRawStr = ''
	__formatted = None

	def __checkPossibleDate(self, inYear, inMonth, inDay):
		"""
		Return the possible date if exists
		"""
		#print("Testing: " + str(inYear) + ' - ' + str(inMonth) + ' - ' + str(inDay))
		try:
			if (int(inYear) < 2000):
				return datetime(2000 + int(inYear), int(inMonth), int(inDay), 0, 0, 0, 0)
			else:
				return datetime(int(inYear), int(inMonth), int(inDay), 0, 0, 0, 0)
	
		except:
			return None

	def getFormattedDate(self):
		"""
		Test all the possible variations, and try to get a correct date
		from each one
		"""
		if (self.__formatted == None):
			possibleDates = []
			dateParts = self.__dateRawStr.split(u"/")

			# Check all the possible variations
			possibleDate = self.__checkPossibleDate(dateParts[0], dateParts[1], dateParts[2])
			if (possibleDate != None):
				possibleDates.append(possibleDate)

			possibleDate = self.__checkPossibleDate(dateParts[0], dateParts[2], dateParts[1])
			if (possibleDate != None):
				possibleDates.append(possibleDate)

			possibleDate = self.__checkPossibleDate(dateParts[1], dateParts[2], dateParts[0])
			if (possibleDate != None):
				possibleDates.append(possibleDate)

			possibleDate = self.__checkPossibleDate(dateParts[1], dateParts[0], dateParts[2])
			if (possibleDate != None):
				possibleDates.append(possibleDate)

			possibleDate = self.__checkPossibleDate(dateParts[2], dateParts[0], dateParts[1])
			if (possibleDate != None):
				possibleDates.append(possibleDate)

			possibleDate = self.__checkPossibleDate(dateParts[2], dateParts[1], dateParts[0])
			if (possibleDate != None):
				possibleDates.append(possibleDate)

			# find the most proximate date 999999 is infinite
			proxDateDiff = 99999999
			proximateDate = None
			earliestDate = datetime(2000, 01, 01, 0, 0, 0, 0)
			for dateToCheck in possibleDates:
				# Check if the date is in the interval
				diffTime = abs((earliestDate - dateToCheck).days)
				#print("Checking: " + dateToCheck.strftime("%Y-%m-%d") + ' - ' + str(diffTime))
				if (diffTime < proxDateDiff):
					proxDateDiff = diffTime
					proximateDate = dateToCheck

			if (proximateDate != None):
				return proximateDate.strftime("%Y-%m-%d")
			else:
				return self.__dateRawStr + u" is illegal"

	def __init__(self, inDate):
		""" This constructor recieve the date and store it to be used """
		self.__dateRawStr = inDate


# Get the input from the stdin, and put the solution at the stdout
bestbefore = Bestbefore(raw_input())
print(bestbefore.getFormattedDate())