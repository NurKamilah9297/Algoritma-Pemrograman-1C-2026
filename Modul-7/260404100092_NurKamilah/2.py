playlist = {}

while True:
    print("\n1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        playlist[nama] = {}

    elif pilih == "2":
        nama = input("Nama playlist: ")

        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Nama penyanyi: ")
            playlist[nama][judul] = penyanyi
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "3":
        for nama, lagu in playlist.items():
            print("\nPlaylist:", nama)
            for judul, penyanyi in lagu.items():
                print(judul, "-", penyanyi)

    elif pilih == "4":
        cari = input("Judul lagu: ")
        ketemu = False

        for nama, lagu in playlist.items():
            if cari in lagu:
                print("Ditemukan di:", nama)
                print("Penyanyi:", lagu[cari])
                ketemu = True

        if ketemu == False:
            print("Lagu tidak ditemukan")

    elif pilih == "5":
        nama = input("Nama playlist: ")

        if nama in playlist:
            judul = input("Judul lagu: ")

            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu dihapus")
            else:
                print("Lagu tidak ditemukan")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "6":
        nama = input("Nama playlist: ")

        if nama in playlist:
            del playlist[nama]
            print("Playlist dihapus")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "7":
        break