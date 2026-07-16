# Mengimport modul-modul tersuai mengikut seni bina multi-file
from pembersihan import bersihkan_data
from inventori import bina_inventori, kemaskini_stok
from cadangan import analisis_stok_buku
from pesanan import proses_pesanan

def papar_laporan(inventori: dict):
    """Mencetak status inventori semasa secara kemas dan selari."""
    print("\n" + "="*60)
    print(f"{'ID':<6} | {'NAMA BUKU':<30} | {'HARGA (RM)':<10} | {'STOK':<5}")
    print("="*60)
    for id_buku, info in inventori.items():
        print(f"{id_buku:<6} | {info['nama']:<30} | {info['harga']:>10.2f} | {info['stok']:>5}")
    print("="*60)

def main():
    data_mentah = " b007:pEnGaTuRcArAn jUnIoR:35.50:6 , b008:dAtA mInInG mUdAh:55.90:1 ,b009:fIkSyEn sAiNs mOdEn:42.00:0 "
    
    print("--- FASA 1: PEMBERSIHAN DATA MENTAH ---")
    senarai_bersih = bersihkan_data(data_mentah)
    print(f"Data Berjaya Dibersihkan: {senarai_bersih}")
    
    print("\n--- FASA 2: PEMBINAAN INVENTORI ASAL ---")
    inventori_buku = bina_inventori(senarai_bersih)
    papar_laporan(inventori_buku)
    
    print("\n--- FASA 3: PENGEMASKINIAN STOK DINAMIK ---")
    inventori_buku = kemaskini_stok(inventori_buku, "b012", 5)
    inventori_buku = kemaskini_stok(inventori_buku, "b999", 10)
    
    print("\n--- FASA 4: SIMULASI PESANAN PELANGGAN ---")
    berjaya, bil, nama = proses_pesanan(inventori_buku, "b010", 2)
    if berjaya:
        print(f"[RESIT]: Pembelian 2 unit '{nama}' berjaya! Jumlah: RM{bil:.2f}")
        
    proses_pesanan(inventori_buku, "b011", 5)

    print("\n--- FASA 5: ANALISIS SET (CADANGAN & STATUS) ---")
    tersedia, habis_stok = analisis_stok_buku(inventori_buku)
    print(f"Set ID Buku Tersedia   : {tersedia}")
    print(f"Set ID Buku Habis Stok : {habis_stok}")
    
    print("\n--- LAPORAN AKHIR SISTEM E-BOOKSTORE ---")
    papar_laporan(inventori_buku)

if __name__ == "__main__":
    main()