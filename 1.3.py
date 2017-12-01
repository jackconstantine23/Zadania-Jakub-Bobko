import os, os.path;
dir  = '/home/hwalgodecha/PycharmProjects/Lab_1';

#os.listdir wyswietla pliki i foldery w sciezce dir
#os.path.join wyswietli pelna sciezke do pliku czy folderu i jego nazwe
#os.path.isfile sprawdzi czy to plik
#os.path.isdir sprawdzi czy katalog
#obie wersje sa dobre !
print len([name for name in os.listdir(dir) if os.path.isfile(name)]);
print len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir,name))]);
 