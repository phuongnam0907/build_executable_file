class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        if self.imag < 0:
            print(f'{self.real}{self.imag}j')
        else:
            print(f'{self.real}+{self.imag}j')