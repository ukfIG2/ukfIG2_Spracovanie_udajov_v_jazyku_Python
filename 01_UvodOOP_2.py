class Zviera:
    def __init__(self, meno, vek, zvuk):
        self._meno = None
        self._vek = None
        self.zvuk = None
        self._uprav_meno(meno)
        self._uprav_vek(vek)
        self._uprav_zvuk(zvuk)

    def _uprav_meno(self, meno):
        if(meno!=''):
            self._meno = meno.title()
        else:
            raise "Meno je prazdne"
    
    def _zobraz_meno(self):
        return self._meno
    
    def _uprav_vek(self, vek):
        if isinstance(vek, int) and vek >= 0:
            self._vek = vek
        else:
            raise ValueError("Vek musí byť nezáporné celé číslo.")

    def _zobraz_vek(self):
        return self._vek
    
    def _uprav_zvuk(self, zvuk):
        self._zvuk = zvuk

    def _zobraz_zvuk(self):
        return self._zvuk
    
    def _info(self):
        print("Meno = {}, vek = {}. Robim '{}' ".format(self._meno, self._vek, self._zvuk))
    
    def __str__(self):
        return "Meno = {}, vek = {}. Robim '{}' ".format(self._meno, self._vek, self._zvuk)


Zviera1 = Zviera("panda", 22, "Nieco")
Zviera1._info()

Zviera1._uprav_meno("kon")
#print(Zviera1._zobraz_meno())
Zviera1._uprav_vek(11)
#print(Zviera1._zobraz_vek())
Zviera1._uprav_zvuk("Chrom chrom")
#print(Zviera1._zobraz_zvuk())
Zviera1._info()
print(Zviera1)

class pes(Zviera):
    def __init__(self, meno, vek, zvuk, farba):
       super().__init__(meno, vek, zvuk)
       self._farba = None
       self._setFarba(farba)
       
    def _setFarba(self, farba):
       self._farba = farba

    def _getFarba(self):
        return self._farba

    def __str__(self):
        return super().__str__() + "Farba = {}".format(self._farba)

Zviera2 = pes("Dunco", 11, "Hav, hav", "Cervena")
print(Zviera2._getFarba())
print(Zviera2)
