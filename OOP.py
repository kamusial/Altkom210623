class Auto:
    def __init__(self, barwa, info_wprowadzone):
        self.kolor = barwa
        self.kondyncja = info_wprowadzone
        self.ilosc_paliwa = 10
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
            print('Ustawiono eco')
        elif tryb == 'normal':
            self.tryb_ekonomiczny = False
            self.spalanie_na_100 = 14
            print('ustawiono normal')
        else:
            print('zły wybor, bez zmian')

    def wlacz_eco(self):
        self.tryb_ekonomiczny = True
        self.spalanie_na_100 = 10
        print('Ustawiono eco')

    def wlacz_normal(self):
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        print('ustawiono normal')


    def __str__(self):
        napis = f'Auto ma kolor {self.kolor} i jest w kondycji {self.kondyncja}'
        return napis

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)


bmw1 = Auto('red', 5)

print(bmw1.kolor)
print(bmw1.zasieg())
print(bmw1)
bmw1.wlacz_eco()
print(bmw1.spalanie_na_100)



class Pracownik:
    pass