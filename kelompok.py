
def h(k, m):
    return k % m


ruang = []
freeSpace = int(input("Masukkan ruang memori yang tersedia : "))
data = int(input("Jumlah data yg diinputkan : "))
count = 0

for i in range(freeSpace):
    ruang.append([])
    if len(ruang) == freeSpace:
        for j in range(data):
            kunci = int(input("Masukkan kunci : "))
            if len(ruang[h(kunci, freeSpace) + count]) != 0:
                count += 1
            else:
                ruang[h(kunci, freeSpace)].append(kunci)


print(f"\nhasil akhir\n{ruang}")
