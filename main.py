class Moskalyk:
    Alive = False
    IQ = -10
    Name = "Chmonya"
    Chromosomes = 47

    def Info(self):
        print(f'Alive: {self.Alive}\nIQ: {self.IQ}\nName: {self.Name}\nChromosomes: {self.Chromosomes}')

    def Vid(self):
        Alive = False

    def Loh(self, Name_changed):
        self.Name = self.Name + Name_changed

student1 = Moskalyk()
student1.Info()
student1.Loh("200")
student1.Info()