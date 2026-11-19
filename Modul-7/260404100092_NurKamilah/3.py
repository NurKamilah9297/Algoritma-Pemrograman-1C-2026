undangan = set()
webinar_A = set()
webinar_B = set()

print("Masukkan nama undangan (ketik selesai untuk berhenti)")
while True:
    nama = input("Nama: ")
    if nama == "selesai":
        break
    undangan.add(nama)

print("\nMasukkan peserta Webinar A")
while True:
    nama = input("Nama: ")
    if nama == "selesai":
        break
    webinar_A.add(nama)

print("\nMasukkan peserta Webinar B")
while True:
    nama = input("Nama: ")
    if nama == "selesai":
        break
    webinar_B.add(nama)

print("\n===== HASIL WEBINAR =====")

print("Semua peserta:", webinar_A | webinar_B)

print("Hadir di kedua webinar:", webinar_A & webinar_B)

print("Hadir di salah satu webinar:", webinar_A ^ webinar_B)

print("Tidak hadir:", undangan - (webinar_A | webinar_B))