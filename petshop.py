from prettytable import PrettyTable
daftarbarang = [ 
    {"ID": 1, "Nama Barang":"Whiskas Kucing", "Harga Barang": 12000, "Stock Barang": 12 },
    {"ID": 2, "Nama Barang":"Whiskas Hamster", "Harga Barang": 12000, "Stock Barang": 16 },
    {"ID": 3, "Nama Barang":"Whiskas Anjing", "Harga Barang": 19000, "Stock Barang": 17 } 
]

def listbarang():
    table = PrettyTable(["ID", "Nama Barang", "Harga Barang", "Stock Barang"])
    for produk in daftarbarang:                                                 
        table.add_row([produk["ID"], produk["Nama Barang"], produk["Harga Barang"], produk["Stock Barang"]])
    print(table)

def tambahbarang():
    global id_barang
    id_barang = int(input("Masukkan ID Barang: "))
    nama_barang = str(input("Masukkan Nama Barang: "))
    harga_barang = int(input("Masukkan Harga Barang: "))
    stock_barang = int(input("Masukkan Stock Barang: "))
    daftarbarang.append({"ID": id_barang, "Nama Barang": nama_barang, "Harga Barang": harga_barang, "Stock Barang": stock_barang})
    print("Barang Berhasil Ditambah")

def updatebarang():
    listbarang() 
    id_barang = int(input("Masukkan ID Barang Yang Ingin Anda Ubah(ID Harus Sesuai!): "))
    for produk in daftarbarang:
        if (produk['ID'] == id_barang):
            nama_barang = str(input("Ubah Nama Barang: "))
            harga_barang = float(input("Ubah Harga Barang: "))
            stock_barang = int(input("Ubah Stock Barang: "))
            produk["Nama Barang"] = nama_barang
            produk["Harga Barang"] = harga_barang
            produk["Jumlah Barang"] = stock_barang
            print("Barang Berhasil iubah!") 
            return
        else:
            print("ID barang tidak ditemukan")

def hapusbarang():
    listbarang()
    id_barang = int(input("Masukkan Barang Yang Ingin Di Hapus(Masukkan Sesuai ID): "))
    for produk in daftarbarang:
        if produk['ID'] == id_barang:
            daftarbarang.remove(produk)
            print("Barang Berhasil Di Hapus")
            return
            

def pembayaran():
    checkout = []
    total = 0

    listbarang()
    while True:
        print("================================")
        id_barang = int(input("Masukkan ID Barang Yang ingin anda beli: "))
        if id_barang == 0:
            break
        terbeli = None
        for i in daftarbarang:
            if (i['ID'] == id_barang):
                terbeli = i
                break

        if terbeli:
            subtotal = int(input("Masukkan Jumlah Barang Yang Ingin Anda Beli: "))
            if subtotal <= terbeli["Stock Barang"]:
                terbeli["Stock Barang"] -= subtotal
                checkout.append({"Nama Barang" : terbeli["Nama Barang"], "Harga Barang" : terbeli["Harga Barang"], "Stock Barang" : terbeli["Stock Barang"] })
                total += terbeli["Harga Barang"] * subtotal
                print("Barang Yang Anda Beli Berhasil Masuk Ke Keranjang")
            else:
                print("Produk Tidak Cukup")
        else:
            print("ID Tidak Valid.")

    print("==================================") 
    print("Detail Transaksi")
    tabelcheckout = PrettyTable(["Nama Barang", "Harga Barang", "Total Pembelian", "Total Harga"])
    for item in checkout:
        namaitem = item["Nama Barang"]
        hargaitem = item["Harga Barang"]
        totalitem = item["Stock Barang"]
        totalhargaitem = hargaitem * totalitem
        tabelcheckout.add_row([namaitem, hargaitem, totalitem, totalhargaitem])
    print(tabelcheckout)
    print("Total Harga Item Anda: Rp", total)
       
def login():
        print("================================")
        print("=     ----Pilih Login----      =")
        print("=           1.Admin            =")
        print("=           2.Pembeli          =")
        print("================================")
     
        login = int(input("Ingin Login Sebagai Apa? (1/2):"))
    
        if login == 1:
            user = str(input("Masukkan Username :"))
            pw = str(input("Masukkan Password :"))

            print("===== Selamat Datang Admin =====")
            print(f"\nHallo Admin {user}, Selamat Datang")
            print(f"\nPassword Anda {pw}\n")
            while True:
                print("===================")
                print("Menu Admin")
                print("1.Tampilkan Barang")
                print("2.Tambah Barang")
                print("3.Edit Barang")
                print("4.Hapus Barang")
                print("5.Keluar")
                print("===================")

                menuadmin = int(input("Pilih Menu (1,2,3,4,5): "))
                if menuadmin == 1:
                    listbarang()
                elif menuadmin == 2:
                    tambahbarang()
                elif menuadmin == 3:
                    updatebarang()
                elif menuadmin == 4:
                    hapusbarang()
                elif menuadmin == 5:
                    print("Semangat Adminku Ganteng CIntaku")
                    break
                else:
                    print("Menu Tidak Tersedia.")
        elif login == 2:
            user = str(input("Masukkan Username :"))
            pw = str(input("Masukkan Password :"))
            print("==========================================")
            print(f"Selamat Datang {user} password anda {pw}")
            print("==========================================")
            while True:
                listbarang()
                print("===================")
                print("Menu Pembeli")
                print("1.Beli Barang")
                print("2.Keluar")
                print("===================")

                menuuser = int(input("Pilih Menu (1,2): "))     
                if menuuser == 1:
                    pembayaran()
                elif menuuser == 2:
                    print("Terimakasih Telah belanja di toko kami")
                    break
                else:
                    print("Pilihan Anda Tidak ada")
        

login()
