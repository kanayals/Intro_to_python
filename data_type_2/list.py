#untuk kembali (cd ..)
#untuk masuk list (ls)
#untuk run (py [files])

#Prinsip programming (CRUD) Create, Read, Update, Delete

#Membuat list (Create)
fruits = ["apple","pisang","salak","semangka"]

#Mencetak semua nilai (Read)
print("======== Mencetak semua nilai ========")
print(fruits)

#Mencetak salah satu nilai
print("\n======== Mencetak salah satu nilai ========")
#namaVariabel[posisi_value]
#contoh semangka
print(fruits[2])

#misal nilainya min
#print nilai terakhir
print(fruits[-1])

#Menambahkan nilai (Update)
print("\n======== Menambahkan nilai ========")
fruits.append("jeruk")
print(fruits)

#Menghapus nilai (Delete)
print("\n======== Menghapus nilai dalam List ========")
fruits.remove("pisang")
print(fruits)

#Mengubah nilai list value jeruk menjadi mangga
print("\n======== Mengubah nilai list value jeruk menjadi mangga ========")
fruits[-1] = "mangga"
print(fruits)

print("\n======== Menghapus nilai mangga dalam List ========")
fruits.remove("mangga")
print(fruits)

#Menambah dua data atau lebih menggunakan Increment
print("\n======== Menambah dua data atau lebih menggunakan Increment ========")
buah = ["tomat", "alpukat"]
#fruits = fruits + buah
fruits += buah
print(fruits)