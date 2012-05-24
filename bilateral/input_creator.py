#!/usr/bin/env python

""" input_creator.py: Create aleatory bipartitie graphs """

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-05-19"

import random

edges = 500

print(edges)
for count in range(0, edges):
	print random.randrange(0, 1000) + 1000, random.randrange(0, 1000) + 2000
	#print random.randrange(0, 3) + 1007, random.randrange(0, 3) + 2000
