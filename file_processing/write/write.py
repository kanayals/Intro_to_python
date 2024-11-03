open_file = open("Contoh_write_text.txt", "w") # run dulu dengan py, lalu panggil dengan type (nanti muncul file baru)
open_file.write("Ini contoh Text yang akan di print")
open_file.close()

open_file = open("Contoh_write_text2.txt", "r+") 
open_file.write("Ini contoh Text 2 yang akan di print")
print(open_file.read())
open_file.close()