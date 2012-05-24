""" bilateral.py: This code is a proof of code for Spotify, @see http://www.spotify.com/es/jobs/tech/bilateral-projects/  """

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-05-20"

# include the Hopcroft-Karp bipartite matching algorithm
import bipartite_match

class Bilateral:
	__debug = False
	__employeesGraph = {}
	__edgesGraph = set()

	def __getReachableVertices(self, inOriginVertex, inEdgesMap):
		""" This method returns all the vertex reachables from the given set of vertices using
		the given edges map
		@see http://en.wikipedia.org/wiki/File:Koenigs-theorem-proof.svg
		@param inOriginVertex set: A set with the current vertices
		@param inEdgesMap dictionary: The map with all the edges, see self.__convertEdgesToGraph
		@return set: A set with all the reachable vertices
		"""
		finalVertex = set()
		for vertex in inOriginVertex:
			for targetVertex in inEdgesMap.get(vertex, set()):
				finalVertex.add(targetVertex)

		return finalVertex

	def __convertEdgesToGraph(self, inEdges):
		""" This method recieve a set of edges, and returns a dictionary of sets that represents
		the edges.
		@param inEdges set: A set of sets with the vertices each set that defines an edge
		@return dictionary: A dictionary of sets where the key are the vertices at the left and
		the value of each vertice a set with the reachable vertices that define the edges """
		graph = {}
		for edge in inEdges:
			try:
				graph[edge[0]].add(edge[1])
			except:
				graph[edge[0]] = set([edge[1]])
			try:
				graph[edge[1]].add(edge[0])
			except:
				graph[edge[1]] = set([edge[0]])

		return graph

	def __minVertexCover(self, inMaxCardinality):
		""" Calculate the min number of vertext necessary to cover all the graph after know the max cardinality
		using the Konig algorithm
		@see http://en.wikipedia.org/wiki/K%C3%B6nig's_theorem_(graph_theory)#Algorithm

		@param inMaxCardinality set: Set of tuples of two integers with the two vertexts that defines a edge
		@return set: A set with the necessary integers that represents the vertexs who cover all the graph
		"""
		unusedEdges = self.__edgesGraph - inMaxCardinality

		# Create the unused and max cardinality graphs using a dict to improve
		# the edges search using vertices. This is the T in the Algorithm definition
		unusedEdgesGraph = self.__convertEdgesToGraph(unusedEdges)
		maxCardinalityGraph = self.__convertEdgesToGraph(inMaxCardinality)

		if self.__debug:
			print "Max cardinality:", maxCardinalityGraph
			print "Unnecessary edges:", unusedEdgesGraph

		leftVertMatch, rightVertMatch = map(set, zip(*inMaxCardinality))
		leftVert, rightVert = map(set, zip(*self.__edgesGraph))

		unusedLeftVert = leftVert - leftVertMatch
		unusedLeftVerttLen = len(unusedLeftVert)
		if self.__debug:
			print "Unused left vertex:", unusedLeftVert

		leftPointerVertexs = unusedLeftVert

		lastUnusedVertLen = -1
		# Do it until all the neigbours are visited
		while lastUnusedVertLen != len(unusedLeftVert):
			# Advance one steep into the graph getting all the reachable vertices from the last reached vertices
			rightPointerVertexs = self.__getReachableVertices(leftPointerVertexs, unusedEdgesGraph)
			leftPointerVertexs = self.__getReachableVertices(rightPointerVertexs, maxCardinalityGraph)

			# Get the last len to know if all the possibilities are studied when all the neighbours are visited
			lastUnusedVertLen = len(unusedLeftVert)
			unusedLeftVert = set.union(unusedLeftVert, leftPointerVertexs, rightPointerVertexs)

		return (leftVert - unusedLeftVert) | (rightVert & unusedLeftVert)

	def getEssentialEmployees(self):
		# Use the "Hopcroft-Karp bipartite matching algorithm" to get the max cardinality
		maxMatching, pred, unlayered = bipartite_match.bipartiteMatch(self.__employeesGraph)

		# With the max cardinality, we can calculate the min vertex cover using the Konig
		# theorem in polynomial time
		return self.__minVertexCover(set(maxMatching.items()))

	def __init__(self, inLines):
		""" Get all the lines of the file as an array and parse all of them
		@type inLines: array
		@param inLines: All the lines contained in the file as an array of strings
		"""
		for lineNum in range(1, int(inLines[0]) + 1):
			ids = map(int, inLines[lineNum].split())

			self.__edgesGraph.add((ids[0], ids[1]))
			# Create the employees graph using a dict, the key will be the employee at the left,
			# and the values a set with all the employees connected to the employees at the right
			try:
				self.__employeesGraph[ids[0]].add(ids[1])
			except:
				self.__employeesGraph[ids[0]] = set([ids[1]])

			try:
				self.__employeesGraph[ids[1]].add(ids[0])
			except:
				self.__employeesGraph[ids[1]] = set([ids[0]])

		if self.__debug:
			print "Employees graph:", self.__employeesGraph
			print "Edges graph set:", self.__edgesGraph



if __name__ == "__main__":
	# I'll use raw_input to get the lines because I can't import fileinput on the test server
	fileLines = []
	while True:
		try:
			fileLines.append(raw_input())
		except (EOFError):
			break #end of file reached

	# Use the Bilateral class to do the calculations
	bilateralProjects = Bilateral(fileLines)
	employees = bilateralProjects.getEssentialEmployees()

	# Send the output to the stdout
	print(len(employees))
	for employee in employees:
		print(employee)
