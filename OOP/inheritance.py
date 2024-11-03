# Kasus
# Manusia

class Ibu:
    #panggilan = "default"
    def __init__(self,panggilan,sifat): #ini constructor harus diisi satt di panggil. notes : def itu definisi 
        self.panggilan = panggilan
        self.__sifat = sifat

    def memanggil(self):
        print("Iyaa, Ada apa??")
    
    # Enkapsulasi mode
    def setsifat(self,sifat):
        self.__sifat= sifat
    def getsifat(self):
        return self.__sifat


class anak(Ibu):
    def suruh(self):
        print("Nanti dulu lahhh!!")

#sekolah = anak()
sekolah = anak("Anja","Malas")

print("Siapa nama anak ini : {nama_anak}".format(nama_anak = sekolah.panggilan)) #panggilan itu di property
sekolah.memanggil() #memanggil parameter fungsi