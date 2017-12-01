
print('Obliczanie pierwiastkow rownania kwadratowego:');
a = float(input('Podaj a:'));
b = float(input('Podaj b:'));
c = float(input('Podaj c:'));
delta = (b*b)-4*a*c; 

if (delta < 0):
    delta = abs(delta);
    pdelta = pow(delta, 1 / 2.0);
    print('Delta ujemna: ');
    print('X_1: (-'+str(b)+'+'+str(pdelta)+'i)/'+'('+str(2*a)+')');
    print('X_2: (-'+str(b)+'-'+str(pdelta)+'i)/'+'('+str(2*a)+')');
else:
    pdelta = pow(delta,1/2.0);
    if delta > 0:
        print('Delta dodatnia: ');
        x_1 = (-b-pdelta)/(2*a);
        x_2 = (-b+pdelta)/(2*a);
        print('X_1:', x_1);
        print('X_2:', x_2);
    elif delta == 0:
        print('Delta rowna zero: ');
        x_0 = -b/(2*a);
        print('X_0:',x_0);

