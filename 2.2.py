import numpy as np;
class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart; 
        self.i = imagpart;
    def conjugate(self):
        self.i = -1*self.i;
    def absolute(self):
        return pow((pow(self.i,2)+pow(self.r,2)),0.5);
    def phase(self):
        return np.tan(self.r/self.i);
    def __add__(self,other):
        total_r = self.r + other.r
        total_i = self.i + other.i
        return Complex(total_r,total_i)
    def __sub__(self,other):
        total_r = self.r - other.r
        total_i = self.i - other.i
        return Complex(total_r,total_i)

x_1 = Complex(1,-1);
x_2 = Complex(2,3);
x_1.conjugate();
print('Sprzezenie x_1: '+str(x_1.r)+'+i('+str(x_1.i)+')');
abs = x_1.absolute();
print('Modul x_1: ' + str(abs));
ph = x_1.phase();
print('Faza x_1: ' + str(ph));
x_3 = x_2 + x_1;
print('Dodanie do x_1, x_2: '+str(x_3.r)+'+i('+str(x_3.i)+')');
x_4 = x_2 - x_1;
print('Odjecie od x_1, x_2: '+str(x_4.r)+'+i('+str(x_4.i)+')');