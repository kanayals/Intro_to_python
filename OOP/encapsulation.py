# Kasus mobil

class mobil:
    def __init__(self,nama,merek):
        self.nama= nama
        self.__merek= merek #__ untuk menyembunyikan nilai sensitif agar tidak menimbulkan error tingkat lanjut (agar tidak bisa diedit)

    # Untuk mengambil atau mengubah data sensitif bisa pakai setter and getter
    # Setter and getter
    def setmerek(self,merek):
        self.__merek = merek

    # get mengambil
    def getmerek(self):
        return self.__merek



honda = mobil("CIVIC TURBO", "HONDA")

print("Saya punya mobil : {nama_mobil}".format(nama_mobil =honda.nama))
# karna sudah ada seter maka bisa diubah dengan cara
# honda.setmerek("Toyota") 
# jadi print("Dengan merek: {merek}".format(merek= honda.setmerek("Toyota")))
print("Dengan merek: {merek}".format(merek= honda.getmerek()))