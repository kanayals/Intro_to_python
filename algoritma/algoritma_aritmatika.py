x = 9
y = 2

#note: klo mau pilih file yg mana tinggal tab aja untuk ganti-gantinya

#Penjumlahan (note: select a lalu ctrl D)
hasil = x+y
print("Hasil tambah dari {a} + {b} = {hasil}".format(a=x,b=y,hasil=hasil))
#Pengurangan
hasil = x-y
print("Hasil kurang dari {0} - {1} = {2}".format(x,y,hasil)) #pakai posisi
#Perkalian
hasil = x * y
print("Hasil kali dari {a} * {b} = {hasil}".format(hasil=hasil,a=x,b=y)) #lebih fleksibel dr posisi karena bisa ditukar-tukar hasilnya di depan atau belakang
#Pembagian
hasil = x/y
print("Hasil bagi dari {a} / {b} = {hasil}".format(a=x,b=y,hasil=hasil))
#Modulus
hasil = x % y
print("Hasil sisa bagi dari {a} % {b} = {hasil}".format(a=x,b=y,hasil=hasil))
#Perpangkatan
hasil = x ** y
print("Hasil dari pangkat {a} ^ {b} = {hasil}".format(a=x, b=y, hasil=hasil)) # (^) simbol pangkat yang di print mengacu pada UI/UX atau biasanya yang di kalkulator

#Increment atau mirip seperti comparison
nilai = 0
#nilai = nilai + 1
nilai += 1
print("Hasil dari increment {nilai} = {nilai} + 1 : {nilai}".format(nilai=nilai))
#nilai = nilai - 1
nilai -= 1
print("Hasil dari increment {nilai} = {nilai} - 1 : {nilai}".format(nilai=nilai))