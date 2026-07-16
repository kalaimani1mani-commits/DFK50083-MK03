def bina_inventori(senarai_bersih: list) -> dict:
    """
    Membina dictionary inventori menggunakan ID buku sebagai kunci.

    Parameters:
        senarai_bersih (list): Senarai tuple data buku yang telah dibersihkan.

    Returns:
        dict: Kamus inventori dengan format {id_buku: {nama, harga, stok}}.
    """
    inventori = {}
    for id_buku, nama, harga, stok in senarai_bersih:
        inventori[id_buku] = {
            "nama": nama,
            "harga": harga,
            "stok": stok
        }
    return inventori

def kemaskini_stok(inventori: dict, id_buku: str, jumlah_tambahan: int) -> dict:
    """
    Mengemaskini jumlah stok buku secara dinamik dengan semakan keselamatan kunci.

    Parameters:
        inventori (dict): Kamus inventori semasa.
        id_buku (str): ID bagi buku yang ingin dikemas kini.
        jumlah_tambahan (int): Bilangan stok yang ingin ditambah.

    Returns:
        dict: Kamus inventori yang telah dikemas kini.
    """
    id_buku = id_buku.upper()
    
    if id_buku in inventori:
        inventori[id_buku]["stok"] += jumlah_tambahan
        print(f"[SISTEM]: Stok untuk {id_buku} berjaya ditambah sebanyak {jumlah_tambahan} unit.")
    else:
        print(f"[AMARAN]: Kemaskini gagal. ID Buku '{id_buku}' tidak wujud dalam inventori.")
        
    return inventori