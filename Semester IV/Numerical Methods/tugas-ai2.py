import pandas
import heapq

tabel = pandas.read_csv('jarak nyata.csv', sep='\t')
h_tabel = pandas.read_csv('Jarak lurus v2.csv', sep='\t')
# print(tabel['yogyakarta'])
# print(h_tabel)
list_kota = {
    0: 'yogyakarta', 1: 'klaten', 2: 'boyolali', 3: 'solo', 4: 'salatiga', 5: 'magelang',
    6: 'ambarawa', 7: 'semarang', 8: 'kulon progo', 9: 'purworejo', 10: 'kebumen',
    11: 'gombong', 12: 'banyumas', 13: 'purwokerto', 14: 'purbalingga', 15: 'temanggung'
}

class Kota:
    def __init__(self, nama):
        self.nama = nama
        self.neighbors = self.get_neighbors()
        self.f_score = 0
        self.index = list(list_kota.values()).index(nama)

    # Insert neighbors and its distance from current city
    def get_neighbors(self):
        neighbor = {}
        for i in range(len(tabel[self.nama])):
            if tabel[self.nama][i] != '999999' and tabel[self.nama][i] != 999999:
                neighbor[list_kota[i]] = tabel[self.nama][i]
        # neighbor[list_kota[i]] = Kota(list_kota[i])
        return neighbor

    # Insert distance
    def set_fScore(self, g_score, goal):
        h_score = float(h_tabel[self.nama][list(list_kota.keys())[list(list_kota.values()).index(goal)]])
        # print(h_score)
        # print(self.nama)
        self.f_score = float(g_score) + float(h_score)

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
    closeSet = []
    heapq.heappush(openSet, (0, start))

    cameFrom = {}

    # Isinya (Kota, jarak dari origin start)
    gScore = {}
    gScore[start] = 0

    fScore = {}
    fScore[start] = 0

    while len(openSet) > 0:

    # openSet isinya (jarak dari start, Kota)
        current = openSet[0][1]
        current = heapq.heappop(openSet)[1]
        print(current.nama)

        if current.nama == goal:
            return jalan(cameFrom, current)

        for neighbor in current.neighbors:
            kota = Kota(neighbor)
            if kota.nama not in closeSet:
                gScore[kota] = tabel[current.nama][kota.index]
                tentative_gScore = float(gScore[current]) + float(gScore[kota])
                kota.set_fScore(tentative_gScore,goal)
                heapq.heappush(openSet, (float(kota.f_score), kota))
                # try:
                # except Exception as e:
                    # print(e)

                closeSet.append(current.nama)
        # print(openSet)
        print('\n\n')
        # print(closeSet)

        # for neighbor in openSet:
            # if neighbor not in closeSet:
                # kota_neighbor = Kota(neighbor)
                # 
                # heapq.heappush(openSet, (kota_neighbor.f_score, kota_neighbor))
    return "Goal not reached"



start = Kota('yogyakarta')
goal = "semarang"

print(A_star(start, goal))