#Tipe data atau Inisialiasi Data
#Format Dasar
#nama_variable = { key:value, key:value2 }

biodata_simple = {
    "nama" : "Kanaya Lintang Salsabila",
    "age" : "22",
    "temppat lahir" : "Bogor"
}

#Cetak Nilai
print(biodata_simple)

#Mengambil Nilai Spesifik
#Biodata_simple("nama")
print("\nHello, nama Anda siapa : {nama}".format(nama= biodata_simple["nama"]))
#Biodata_simple.get("Age")
print("{nama}, saya berumur : {age}".format(nama = biodata_simple.get("nama"), age = biodata_simple.get("age")))

#Menambahkan key dan value 
biodata_simple["tanggal_lahir"] = "18-May-2002"
print("\nData Setelah di Update: ")
print(biodata_simple)

#Mengubah nilai 
biodata_simple["tanggal_lahir"] = "04-Mar-2000"
print("\nSetalah di ganti format Tanggal lahirnya : ")
print(biodata_simple)

#Menghapus nilai
del biodata_simple["tanggal_lahir"]
print("\nData setelah di hapus : ")
print(biodata_simple)

#Check key yang ada
print("\nlist key : ")
print(biodata_simple.keys())
print("list value : ")
print(biodata_simple.values())