def proses_pesanan(inventori: dict, id_buku: str, kuantiti: int) -> tuple:
    """
    Memproses simulasi transaksi pesanan buku secara selamat dan mengira jumlah bil.

    Parameters:
        inventori (dict): Kamus inventori semasa.
        id_buku (str): ID buku yang ingin dibeli.
        kuantiti (int): Jumlah unit yang ingin dibeli.

    Returns:
        tuple: (status_berjaya: bool, jumlah_bil: float, nama_buku: str)
    """
    id_buku = id_buku.upper()
    
    if id_buku not in inventori:
        print(f"[RALAT TRANSAKSI]: ID Buku '{id_buku}' tidak wujud.")
        return False, 0.0, "Tidak Wujud"
        
    buku = inventori[id_buku]
    
    if buku["stok"] >= kuantiti:
        # Tolak stok secara dinamik
        buku["stok"] -= kuantiti
        jumlah_bil = buku["harga"] * kuantiti
        return True, jumlah_bil, buku["nama"]
    else:
        print(f"[TRANSAKSI GAGAL]: Stok untuk '{buku['nama']}' tidak mencukupi (Baki: {buku['stok']}).")
        return False, 0.0, buku["nama"]