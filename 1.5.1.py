import os

rootdir = '/home/hwalgodecha/PycharmProjects'

for root,dir,files in os.walk(rootdir):
    print root;     #foldery
    print files;    #pliki w folderach
    for file in files:
        print os.path.join(root, file) 