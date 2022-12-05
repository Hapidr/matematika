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


validation = True
try:
    panjangIndeks = int(input("Jumlah memori yang tersedia : "))
    create(panjangIndeks)
    while (validation):
        key = int(input(
            "\nJika tidak ada kunci yang ditambahkan lagi masukkan q\nkunci : "))
        insert(key, panjangIndeks)
        printAble(panjangIndeks)
        # validate = input(
        # "Masukkan 'q' jika tidak ada kunci yang dimasukkan lagi\n")
        if str(key) == 'q'.lower():
            validation = False
            print(key)
except:
    print("Program Selesai.")
