import numpy as np
import pyfiglet
import os


class Graph():

    # Constructor Function
    def __init__(self):
        self.vertex = 0
        self.data = None
        self.repeat = []
        self.directed = 0
        self.stack = []
        self.travelled = []
        self.way = []
        self.delim = ">"
        self.checkifloop = []
        self.counter = 0
        self.degreeMatrix = None
        self.degree = 0
        self.connect = []

    # Method untuk membuat matriks dan mengisinya dengan nilai
    def fill(self):
        self.vertex = int(input(">> Masukkan jumlah vertex: "))
        self.data = np.zeros((self.vertex, self.vertex))
        self.directed = int(input(">> Apakah ini matrix tidak berarah jika iya input 1, jika tidak input 0:: "))
        for i in range(self.vertex):
            for j in range(self.vertex):
                repeat = [i, j]
                if i == j:
                    continue
                if self.directed == 1 and repeat in self.repeat:
                    continue
                else:
                    temp = int(input(f">> Jika {i+1} {j+1} terhubung input 1, jika tidak input 0: "))
                    if self.directed == 1:
                        if temp == 1:
                            self.data[i][j] = temp
                            self.data[j][i] = temp
                        else:
                            self.data[i][j] = 0
                    self.repeat.append(repeat)
                    repeat = [j, i]
                    self.repeat.append(repeat)
                    if self.directed == 0:
                        if temp == 1:
                            self.data[i][j] = temp
                        else:
                            self.data[i][j] = 0
        self.repeat = []

    # Method untuk output matriks yang sudah di isi
    def getMatrix(self):
        print(">> Matriks:")
        print(self.data)

    # Method untuk mengecek apakah matriks berarah atau tidak
    def isDirected(self):
        if self.directed == 1:
            return True
        else:
            for i in range(self.vertex):
                for j in range(self.vertex):
                    if i != j:
                        if self.data[i][j] != self.data[j][i]:
                            return False
            return True

    # Method untuk mencari rute antara a ke b dalam matriks
    def pathfind(self, asal, tujuan):
        tujuan -= 1
        asal -= 1
        self.travelled.append(asal)
        self.stack.append(asal)
        if self.data[asal][tujuan] == 1:
            self.stack.append(tujuan)
            for i in self.stack:
                self.way += (str(i+1) + self.delim)
            print(f">> Rute dari {self.way[0]} ke {tujuan + 1} adalah {self.way[:-1]}")
            self.way = []
            self.stack = []
            self.travelled = []
        else:
            for i in range(self.vertex):
                if self.data[asal][i] == 1 and i not in self.travelled:
                    asal = i+1
                    tujuan += 1
                    return self.pathfind(asal, tujuan)
                else:
                    continue
            if len(self.stack) >= 1:
                tujuan += 1
                self.stack.pop()
                asal = self.stack.pop(-1) + 1
                self.checkifloop.insert(0, asal)
                self.travelled.pop(-2)
            if not self.stack:
                return print(">> Tidak ada jalan kesana")
            return self.pathfind(asal, tujuan)

    # Method untuk mencari derajat matriks
    def getdegreeMatrix(self):
        self.degreeMatrix = np.zeros((self.vertex, self.vertex))
        if self.isDirected():
            for i in range(self.vertex):
                for j in range(self.vertex):
                    if i == j:
                        for k in range(self.vertex):
                            if self.data[i][k] == 1:
                                self.degree += 1
                        self.degreeMatrix[i][j] = self.degree
                        self.degree = 0
            print("Matriks Derajat:")
            print(self.degreeMatrix)
        else:
            for i in range(self.vertex):
                for j in range(self.vertex):
                    if i == j:
                        for k in range(self.vertex):
                            if self.data[i][k] == 1:
                                self.degree += 1
                        self.degreeMatrix[i][j] = self.degree
                        self.degree = 0
            print("Matriks Derajat Masuk:")
            print(self.degreeMatrix)
            for a in range(self.vertex):
                for b in range(self.vertex):
                    if a == b:
                        for c in range(self.vertex):
                            if self.data[c][a] == 1:
                                self.degree += 1
                        self.degreeMatrix[a][b] = self.degree
                        self.degree = 0
            print("Matriks Derajat Keluar:")
            print(self.degreeMatrix)

    # Method rekursi untuk mencari tempat" yang terkoneksi
    def checkConnected(self, baba):
        for i in range(self.vertex):
            if self.data[baba][i] == 1 and i not in self.connect:
                self.connect.append(i)
                self.checkConnected(i)

    # Method untuk mengecek apakah graph terhubung atau tidak
    # Definisi terkoneksi adalah bisa kemana aja, dari mana aja
    def getConnected(self, baba):
        self.checkConnected(baba)
        if len(self.connect) == self.vertex:
            print("Connected")
        else:
            print("Not Connected")
        self.connect = []


def main(adi):
    os.system("cls")
    for i in range(35):
        print("=", end =' ')
    print(" ")
    result = pyfiglet.figlet_format("Representasi Matriks")
    print(result)
    for j in range(35):
        print("=", end =' ')
    print("")
    print("1. Buat Matriks \n2. Cek apakah matriks itu terkoneksi\n3. Cek apakah matriks berarah\n4. Cari Derajat Matriks\n5. Cari rute dari titik a ke b ")
    menu = int(input(">> Pilih yang ingin anda lakukan, (1-5): "))
    if menu == 1:
        adi.fill()
        adi.getMatrix()
        input()
        main(adi)
    elif menu == 2:
        connect = int(input(f">> Pilih ingin mulai mengecek dari mana(1-{adi.vertex})"))
        adi.getConnected(connect - 1)
        input()
        main(adi)
    elif menu == 3:
        directed = adi.isDirected()
        if directed:
            print(">> Matriks ini tidak berarah")
        else:
            print(">> Matriks ini berarah")
        input()
        main(adi)
    elif menu == 4:
        adi.getdegreeMatrix()
        input()
        main(adi)
    elif menu == 5:
        asal = int(input(">> Masukkan titik start: "))
        tujuan = int(input(">> Masukkan titik tujuan: "))
        adi.pathfind(asal, tujuan)
        input()
        main(adi)
    else:
        print("Pilihan tidak tersedia")
        main(adi)


adi = Graph()
main(adi)
