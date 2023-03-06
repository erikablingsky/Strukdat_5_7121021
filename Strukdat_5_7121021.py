class Karyawan:
    _nama = ""
    _umur = 0
    _jenisKelamin = None
    _upahPerHari = None

    def __init__(self, nama: str, umur: int):
        self._nama = nama
        self._umur = umur

    def setJenisKelamin(self, jenisKelamin):
        self._jenisKelamin = jenisKelamin

    def setUpahPerHari(self, upahPerHari):
        self._upahPerHari = upahPerHari

    def hitungGajiBulanan(self, bulan):
        if self._upahPerHari is None:
            print("ERROR! Upah per Hari belum di inputkan")
        else:
            print("Gaji Bulan ini : Rp", self._upahPerHari * bulan)

    def printInfo(self):
        print(f"========== INFO ==========")
        print(f"Nama : {self._nama}")
        print(f"Umur : {self._umur}")
        print(f"Jenis Kelamin : {self._jenisKelamin}")
        print(f"Upah per Hari : {self._upahPerHari}")


orang1 = Karyawan("Haniif", 90)
orang1.printInfo()

orang2 = Karyawan("Sindu", 190)
orang2.setJenisKelamin("Laki-laki")
orang2.setUpahPerHari(30000)
orang2.printInfo()

orang1.hitungGajiBulanan(28)
orang2.hitungGajiBulanan(30)
