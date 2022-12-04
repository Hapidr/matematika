table = {}
total = 0


def create(b):
    for i in range(b):
        table[i] = None


def insert(key, b):
    global total
    hash = key % b
    flag = 0
    if table[hash] == None:
        table[hash] = key
    else:
        for i in range(0, b):
            hash = (key+i) % b
            if table[hash] == None:
                table[hash] = key
                total += key
                flag += 1
                break
        if flag == 0:
            print("Tabel sudah penuh")


def printAble(b):
    for i in range(b):
        print(table[i], end=" | ")
    print("")


panjangIndeks = int(input("Masukkan jumlah memori kosong : "))
create(panjangIndeks)
validation = True
try:
    while (validation):
        key = int(input("Masukkan kunci : "))
        insert(key, panjangIndeks)
        printAble(panjangIndeks)
        confirmation = input("Tambah data (Y/n) : ")
        if confirmation != 'y'.lower():
            validation = False
except:
    print("Nilai yang anda masukkan tidak sesuai!")
