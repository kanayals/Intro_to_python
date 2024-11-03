from abc import ABC , abstractmethod

class kendaraan(ABC):
    @abstractmethod
    def nyalakan_mesin(self):
        pass

class mobil(kendaraan):
    def nyalakan_mesin(self):
        return "Start"
    
class motor(kendaraan):
    def nyalakan_mesin(self):
        return "Motor Mogok"
    
#kendaraan = kendaraan()
#print(kendaraan.nyalakan_mesin())

mobil = mobil()
print(mobil.nyalakan_mesin())