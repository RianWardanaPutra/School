import pandas

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
            if tabel[self.nama][i] != '9999' or tabel[self.nama][i] != 9999:
                neighbor[list_kota[i]] = tabel[self.nama][i]
        return neighbor
    
    # Insert air distance
    def get_air_distance(self):
        distances = {}
        for i in range(len(h_tabel[self.nama])):
            if h_tabel[self.nama][i] != '999999' or h_tabel[self.nama][i] != 999999:
                distances[list_kota[i]] = h_tabel[self.nama][i]
        return distances

    



def jalan(cameFrom, current):
    total_path = current
    while current in cameFrom.Keys():
        current = cameFrom[current]
        

def A_star(start, goal, h):
    openSet = start

    cameFrom = {}

    gScore = {}
    gScore[start] = 0

# a = Kota()