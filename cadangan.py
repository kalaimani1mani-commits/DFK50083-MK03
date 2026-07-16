def analisis_stok_buku(inventori: dict) -> tuple:
    """
    Menganalisis status buku menggunakan operasi set untuk mengasingkan 
    buku yang mempunyai stok dan buku yang kehabisan stok (stok == 0).

    Parameters:
        inventori (dict): Kamus inventori semasa.

    Returns:
        tuple: Mengandungi dua set (set_tersedia, set_habis_stok).
    """
    set_semua = set(inventori.keys())
    set_habis_stok = set()
    
    for id_buku, info in inventori.items():
        if info["stok"] == 0:
            set_habis_stok.add(id_buku)
            

    set_tersedia = set_semua - set_habis_stok
    
    return set_tersedia, set_habis_stok