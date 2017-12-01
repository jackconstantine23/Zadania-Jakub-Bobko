from PIL import Image;

import os;
os.mknod('foto.jpg');                  #os.mknod tworzy pusty plik o dowolnym rozszerzeniu


im = Image.open("zdjecie.jpg")
im.save("zdjecie.png")