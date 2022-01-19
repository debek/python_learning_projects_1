class Zawodnik:
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def bmi(self):
        bmi_ = self.waga/self.wzrost**2
        print(f"Moje BMI to: {bmi_}")

zaw1 = Zawodnik("Daniel", 1.91, 92)
zaw1.bmi()
