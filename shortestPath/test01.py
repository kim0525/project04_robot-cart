import heapq

 

def dijkstra(graph, start, end):

	distances = {vertex : [float('inf'), start] for vertex in graph}

	distances[start] = [0, start]

	queue = []

	heapq.heappush(queue, [distances[start][0], start])

 

	while queue:

		current_distance, current_vertex = heapq.heappop(queue)

 

		if distances[current_vertex][0] < current_distance:

			continue

		for adjacent, weight in graph[current_vertex].items():

			distance = current_distance + weight

 

			if distance < distances[adjacent][0]:

				distances[adjacent] = [distance, current_vertex]

				heapq.heappush(queue, [distance, adjacent])

 

	path = end

	path_output = end + '->'

 

	while distances[path][1] != start:

		path_output += distances[path][1] + '->'

		path = distances[path][1]

 

	path_output += start

 

	print(path_output)

 

	return distances

 

 

mygraph = {

	'1' : {'2' : 1, '4' : 1},

	'2'  : {'1' : 1, '3': 1, '5': 1},

	'3'  : {'2' : 1, '6' : 1},

	'4'  : {'1' : 1, '5' : 1, '7' : 1},

	'5'  : {'2' : 1, '4' : 1, '6' : 1, '8' : 1},

	'6'  : {'3' : 1, '5' : 1, '9' : 1},

	'7'  : {'4' : 1, '8' : 1},

	'8'  : {'5' : 1, '7' : 1, '9' : 1},

	'9'  : {'6' : 1, '8' : 1},



}

 

start_point = str(input('start point : '))

end_point = str(input('end point : '))

 

dijkstra(mygraph, end_point, start_point)