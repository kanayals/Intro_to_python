# Case
# Kita diberi tugas untuk mengamati hewan

class hewan: # hewan itu nama class
    nama_hewan = "" #nama_hewan object
    jenis_hewan = "" 
    umur_hewan = 10 #object property dimana umur_hewam tidak bisa diubah private
    def __init__(self,nama,jenis): #ini disebut construktor
        self.nama_hewan = nama 
        self.jenis_hewan = jenis

    def makan(self): #parameter self jangan lupa
        print("Hewan sedangan makan!!!")


# Cara panggil
kucing = hewan("tom","british short hair")
# Cara panggil variabel
print("Nama kucing {nama}".format(nama= kucing.nama_hewan))
print("Jenis kucing {jenis}".format(jenis= kucing.jenis_hewan))
print("Umur hewan {umur}".format(umur = kucing.umur_hewan))
# manggil fungsi atau method
print("Sedang apakah kucing?")
kucing.makan()