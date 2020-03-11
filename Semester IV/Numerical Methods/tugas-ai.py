import pandas
import heapq

tabel = pandas.read_csv('jarak nyata.csv', delimiter='\t')
h_tabel = pandas.read_csv('Jarak lurus v2.csv', delimiter='\t')
# print(tabel['Yogyakarta'])
list_kota = {
    0: 'yogyakarta',
    1: 'klaten',
    2: 'boyolali',
    3: 'solo',
    4: 'salatiga',
    5: 'magelang',
    6: 'ambarawa',
    7: 'semarang',
    8: 'kulon progo',
    9: 'purworejo',
    10: 'kebumen',
    11: 'gombong',
    12: 'banyumas',
    13: 'purwokerto',
    14: 'purbalingga',
    15: 'temanggung'
}

class Kota:
    def __init__(self, nama):
        self.nama = nama
        self.neighbors = self.get_neighbors()
        self.air_distance = self.get_air_distance()
    
    # Insert neighbors and its distance from current city
    def get_neighbors(self):
        neighbor = {}
        for i in range(len(tabel[self.nama])):
            if tabel[self.nama][i] != '9999' and tabel[self.nama][i] != 9999:
                neighbor[list_kota[i]] = tabel[self.nama][i]
                # neighbor[list_kota[i]] = Kota(list_kota[i])
        return neighbor
    
    # Insert air distance
    def get_air_distance(self):
        distances = {}
        for i in range(len(h_tabel[self.nama])):
            if h_tabel[self.nama][i] != '9999999' and h_tabel[self.nama][i] != 9999999:
                distances[list_kota[i]] = h_tabel[self.nama][i]
        return distances



def jalan(cameFrom, current):
    print(cameFrom)
    total_path = []
    total_path.append(current)
    score = 0
    while current in cameFrom.Keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path 
        

def A_star(start, goal):

    # openSet start with a node contains only starting city
    openSet = []
    heapq.heappush(openSet, (start.air_distance[goal], start))

    cameFrom = {}

    gScore = {}
    gScore[start.nama] = 0

    fScore = {}
    fScore[start] = start.air_distance[goal]

    while len(openSet) > 0:

        current = openSet[0][1]
        
        if current.nama == goal:
            return jalan(cameFrom, current)
        
        # min_fScore = min([(x.air_distance[goal] + gScore[x]) for x in openSet])
        heapq.heappop(openSet)

        for neighbor in current.neighbors:
            kota_neighbor = Kota(neighbor)
            index = list(list_kota.keys())[list(list_kota.values()).index(neighbor)]
            gScore[neighbor] = tabel[current.nama][index]
            tentative_gScore = gScore[current.nama] + float(current.neighbors[neighbor])
            print([x for x in gScore.keys()])
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = Kota(current)
                gScore[neighbor] = tentative_gScore
                the_neighbor_city = Kota(current.nama)
                fScore[neighbor] = gScore[neighbor] + the_neighbor_city.air_distance[goal]
                if neighbor not in openSet:
                    element = Kota(neighbor)
                    heapq.heappush(openSet, (element[neighbor], element))

        return "Goal not reached"



start = Kota('yogyakarta')
goal = "semarang"

A_star(start, goal)

