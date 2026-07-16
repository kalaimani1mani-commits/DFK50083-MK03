def bersihkan_data(data_mentah: str) -> list:
    """
    Membersihkan string data mentah, memecahkannya kepada rekod individu, 
    dan menukarkan jenis data harga (float) serta stok (int) secara selamat.

    Parameters:
        data_mentah (str): String data mentah daripada senarai kumpulan.

    Returns:
        list: Senarai tuple yang mengandungi (id_buku, nama_buku, harga, stok).
    """
    senarai_bersih = []
    
    # Memisahkan setiap buku berasaskan karakter koma
    rekod_buku = data_mentah.split(",")
    
    for rekod in rekod_buku:
        rekod = rekod.replace("\n", "").strip()
        
        if not rekod:
            continue
            
        bahagian = rekod.split(":")
        
        if len(bahagian) == 4:
            id_buku = bahagian[0].strip().upper()
            nama_buku = bahagian[1].strip().title()
            
            try:
                harga_str = bahagian[2].replace(" ", "")
                stok_str = bahagian[3].replace(" ", "")
                
                harga = float(harga_str)
                stok = int(stok_str)
            except ValueError:
                print(f"[RALAT BATAL]: Data nombor tidak sah pada rekod '{rekod}'. Rekod diabaikan.")
                continue
                
            senarai_bersih.append((id_buku, nama_buku, harga, stok))
            
    return senarai_bersih