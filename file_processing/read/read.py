# case
# membaca file yang ada di file_laporan1.txt
# tampilkan
# "r" : read file
open_file = open("file_laporan1.txt", "r")
value = open_file.read()
print(value)
open_file.close()

# read ada 3:
# read
open_file = open("file_laporan1.txt", "r")
read_ = open_file.read()
print("\nContoh read : ")
print(read_)

# readline
open_file.seek(0) #gunanya untuk mengembalikan posisi pointer atau karakter atau kursor () yang kotak2 kecil gini
print("\nContoh penggunaan readline : ")
# gunanya untuk character
print(open_file.readline(120))

# readlines
open_file.seek(0)
print("\nContoh penggunaan readlines : ")
for line in open_file.readlines():
    print(line.strip())

open_file.close()