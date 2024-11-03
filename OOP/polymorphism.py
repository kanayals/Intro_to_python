# Kasus mobil

class Mobil:
    def hidupkan_mesin(self):
        return "Mobil Menyala!"


class ElectricMobil(Mobil):
    def hidupkan_mesin(self):
        return "Akinya soak!" #jadi pake return bukan print agar tidak keluar non di result


def start(Mobil):
    print(Mobil.hidupkan_mesin())


# Cara panggil
mobil = Mobil()
listrik = ElectricMobil()

start(mobil)
start(listrik)