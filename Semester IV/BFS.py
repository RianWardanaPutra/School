inf = 99999
white = "white"
black = "black"
gray = "gray"
nil = None


BFS(G,s)
for all x in V-{s}
	color[x] = white
	d[x] = inf
	p[x] = nil
color[x] = gray
d[s] = 0
p[s] = nil
Q = new empty Queue
Enqueue(Q, s)
while Q is not empty
	x = Dequeue(Q)
	for y = 1 to |V|
		if A[x][y] == 1 and color[y] == white
			color[y] = gray
			d[y] = d[x] + 1
			p[y] = x
			Enqueue(Q, y)
	color[x] = black
