import datetime

# Daftar produk
produk = {
    "001": {"nama": "Pulpen", "harga": 3000, "stok": 20},
    "002": {"nama": "Buku Tulis", "harga": 5000, "stok": 15},
    "003": {"nama": "Penghapus", "harga": 2000, "stok": 30},
    "004": {"nama": "Penggaris", "harga": 4000, "stok": 10},
}

keranjang = []
total_pemasukan = 0  # menyimpan hasil uang penjualan

# Menampilkan produk
def tampilkan_produk():
    print("\n=== Daftar Produk ===")
    print("Kode   Nama             Harga   Stok")
    for kode, data in produk.items():
        print(f"{kode}  {data['nama']:<15} {data['harga']:<7} {data['stok']}")

# Tambah ke keranjang
def tambah_ke_keranjang():
    kode = input("Masukkan kode produk: ")
    if kode not in produk:
        print("❌ Produk tidak ditemukan!")
        return
    
    jumlah = int(input("Jumlah beli: "))
    if jumlah > produk[kode]["stok"]:
        print("❌ Stok tidak cukup!")
        return
    
    keranjang.append((kode, jumlah))
    produk[kode]["stok"] -= jumlah
    print("✔ Ditambahkan ke keranjang!")

# Hitung total
def hitung_total():
    total = 0
    print("\n=== Struk Belanja ===")
    for kode, jumlah in keranjang:
        nama = produk[kode]["nama"]
        harga = produk[kode]["harga"]
        subtotal = harga * jumlah
        total += subtotal
        print(f"{nama} x{jumlah} = Rp{subtotal}")
    
    print(f"\nTotal Belanja: Rp{total}")
    return total

# Simpan transaksi dan pemasukan
def simpan_transaksi(total):
    global total_pemasukan  # akses variabel global
    total_pemasukan += total

    with open("penjualan.txt", "a") as f:
        waktu = datetime.datetime.now()
        f.write(f"\n=== Transaksi ({waktu}) ===\n")
        for kode, jumlah in keranjang:
            nama = produk[kode]["nama"]
            harga = produk[kode]["harga"]
            subtotal = harga * jumlah
            f.write(f"{nama} x{jumlah} = Rp{subtotal}\n")
        f.write(f"Total: Rp{total}\n")

    print("✔ Transaksi tersimpan!")
    keranjang.clear()

# Menampilkan hasil uang penjualan
def tampilkan_pemasukan():
    print(f"\n💰 Total hasil uang penjualan saat ini: Rp{total_pemasukan}")

# Program utama
while True:
    print("\n===== StoreSale =====")
    print("1. Lihat Produk")
    print("2. Tambah ke Keranjang")
    print("3. Checkout")
    print("4. Lihat Total Hasil Penjualan")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_produk()
    elif pilihan == "2":
        tambah_ke_keranjang()
    elif pilihan == "3":
        total = hitung_total()
        simpan_transaksi(total)
    elif pilihan == "4":
        tampilkan_pemasukan()
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid!")