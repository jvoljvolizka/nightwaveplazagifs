import os

i = 1

while i != 81:
    os.system("wget https://plaza.one/img/backs/" + str(i).zfill(2) +".gif")
    i = i+1
