import os
import shutil  

path = input("path: ")
dst = input("sidt: ")
 
path = "/home/pi/media/tv/Hunter X Hunter"
dst = "/home/pi/media/tv/Hunter X Hunter"


def rename(m_path: str):
    ls = os.listdir(m_path)
    for name in ls:
        epn = int(name.split(".")[-2].split("_")[-1])
        shutil.move(m_path + "/" + name, dst + "/ep " + str(epn))
rename(path)
