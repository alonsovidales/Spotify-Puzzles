#!/usr/bin/env python

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-08-02"

from itertools import *

class CheckGraph:
    """ Check if a graph is complethly covered by a set of vertexs.
    The input file should to containt the bipartitie graph for the problem,
    concatenated by the solution lines"""
    __graph = {}
    __finalVertexs = []
    
    def checkGraph(self):
        for vertex in self.__finalVertexs:
            for destVert in self.__graph[vertex]:
                self.__graph[destVert].remove(vertex)

            del self.__graph[vertex]

        # Show al the edges not covered
        for vertex, edges in self.__graph.items():
            if len(edges) > 0:
                print "Edge: %s -> [%s]" % (vertex, ', '.join(map(str, edges)))

    def __init__(self, inLines):
        for lineNum in range(1, int(inLines[0]) + 1):
            ids = map(int, inLines[lineNum].split(' '))
            try:
                self.__graph[ids[0]].append(ids[1])
            except:
                self.__graph[ids[0]] = [ids[1]]
                
            try:
                self.__graph[ids[1]].append(ids[0])
            except:
                self.__graph[ids[1]] = [ids[0]]

        for lineNum in range(int(inLines[0]) + 2, int(inLines[0]) + int(inLines[int(inLines[0]) + 1]) + 2):
            self.__finalVertexs.append(int(inLines[lineNum]))
                

fileLines = []
while True:
    try:
        fileLines.append(raw_input())
    except (EOFError):
        break #end of file reached

# Use the CheckGraph class to do the calculations
bilateralProjects = CheckGraph(fileLines)
bilateralProjects.checkGraph()
