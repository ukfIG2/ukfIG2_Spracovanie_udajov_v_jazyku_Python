class Zviera:
    def __init__(self, meno, vek, zvuk):
        if(meno!=''):
            self._meno = meno.title()
        else:
            raise "Meno je prazdne"
        if(vek>0):
            self._vek=vek
        else:
            raise "Vek je menej ako nula"
        self._zvuk = zvuk

    def _uprav_meno(self, meno):
        if(meno!=''):
            self._meno = meno.title()
        else:
            raise "Meno je prazdne"
    
    def _zobraz_meno(self):
        return self._meno
    
    def _uprav_vek(self, vek):
        if(vek>0):
            self._vek=vek
        else:
            raise "Vek je menej ako nula"

    def _zobraz_vek(self):
        return self._vek
    
    def _uprav_zvuk(self, zvuk):
        self._zvuk = zvuk

    def _zobraz_zvuk(self):
        return self._zvuk
    
    def _info(self):
        print("Meno = {}, vek = {}. Robim '{}' ".format(self._meno, self._vek, self._zvuk))
    
Zviera1 = Zviera("panda", 22, "Nieco")
Zviera1._info()

Zviera1._uprav_meno("kon")
#print(Zviera1._zobraz_meno())
Zviera1._uprav_vek(11)
#print(Zviera1._zobraz_vek())
Zviera1._uprav_zvuk("Chrom chrom")
#print(Zviera1._zobraz_zvuk())
Zviera1._info()
