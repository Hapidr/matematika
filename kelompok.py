
def h(k,m):
  return k%m

ruang = []
freeSpace = int(input("Masukkan ruang memori yang tersedia : "))
data = int(input("Jumlah data yg diinputkan: "))

for i in range(freeSpace):
  ruang.append([])
  if len(ruang) == freeSpace:
    for j in range(data):
      kunci = int(input("Masukkan kunci : "))
      ruang[h(kunci, freeSpace)].append(kunci)

print(ruang)