import pandas
import heapq

tabel = pandas.read_csv('jarak nyata.csv', sep=';')
h_tabel = pandas.read_csv('jarak lurus v2.csv',  sep=';')

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
        self.g_score = 999999
        self.index = list(list_kota.values()).index(nama)
        self.before = None
    
    # Insert neighbors and its distance from current city
    def get_neighbors(self):
        neighbor = {}
        for i in range(len(tabel[self.nama])):
            if tabel[self.nama][i] != '999999' and tabel[self.nama][i] != 999999:
                neighbor[list_kota[i]] = tabel[self.nama][i]
        return neighbor

    # Insert distance
    def set_fScore(self, g_score, city_before, goal):
        if g_score < self.g_score:
            self.g_score = g_score 
        if self.nama == goal:
            h_score = 0
        else:
            h_score = float(h_tabel[self.nama][list(list_kota.keys())[list(list_kota.values()).index(goal)]])
        self.f_score = g_score + h_score
        self.before = city_before

def jalan(start, tujuan):
    path = []
    current = tujuan
    total_path = 0
    while current.nama != current.before:
        total_path += current.g_score
        path.append([current.nama, current.g_score])
        current = current.before
    path.append([current.nama, 0])
    path.reverse()
    print(*path, sep="\n")
    print("Jarak dari",start.nama, "ke",tujuan.nama, "=",total_path,"km")
    return True
        
def A_star(start, goal):

    start.set_fScore(99999,start.nama,goal)

    # openSet start with a node contains only starting city
    openSet = []
    closeSet = []
    heapq.heappush(openSet, (0, start))

    # Isinya (Kota, jarak dari origin start)
    gScore = {}
    gScore[start] = 0

    fScore = {}
    fScore[start] = 0

    while len(openSet) > 0:

    # openSet isinya (jarak dari start, Kota)
        current = openSet[0][1]
        current = heapq.heappop(openSet)[1]

        for neighbor in current.neighbors:
            kota = Kota(neighbor)
            if kota.nama not in closeSet:
                gScore[kota] = tabel[current.nama][kota.index]
                # tentative_gScore = float(gScore[current]) + float(gScore[kota])
                kota.set_fScore(float(gScore[kota]), current, goal)
                heapq.heappush(openSet, (float(kota.f_score), kota))
                # print(current.nama)
                # print(neighbor)
                # print(tentative_gScore)
                # print(kota.f_score)
                # print()
            if kota.nama == goal:
                return jalan(start,kota)

        closeSet.append(current.nama)
    return "Goal not reached"

print("Daftar kota:")

a = list(list_kota.values())

for i, j in zip(a[::2],a[1::2]):
    if len(i) < 8: i += '  '
    print(i, '|', j, sep='\t')

awal = input("Kota asal (No Caps) = ")
goal = input("Kota tujuan = ")
start = Kota(awal)

A_star(start, goal)