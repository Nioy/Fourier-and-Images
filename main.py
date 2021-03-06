from Image import Image
from Fourier import Fourier

im_1 = Image("images/pikachu.png", (200, 200))
im_2 = Image("images/einstein.jpg", (200, 200))
im_3 = Image("images/formula.jpeg", (200, 200))
im_4 = Image("images/dickbutt.jpg", (200, 200))
im_5 = Image("images/obama.jpg", (200, 200))

path_1 = im_1.sort()
path_2 = im_2.sort()
path_3 = im_3.sort()
path_4 = im_4.sort()
path_5 = im_5.sort()

Fourier(path_1).draw(1000, speed = 8, mode = 1, save = False, ani_name = "im1.gif")
Fourier(path_2).draw(1000, speed = 8, mode = 2, save = False, ani_name = "im2.gif")
Fourier(path_3, path_4).draw(1000, speed = 8, mode = 1, save = False, ani_name = "im3.gif")
Fourier(path_5).visualize(save = False, ani_name = "im5.gif")

