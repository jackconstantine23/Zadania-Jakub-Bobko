import os;
dir = '/home/hwalgodecha/PycharmProjects/Lab_1';
print(os.getcwd());                                 #wyswiela sciezke w ktorej jestesmy
os.chdir(dir);                                      #przechodzimy do katalogu od ktorego zaczynamy
print(os.path.dirname(dir));                        #wyswietla katog wyzej


while dir != '/':
    print(os.getcwd());
    #print [name for name in os.listdir(dir) if os.path.isfile(name)];
    print [name for name in os.listdir(dir)]; 
    os.chdir(os.path.dirname(dir));
    dir = os.getcwd();