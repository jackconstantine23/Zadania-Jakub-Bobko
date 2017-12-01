kod_1 = raw_input('Podaj nowy kod do zamka szyfrowego: ');
print('Zablokowano zamek, podaj kod aby go odblokowac.')
kod_2 = raw_input('Podaj kod: ');
while kod_2 != kod_1:
    if kod_1 == kod_2:
        print('Podano prawodlowy kod.');
    else:
        print('Podano bledny kod! Podaj jeszcze raz');
        kod_2 = raw_input('Podaj kod: ');
print('Podano prawodlowy kod.'); 